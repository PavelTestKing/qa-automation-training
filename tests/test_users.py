import requests

def test_get_single_user(base_url):
    """
    Тест: Получаем данные одного пользователя (ID=1) и проверяем ответ
    Фикстура base_url приходит из conftest.py
    """
    
    # Отправляем GET-запрос к API
    response = requests.get(f"{base_url}/users/1")
    
    # Проверка 1: статус-код должен быть 200 (успех)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    
    # Получаем данные в виде словаря
    data = response.json()
    
    # Проверка 2: ID пользователя должен быть 1
    assert data["id"] == 1
    
    # Проверка 3: имя пользователя должно совпадать с ожидаемым
    assert data["name"] == "Leanne Graham"
    
    # Проверка 4: в email должен быть символ @ (это простая проверка формата)
    assert "@" in data["email"]
    
    print("✅ Тест test_get_single_user пройден успешно!")


def test_get_all_users(base_url):
    """
    Тест: Получаем список всех пользователей и проверяем, что их 10
    Фикстура base_url приходит из conftest.py
    """
    
    # Отправляем GET-запрос к API
    response = requests.get(f"{base_url}/users")
    
    # Проверка статус-кода
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    
    # Преобразуем ответ в список словарей
    users = response.json()
    
    # Проверка, что пришёл именно список
    assert isinstance(users, list)
    
    # Проверка, что в списке ровно 10 пользователей
    assert len(users) == 10
    
    print("✅ Тест test_get_all_users пройден успешно!")