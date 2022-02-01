import pytest


def function_data():
    """Генерация кортежа с тестовыми данными"""
    return 1, 2, 3, 4


@pytest.mark.parametrize("test_data", function_data())
def test_ex(test_data):
    assert True
