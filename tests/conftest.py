import pytest

@pytest.fixture
def base_url():
    """Фикстура, возвращающая базовый URL тестового API"""
    return "https://jsonplaceholder.typicode.com"