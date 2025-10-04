import pytest

def fun():
  raise ValueError("Divided by zero")

def test_fun():
  with pytest.raises(ValueError) as ValueErr:
    fun()

  assert str(ValueErr.value) == "Divided by zero"

def test_a1():
  with pytest.raises(ZeroDivisionError) as ValueDivErr:
    1 / 0

  