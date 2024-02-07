import pytest

import pandas as pd
import numpy as np

from index_analyze.buy_every import build_analyze_matrix
from index_analyze.main import Investor

def test_build_analyze_matrix_with_ones():
    start_date = '2001-01-01'
    end_date = '2015 -01-10'
    date_index = pd.date_range(start=start_date, end=end_date, freq='MS')
    source = pd.DataFrame(index=date_index, data={'value': 1.0})

    result_index = pd.date_range(start='2006-01-01', end=end_date, freq='MS')
    excepted = pd.DataFrame(index=result_index, data={'value': 1.0})
    result = build_analyze_matrix(source)
    assert result.equals(excepted)

def test_build_analyze_matrix_with_increase():
    start_date = '2001-01-01'
    end_date = '2015-01-10'
    date_index = pd.date_range(start=start_date, end=end_date, freq='MS')
    values = np.arange(1, len(date_index) + 1) * 1.0
    source = pd.DataFrame(index=date_index, data={'value': values})

    for start, end in [(f"20{i:02d}", f"20{i+5:02d}") for i in range(1, 10)]:
        for mon in [f"{i:02d}" for i in range(1, 13)]:
            investor = Investor("test")
            for date, row in source.loc[f"{start}-{mon}-01":f"{end}-{mon}-01"].iterrows():
                investor.buy(date, row['value'], 1.0)
            result = build_analyze_matrix(source)
            assert result.loc[f"{end}-{mon}-01"].value == pytest.approx(investor.total_precentage, 0.00001)


def test_build_analyze_matrix_with_percentage():
    start_date = '2001-01-01'
    end_date = '2015-01-10'
    date_index = pd.date_range(start=start_date, end=end_date, freq='MS')
    values = 1.0 + np.arange(len(date_index)) * 0.01
    source = pd.DataFrame(index=date_index, data={'value': values})

    for start, end in [(f"20{i:02d}", f"20{i+5:02d}") for i in range(1, 10)]:
        for mon in [f"{i:02d}" for i in range(1, 13)]:
            investor = Investor("test")
            for date, row in source.loc[f"{start}-{mon}-01":f"{end}-{mon}-01"].iterrows():
                investor.buy(date, row['value'], 1.0)
            result = build_analyze_matrix(source)
            assert result.loc[f"{end}-{mon}-01"].value == pytest.approx(investor.total_precentage, 0.00001)
