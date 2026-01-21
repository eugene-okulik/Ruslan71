import allure
import pytest


@allure.feature("Objects")
@allure.story("Get all objects")
@pytest.mark.smoke
def test_get_all_objects(create_post_endpoint):
    create_post_endpoint.create_new_object({"name": "temp", "data": {"k": "v"}})
    response = create_post_endpoint.response.json()
    assert len(response['data']) > 0


@allure.feature("Objects")
@allure.story("Get single object")
@pytest.mark.smoke
def test_get_object(new_object_id, create_post_endpoint):
    create_post_endpoint.create_new_object({"name": "temp2", "data": {"k": "v"}})
    response_json = create_post_endpoint.response.json()
    assert response_json['id'] == new_object_id


@allure.feature("Objects")
@allure.story("Create object")
@pytest.mark.regression
@pytest.mark.parametrize("payload", [
    {"name": "Объект 1", "data": {"color": "red"}},
    {"name": "Объект 2", "data": {"color": "blue"}},
    {"name": "Объект 3", "data": {"key": "value123"}}
])
def test_create_object(payload, create_post_endpoint):
    create_post_endpoint.create_new_object(payload)
    create_post_endpoint.check_status_200()
    create_post_endpoint.check_object_name(payload['name'])


@allure.feature("Objects")
@allure.story("Update object PUT")
@pytest.mark.regression
def test_update_object_put(new_object_id, update_post_endpoint):
    payload = {"name": "Обновлённый объект", "data": {"key": "новое значение"}}
    update_post_endpoint.update_put(new_object_id, payload)
    update_post_endpoint.check_status_200()
    update_post_endpoint.check_object_name(payload['name'])


@allure.feature("Objects")
@allure.story("Update object PATCH")
@pytest.mark.regression
def test_update_object_patch(new_object_id, update_post_endpoint):
    payload = {"data": {"key": "частичное обновление"}}
    update_post_endpoint.update_patch(new_object_id, payload)
    update_post_endpoint.check_status_200()
