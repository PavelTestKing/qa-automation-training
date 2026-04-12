import csv
import pytest
import requests
import allure

def load_post_ids_from_csv(file_path):
    """Читает CSV и возвращает список post_id"""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [int(row['post_id']) for row in reader]

@allure.feature("Posts")
@allure.story("Get post from CSV")
@pytest.mark.parametrize("post_id", load_post_ids_from_csv("data/post_ids.csv"))
def test_get_post_csv(base_url, post_id):
    with allure.step(f"Send GET request to /posts/{post_id}"):
        response = requests.get(f"{base_url}/posts/{post_id}")
    with allure.step("Check status code 200"):
        assert response.status_code == 200
    with allure.step("Validate response"):
        data = response.json()
        assert data["id"] == post_id