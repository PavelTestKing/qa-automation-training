import allure
import pytest
import requests
from faker import Faker
from models.post import Post

@allure.feature("Posts")
@allure.story("Get post")
@pytest.mark.parametrize("post_id", [1, 2, 3])   # параметризация
def test_get_post(base_url, post_id):
    with allure.step(f"Send GET request to /posts/{post_id}"):
        response = requests.get(f"{base_url}/posts/{post_id}")
    with allure.step("Check status code 200"):
        assert response.status_code == 200
    with allure.step("Validate response with Pydantic model"):
        data = response.json()
        post = Post(**data)
    with allure.step("Check specific fields"):
        assert post.id == post_id
        assert post.userId is not None

@allure.feature("Posts")
@allure.story("Create post")
def test_create_post(base_url):
    fake = Faker()
    payload = {
        "title": fake.sentence(),
        "body": fake.paragraph(),
        "userId": fake.random_int(min=1, max=10)
    }
    with allure.step("Send POST request to /posts"):
        response = requests.post(f"{base_url}/posts", json=payload)
    with allure.step("Check status code 201"):
        assert response.status_code == 201
    with allure.step("Validate response"):
        data = response.json()
        assert "id" in data
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]