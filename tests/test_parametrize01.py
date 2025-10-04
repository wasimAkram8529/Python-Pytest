import pytest
import math

data = [
    ([1, 2, 3], "sum", 6),
    ([1, 2, 3], "prod", 6)
]

@pytest.mark.parametrize("x,y,result", [(1,2,3)])
def test_add(x,y,result):
    assert x+y == result


@pytest.mark.parametrize("list, action, result", data, ids=["sum", "prod"])
def test_custome_data(list, action, result):
    if(action == 'sum'):
        assert sum(list) == result

    elif(action == 'prod'):
        assert math.prod(list) == result