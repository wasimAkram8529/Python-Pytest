import pytest
from utils.configFileParser import ConfigFileParser

def pytest_configure():
  pytest.weekends1 = ["mon", "tue", "wed"]
  pytest.weekends2 = ["fri", "sat", "sun"]

def pytest_addoption(parser):
   parser.addoption('--cmdOpt', default='qa.ini')

@pytest.fixture()
def read_configfile(pytestconfig):
   opt = pytestconfig.getoption('cmdOpt')
   opt = opt + '.ini'
   configFile = ConfigFileParser(opt)
   yield configFile
   print("\n Tear down of fixture read_configFile")


@pytest.fixture()
def setup03():
  wek1 = pytest.weekends1.copy()
  wek1.append("Thru")
  yield wek1
  print("\n Tear down of fixture setup03 \n")

@pytest.fixture(scope="module")
def setup04():
   wek2 = pytest.weekends2.copy()
   wek2.insert(0, 'Thru')
   yield wek2
   print("\n Tear down of fixture setup04 \n")


@pytest.fixture()
def setup05(request):
   weekends1 = getattr(request.module, "months")
   weekends2 = weekends1.copy()
   weekends2.append("April")
   yield weekends2

   print("\n Tear down of fixture setup05")
