import numpy as np
import pandas as pd

from index_analyze.index_stats import compare_matrix

def test_compare_matrix_equal():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "index": 2.0, "b": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "index": 2.0, "b": 2.0},
        {"date": pd.Timestamp("2015-01-01"), "index": 2.0, "b": 2.0},
    ]).set_index("date")
    index = source["index"]

    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "index": 1, "b": 1},
        {"date": pd.Timestamp("2015-01-01"), "index": 1, "b": 1},
    ]).set_index("date")

    result = compare_matrix(index, source)
    assert result.equals(excepted)

def test_compare_matrix_more_less():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "index": 2.0, "b": 2.0, "c": 2.0},
        {"date": pd.Timestamp("2010-01-01"), "index": 2.0, "b": 3.0, "c": 1.0},
        {"date": pd.Timestamp("2015-01-01"), "index": 2.0, "b": 2.0, "c": 2.0},
    ]).set_index("date")
    index = source["index"]

    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "index": 1, "b": 1, "c": 0},
        {"date": pd.Timestamp("2015-01-01"), "index": 1, "b": 0, "c": 1},
    ]).set_index("date")

    result = compare_matrix(index, source)
    assert result.equals(excepted)


def test_compare_matrix_with_nan():
    source = pd.DataFrame(data=[
        {"date": pd.Timestamp("2005-01-01"), "index": 2.0, "b": 2.0,    "c": np.NaN},
        {"date": pd.Timestamp("2010-01-01"), "index": 2.0, "b": 2.0,    "c": 1.0 },
        {"date": pd.Timestamp("2015-01-01"), "index": 2.0, "b": 1.0,    "c": 2.0 },
        {"date": pd.Timestamp("2020-01-01"), "index": 2.0, "b": np.NaN, "c": 2.0 },
    ]).set_index("date")
    index = source["index"]

    excepted = pd.DataFrame(data=[
        {"date": pd.Timestamp("2010-01-01"), "index": 1, "b": 1, "c": np.NaN},
        {"date": pd.Timestamp("2015-01-01"), "index": 1, "b": 0, "c": 1},
        {"date": pd.Timestamp("2020-01-01"), "index": 1, "b": np.NaN, "c": 1},
    ]).set_index("date")

    result = compare_matrix(index, source)
    assert result.equals(excepted)

