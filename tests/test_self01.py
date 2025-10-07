import pytest
import sys

@pytest.mark.skip(reason="Not ready yet")
def test_example():
    assert 1 == 2

@pytest.mark.skipif(sys.platform == 'win32', reason = "Skip this test on window os")
def test_skip_with_condition():
    assert 1 == 2


