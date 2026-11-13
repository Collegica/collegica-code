"""River gauges: a first pixi project.

Reads a small table of made-up river gauges, fits flow against catchment
area with scikit-learn, spreads the readings over a grid, writes the grid
as a GeoTIFF with GDAL, and smooths it into a picture with OpenCV.
"""

from pathlib import Path

import cv2
import numpy as np
import pandas as pd
from osgeo import gdal, osr
from sklearn.linear_model import LinearRegression

gdal.UseExceptions()

DATA = Path("data/gauges.csv")
OUT = Path("output")
SIZE = 50  # cells along each side of the grid
MARGIN = 0.05  # degrees of padding around the gauges


def fit_flow(gauges: pd.DataFrame) -> tuple[float, float]:
    """Return the slope (m3/s per km2) and R squared of flow against catchment."""
    x, y = gauges[["catchment_km2"]], gauges["flow_m3s"]
    model = LinearRegression().fit(x, y)
    return float(model.coef_[0]), float(model.score(x, y))


def grid_bounds(gauges: pd.DataFrame) -> tuple[float, float, float, float]:
    """West, east, south and north edges of the grid, in degrees."""
    return (
        gauges.lon.min() - MARGIN,
        gauges.lon.max() + MARGIN,
        gauges.lat.min() - MARGIN,
        gauges.lat.max() + MARGIN,
    )


def idw_grid(gauges: pd.DataFrame, bounds, size: int = SIZE) -> np.ndarray:
    """Spread the gauge readings over a size x size grid by inverse-distance weighting."""
    west, east, south, north = bounds
    dx, dy = (east - west) / size, (north - south) / size
    xs = west + (np.arange(size) + 0.5) * dx  # cell centres, west to east
    ys = north - (np.arange(size) + 0.5) * dy  # cell centres, north to south
    gx, gy = np.meshgrid(xs, ys)
    dist = np.hypot(gx[..., None] - gauges.lon.to_numpy(), gy[..., None] - gauges.lat.to_numpy())
    weight = 1.0 / np.maximum(dist, 1e-9) ** 2
    return (weight * gauges.flow_m3s.to_numpy()).sum(axis=-1) / weight.sum(axis=-1)


def write_geotiff(grid: np.ndarray, bounds, path: Path) -> None:
    """Write the grid as a single-band GeoTIFF in WGS 84 (EPSG:4326)."""
    west, east, south, north = bounds
    rows, cols = grid.shape
    ds = gdal.GetDriverByName("GTiff").Create(str(path), cols, rows, 1, gdal.GDT_Float32)
    ds.SetGeoTransform((west, (east - west) / cols, 0, north, 0, -(north - south) / rows))
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    ds.SetProjection(srs.ExportToWkt())
    ds.GetRasterBand(1).WriteArray(grid.astype(np.float32))
    ds = None  # closing the dataset writes it to disk


def write_png(grid: np.ndarray, path: Path) -> None:
    """Smooth the grid, colour it and save it as a 400 x 400 picture."""
    scaled = cv2.normalize(grid.astype(np.float32), None, 0, 255, cv2.NORM_MINMAX)
    smooth = cv2.GaussianBlur(scaled.astype(np.uint8), (7, 7), 0)
    big = cv2.resize(smooth, (400, 400), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(str(path), cv2.applyColorMap(big, cv2.COLORMAP_VIRIDIS))


def main() -> None:
    gauges = pd.read_csv(DATA)
    print(f"{len(gauges)} gauges, flow {gauges.flow_m3s.min()} to {gauges.flow_m3s.max()} m3/s")

    slope, r2 = fit_flow(gauges)
    print(f"Flow rises {slope:.3f} m3/s per km2 of catchment (R squared {r2:.2f})")

    bounds = grid_bounds(gauges)
    grid = idw_grid(gauges, bounds)

    OUT.mkdir(exist_ok=True)
    tif, png = OUT / "flow.tif", OUT / "flow.png"
    write_geotiff(grid, bounds, tif)
    check = gdal.Open(str(tif))
    band = check.GetRasterBand(1).ReadAsArray()
    epsg = osr.SpatialReference(wkt=check.GetProjection()).GetAuthorityCode(None)
    print(f"Wrote {tif}: {check.RasterXSize} x {check.RasterYSize} cells, EPSG:{epsg}, "
          f"mean flow {band.mean():.1f} m3/s")

    write_png(grid, png)
    print(f"Wrote {png}")


if __name__ == "__main__":
    main()
