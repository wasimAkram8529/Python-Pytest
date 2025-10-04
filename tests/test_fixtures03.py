import pytest

months = ["Jan", "Feb", "March"]

def test_setup03(setup03):
   assert len(setup03) == 4
   assert setup03[-1] == "Thru"
   
   setup03.pop()

   assert setup03 == pytest.weekends1


def test_setup04(setup04):
   assert len(setup04) == 4
   assert setup04[0] == 'Thru'

def test_setup05(setup05):
   assert len(setup05) == 4
