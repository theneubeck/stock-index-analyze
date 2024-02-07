import pytest

import pandas as pd
import numpy as np

from index_analyze.buy_every import calc_shares, mean_shares, build_analyze_matrix
from index_analyze.main import Investor

def test_build_analyze_matrix():
    start_date = '2001-01-01'
    end_date = '2015-01-10'
    date_index = pd.date_range(start=start_date, end=end_date, freq='MS')
    source = pd.DataFrame(index=date_index, data={'value': 1.0})

    result_index = pd.date_range(start='2006-01-01', end=end_date, freq='MS')
    excepted = pd.DataFrame(index=result_index, data={'value': 1.0})
    result = build_analyze_matrix(source)
    assert result.equals(excepted)

@pytest.mark.skip
def test_build_analyze_matrix():
    start_date = '2001-01-01'
    end_date = '2015-01-10'
    date_index = pd.date_range(start=start_date, end=end_date, freq='MS')
    values = np.arange(1, len(date_index) + 1) * 1.0
    source = pd.DataFrame(index=date_index, data={'value': values})

    result_index = pd.date_range(start='2006-01-01', end=end_date, freq='MS')
    excepted = pd.DataFrame(index=result_index, data={'value': 1.0})
    result = build_analyze_matrix(source)
    assert result.equals(excepted)
