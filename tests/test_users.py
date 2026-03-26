import requests
import pytest


def test_get_single_user(base_url):
    """
    Тест: получаем данные одного пользователя (ID=1) и проверяем ответ.
    Фикстура base_url приходит из conftest.py.
    """
    # Отправляем GET-запрос к API
    response = requests.get(f"{base_url}/users/1")

    # Проверка статус-кода
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

    # Получаем данные в виде словаря
    data = response.json()

    # Проверки содержимого
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]  # простая проверка формата email

    print("✅ Тест test_get_single_user пройден успешно!")


def test_get_all_users(base_url):
    """
    Тест: получаем список всех пользователей и проверяем, что их 10.
    Фикстура base_url приходит из conftest.py.
    """
    response = requests.get(f"{base_url}/users")

    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 10

    print("✅ Тест test_get_all_users пройден успешно!")


@pytest.mark.parametrize(
    "user_id, expected_name",
    [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch"),
    ],
)
def test_user_data(base_url, user_id, expected_name):
    """
    Параметризованный тест: получаем данные пользователя по ID
    и проверяем, что имя совпадает с ожидаемым.
    """
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == expected_name
    print(f"✅ Пользователь {user_id} – {expected_name}")


@pytest.mark.parametrize("user_id", range(1, 11))
def test_user_by_id(base_url, user_id):
    """
    Параметризованный тест для пользователей с ID от 1 до 10.
    Проверяем, что данные приходят и имеют правильную структуру.
    """
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "@" in data["email"]
    assert data["id"] == user_id

    print(f"✅ Пользователь {user_id} – {data['name']} ({data['email']})")
