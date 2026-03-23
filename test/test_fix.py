import pytest


@pytest.fixture()
def file_one():
    return 22


def test_file_one(file_one):
    assert file_one == 22
