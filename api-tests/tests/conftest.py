import pytest

@pytest.fixture
def base_url():
    """Возвращает базовый URL для API"""
    return "https://jsonplaceholder.typicode.com"