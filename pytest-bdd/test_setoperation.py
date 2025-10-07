import pytest
from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path

fileName = "setOperation.feature"
parentFolder = "featureFiles"
Base_dir = Path(__file__).resolve().parent
filePath = Base_dir.joinpath(parentFolder).joinpath(fileName)

@pytest.fixture()
def setup_set():
  mySet = {'New delhi', 'Mumbai', 'Hyderabad'}
  return mySet

@scenario(filePath,'Add element in set')
def test_setOperation():
  pass


@given('a set of 3 cities', target_fixture='mySet')
def verify_set(setup_set):
  if(len(setup_set) == 0):
    pytest.xfail('Set length should not be zero')
  elif(len(setup_set) > 3):
    while(len(setup_set) > 3):
      setup_set.pop()

  return setup_set


@when('add 2 city in set')
def add_element_in_set(mySet):
  mySet.add('Patna')
  mySet.add('Lucknow')


@then('set contain 5 cities')
def check_set_length(mySet):
  assert len(mySet) == 5