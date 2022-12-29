import pytest
@pytest.fixture
def numbers():
    x,y,z= 10,20,30
    return[x,y,z]

def test_function(nums):
    a=10
    assert nums[1]==a