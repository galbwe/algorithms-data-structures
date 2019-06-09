import pytest

from selection_sort import selection_sort

def selection_sort_test_params():
    return [
        ([], []),
        ([1], [1]),
        ([3,2,1], [1,2,3]),
        ([1,2,3], [1,2,3]),
        ([2,4,3,1], [1,2,3,4]),
        (['c', 'b', 'a'], ['a', 'b', 'c'])
    ]

@pytest.mark.parametrize('A,result', selection_sort_test_params())
def test_selection_sort(A, result):
    assert selection_sort(A) == result
