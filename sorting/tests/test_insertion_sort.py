from insertion_sort import insert, insertion_sort

import pytest

def insert_test_cases():
    return [
        (([1, 3, 2], 1), [1, 3, 2]),
        (([1, 3, 2], 2), [1, 2, 3])
    ]

@pytest.mark.parametrize('params,result', insert_test_cases())
def test_insert(params, result):
    assert insert(*params) == result

def insert_error_test_cases():
    return [
        (([1, 3, 2], 0), ValueError),
        (([1, 3, 2], 3), ValueError)
    ]

@pytest.mark.parametrize('params,exception', insert_error_test_cases())
def test_insert_error(params, exception):
    with pytest.raises(exception):
        A = insert(*params)

def test_insertion_sort():
    A = [5,4,2,3,1]
    assert insertion_sort(A) == [1,2,3,4,5]
