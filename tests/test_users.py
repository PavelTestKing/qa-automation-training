import requests

def test_get_single_user(base_url):
    """
    Тест: получаем данные одного пользователя (ID=1) и проверяем ответ.
    Фикстура base_url приходит из conftest.py.
    """
    # Отправляем GET-запрос к API
    response = requests.get(f"{base_url}/users/1")

    # Проверка статус-кода
    assert response.status_code == 200, (
        f"Ожидали 200, получили {response.status_code}"
    )

    # Получаем данные в виде словаря
    data = response.json()

    # Проверки содержимого
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]   # простая проверка формата email

    print("✅ Тест test_get_single_user пройден успешно!")


def test_get_all_users(base_url):
    """
    Тест: получаем список всех пользователей и проверяем, что их 10.
    Фикстура base_url приходит из conftest.py.
    """
    response = requests.get(f"{base_url}/users")

    assert response.status_code == 200, (
        f"Ожидали 200, получили {response.status_code}"
    )

    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 10

    print("✅ Тест test_get_all_users пройден успешно!")