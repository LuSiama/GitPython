import pytest

@pytest.fixture()
def file_one():
    return 22

def test_file_one(file_one):
    assert file_one == 22

def my_function(a, b):
    return a + b

print(my_function(1, 2))

def test_my_function():
    assert my_function(1, 2) == 3
