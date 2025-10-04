# fixture provides reusable test data
# pass it as argument, which give a fresh copy each time

import pytest 

@pytest.fixture
def sample_list():
    return [1,2,3]

def test_list_append(sample_list):
    sample_list.append(4)
    assert sample_list == [1,2,3,4]
    
def test_list_append(sample_list):
    sample_list.remove(1)
    assert sample_list == [2,3]