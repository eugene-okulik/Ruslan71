import pytest

from test_api_bochin.endpoints.create_object import CreateObject
from test_api_bochin.endpoints.delete_object import DeleteObject
from test_api_bochin.endpoints.update_object import UpdateObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_object_id(create_object_endpoint, delete_object_endpoint):
    payload = {"name": "Мой объект", "data": {"key": "value"}}
    create_object_endpoint.create_new_object(payload)
    object_id = create_object_endpoint.object_id

    yield object_id

    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_status_200()
