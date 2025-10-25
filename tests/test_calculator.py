import pytest
from app.calculator import add, sub, mul, div

def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0

def test_sub():
  assert sub(4, 2) == 2
  assert sub(2, 4) == -2

def test_mul():
  assert mul(2, 2) == 4
  assert mul(3, 5) == 15


def test_div01():
  assert div(4, 2) == 2.0
  assert div(5, 2) == 2.5

def test_div02():
  with pytest.raises(ZeroDivisionError):
    div(2, 0)


# if __name__ == '__main__':
#     pytest.main()
