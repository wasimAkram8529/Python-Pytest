import pytest
from utils.util import get_data

@pytest.mark.parametrize("id,name,course,city", get_data())
def test_param_from_custome_file(id, name, course, city):
  print(city)