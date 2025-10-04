import pytest

weekends1 = ["mon", "tue", "wed"]
weekends2 = ["fri", "sat", "sun"]

@pytest.fixture()
def setup01():
  wek1 = weekends1.copy()
  wek1.append("Thru")
  yield wek1
  print("\n Tear down of fixture setup01 \n")

@pytest.fixture()
def setup02():
   wek2 = weekends2.copy()
   wek2.insert(0, 'Thru')
   yield wek2
   print("\n Tear down of fixture setup02 \n")


def test_setup01(setup01):
   assert len(setup01) == 4
   assert setup01[-1] == "Thru"


def test_setup02(setup02):
   assert len(setup02) == 4
   assert setup02[0] == 'Thru'
