import pytest

@pytest.fixture(params=[(3, 4), [6, 8]], ids=["Tuple", "List"])
def setup06(request):
   return request.param


def test_setup06(setup06):
   if(type(setup06) == list):
      assert setup06[0] == 6
   elif(type(setup06) == tuple):
      assert setup06[0] == 3