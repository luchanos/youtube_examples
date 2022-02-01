import pytest


@pytest.fixture(scope="function", autouse=True)
def my_fixture():
    print(1212121)
