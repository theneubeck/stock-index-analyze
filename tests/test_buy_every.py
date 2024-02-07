import pytest

import pandas as pd

from index_analyze.buy_every import calc_shares, mean_shares, build_analyze_matrix

def test_shares_matrix():
    data = [
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 4.0}
    ]

    source = pd.DataFrame(data=data).set_index("date")
    result = calc_shares(source)

    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 0.5, "c": 0.25}
    ]).set_index("date")

    assert result.shape == (2,3)
    assert result.equals(excepted)


def test_analyze_matrix_other_values():
    data = [
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 8.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 8.0}
    ]

    source = pd.DataFrame(data=data).set_index("date")
    result = calc_shares(source)
    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 0.5, "c": 0.125},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 0.5, "c": 0.125}
    ]).set_index("date")

    assert result.shape == (2,3)
    assert result.equals(excepted)


def test_mean_shares():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 0.5, "c": 0.25},
    ]).set_index("date")

    result = mean_shares(source, years=5, min_periods=2).dropna()
    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 0.75, "c": 0.625},
    ]).set_index("date")
    assert result.equals(excepted)

def test_mean_shares_multiple_spans():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")

    result = mean_shares(source, min_periods=2).dropna()
    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")
    assert result.equals(excepted)

def test_sum_shares_with_inbetweens_multiple_spans():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2007-03-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2012-02-28"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")

    result = mean_shares(source, min_periods=2).dropna()

    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2007-03-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2012-02-28"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")
    assert result.equals(excepted)

@pytest.mark.skip
def test_build_analyze_matrix():
    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2007-03-01"), "a": 2.0, "b": 4.0, "c": 4.0},
        {"date": pd.Timestamp("2010-01-01"), "a": 2.0, "b": 4.0, "c": 4.0},
        {"date": pd.Timestamp("2012-02-28"), "a": 2.0, "b": 4.0, "c": 4.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 2.0, "b": 4.0, "c": 4.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")

    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2007-03-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2012-02-28"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")

    result = build_analyze_matrix(source)
    assert result.equals(excepted)
