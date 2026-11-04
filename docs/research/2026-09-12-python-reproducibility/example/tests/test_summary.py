import pytest

from bocrates import annual_average


def test_averages_within_a_year():
    got = annual_average([("2021-01-01", 1.0), ("2021-07-01", 2.0)])
    assert got == {2021: pytest.approx(1.5)}


def test_separates_years():
    got = annual_average([("2021-01-01", 1.0), ("2022-01-01", 3.0)])
    assert got == {2021: pytest.approx(1.0), 2022: pytest.approx(3.0)}


def test_empty_input_gives_empty_result():
    assert annual_average([]) == {}


@pytest.mark.parametrize("bad", ["21-01-01", "not-a-date"])
def test_rejects_non_iso_dates(bad):
    with pytest.raises(ValueError):
        annual_average([(bad, 1.0)])
