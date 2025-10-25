import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from pathlib import Path

fileName = "bankTransaction.feature"
parentFolder = "featureFiles"
Base_dir = Path(__file__).resolve().parent
filePath = Base_dir.joinpath(parentFolder).joinpath(fileName)

def pytest_configure():
  pytest.balance = 0


@scenario(filePath, 'Withdraw money')
def test_withdraw_money():
    pass

@given(parsers.parse('account balance is {balance:d} dollar'))
def set_account_balance(balance):
   pytest.balance = balance

@when(parsers.parse('withdraw {withdrawAmount:d} dollar'))
def withdraw_money(withdrawAmount):
   if(pytest.balance < withdrawAmount):
      pytest.xfail(reason='Insufficient account balance')
   else:
      pytest.balance = pytest.balance - withdrawAmount

@then(parsers.parse('account balance should be {currentBalance:d} dollar'))
def check_balance(currentBalance):
   assert pytest.balance == currentBalance