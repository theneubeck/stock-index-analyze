import pytest
from index_analyze.rolling_investment import merge
import pandas as pd

def test_merge():
    a = pd.DataFrame(data=[{'a': 1}])
    b = pd.DataFrame(data=[{'b': 2}])
    assert merge([a,b]).equals(pd.DataFrame(data=[{'a': 1, 'b': 2}]))

def test_merge_multiple():
    a = pd.DataFrame(data=[{'a': 1}])
    b = pd.DataFrame(data=[{'b': 2}])
    c = pd.DataFrame(data=[{'c': 3}])
    assert merge([a,b,c]).equals(pd.DataFrame(data=[{'a': 1, 'b': 2, 'c': 3}]))

def test_merge_with_index():
    a = pd.DataFrame(data=[{'i': 0, 'a': 1}]).set_index('i')
    b = pd.DataFrame(data=[{'i': 1, 'b': 2}]).set_index('i')
    c = pd.DataFrame(data=[{'i': 0, 'c': 3}]).set_index('i')

    excepted = pd.DataFrame(data=[{'a': 1, 'c': 3}, {'b': 2}], columns=['a', 'b', 'c'])
    assert merge([a,b,c]).equals(excepted)
