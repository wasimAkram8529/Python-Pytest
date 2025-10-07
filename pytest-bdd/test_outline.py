import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path

fileName = "outline.feature"
parentFolder = "featureFiles"
Base_dir = Path(__file__).resolve().parent
filePath = Base_dir.joinpath(parentFolder).joinpath(fileName)

@scenario(filePath, 'Scene Outline Test')
def test_scene_outline_test():
  pass

@given(parsers.parse('there are {start:d} cucumbers'), target_fixture='cucumbers')
def initial_cucumber(start):
  return {'cucumber':start}

@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def cucumber_after_deposit(deposit, cucumbers):
    cucumbers['cucumber'] = cucumbers['cucumber'] + deposit

@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def cucumber_after_withdraw(withdraw, cucumbers):
   cucumbers['cucumber'] = cucumbers['cucumber'] - withdraw

@then(parsers.parse('I should have {final:d} cucumbers'))
def cucumber_after_all_operation(final, cucumbers):
   assert cucumbers['cucumber'] == final