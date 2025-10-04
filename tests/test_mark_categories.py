import pytest

@pytest.mark.str_concate
def test_concatenate_str():
  string_1 = "abcdefghi"
  string_2 = "jklmnopqrstuvwxyz"

  assert string_1 + string_2 == "abcdefghijklmnopqrstuvwxyz"

@pytest.mark.str_concate
def test_concate_str():
  str_1 = "12345"
  str_2 = "67890"

  assert str_1 + str_2 == "1234567890"

@pytest.mark.str_slice
def test_str_slice():
  str_1 = "abcdefghijklmnopqrstuvwxyz"

  assert str_1[:] == "abcdefghijklmnopqrstuvwxyz"
  assert str_1[1:] == "bcdefghijklmnopqrstuvwxyz"
  assert str_1[-2:] == "yz"