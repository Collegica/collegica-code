import numpy as np
import pandas as pd

from analyse import grid_bounds, idw_grid

GAUGES = pd.DataFrame(
    {"lon": [0.0, 1.0], "lat": [0.0, 1.0], "catchment_km2": [10, 20], "flow_m3s": [2.0, 4.0]}
)


def test_grid_stays_within_the_readings():
    grid = idw_grid(GAUGES, grid_bounds(GAUGES), size=10)
    assert grid.shape == (10, 10)
    assert 2.0 <= grid.min() and grid.max() <= 4.0


def test_grid_is_highest_near_the_higher_gauge():
    grid = idw_grid(GAUGES, grid_bounds(GAUGES), size=10)
    # Row 0 is the north edge, column -1 the east edge: nearest the (1, 1) gauge.
    assert np.isclose(grid[0, -1], grid.max())
