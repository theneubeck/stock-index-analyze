import pandas as pd

from index_analyze.rolling_investment import build_analyze_matrix, merge


def test_merge():
    a = pd.DataFrame(data=[{"a": 1}])
    b = pd.DataFrame(data=[{"b": 2}])
    assert merge([a, b]).equals(pd.DataFrame(data=[{"a": 1, "b": 2}]))


def test_merge_multiple():
    a = pd.DataFrame(data=[{"a": 1}])
    b = pd.DataFrame(data=[{"b": 2}])
    c = pd.DataFrame(data=[{"c": 3}])
    assert merge([a, b, c]).equals(pd.DataFrame(data=[{"a": 1, "b": 2, "c": 3}]))


def test_merge_with_index():
    a = pd.DataFrame(data=[{"i": 0, "a": 1}]).set_index("i")
    b = pd.DataFrame(data=[{"i": 1, "b": 2}]).set_index("i")
    c = pd.DataFrame(data=[{"i": 0, "c": 3}]).set_index("i")

    excepted = pd.DataFrame(data=[{"a": 1, "c": 3}, {"b": 2}], columns=["a", "b", "c"])
    assert merge([a, b, c]).equals(excepted)


def test_analyze_matrix():
    data = [
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 3.0}
    ]

    source = pd.DataFrame(data=data).set_index("date")
    result = build_analyze_matrix(source)

    assert result.shape == (1,3)
    assert result.loc[pd.Timestamp("2015-01-01")].loc["a"] == 1.0
    assert result.loc[pd.Timestamp("2015-01-01")].loc["b"] == 2.0
    assert result.loc[pd.Timestamp("2015-01-01")].loc["c"] == 3.0


def test_analyze_matrix_with_more_rows():
    data = [
        {"date": pd.Timestamp("2010-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2009-01-01"), "a": 1.0, "b": 1.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "a": 1.0, "b": 2.0, "c": 3.0},
        {"date": pd.Timestamp("2020-01-01"), "a": 1.0, "b": 2.0, "c": 3.0}

    ]

    source = pd.DataFrame(data=data).set_index("date")
    result = build_analyze_matrix(source)
    assert result.shape == (2,3)
    assert result.loc[pd.Timestamp("2020-01-01")].loc["a"] == 1.0
    assert result.loc[pd.Timestamp("2020-01-01")].loc["b"] == 1.0
    assert result.loc[pd.Timestamp("2020-01-01")].loc["c"] == 1.0
