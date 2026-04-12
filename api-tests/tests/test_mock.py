import pytest
import requests
from pytest_mock import MockerFixture

def test_get_post_mock(mocker: MockerFixture):
    # 1. Создаём фальшивый ответ
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 99, "title": "Mocked title"}

    # 2. Подменяем requests.get
    mocker.patch("requests.get", return_value=mock_response)

    # 3. Вызываем requests.get (он вернёт подставленные данные)
    response = requests.get("https://any-url.com")
    
    # 4. Проверяем
    assert response.status_code == 200
    assert response.json()["title"] == "Mocked title"