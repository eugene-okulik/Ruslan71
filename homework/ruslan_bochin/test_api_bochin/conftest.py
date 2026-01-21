import pytest

from homework.ruslan_bochin.test_api_bochin.endpoints.create_post import CreatePost
from homework.ruslan_bochin.test_api_bochin.endpoints.update_post import UpdatePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def new_object_id(create_post_endpoint):
    """Создаёт объект перед тестом и удаляет после"""
    payload = {"name": "Мой объект", "data": {"key": "value"}}
    create_post_endpoint.create_new_object(payload)
    yield create_post_endpoint.object_id
    # удаляем объект после теста (если нужно)
    if create_post_endpoint.object_id:
        create_post_endpoint.response = None
