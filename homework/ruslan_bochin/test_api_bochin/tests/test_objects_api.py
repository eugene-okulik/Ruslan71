import allure
import pytest


@allure.feature("Objects")
@allure.story("Get all objects")
@pytest.mark.smoke
def test_get_all_objects(create_object_endpoint):
    create_object_endpoint.get_all_objects()
    create_object_endpoint.check_status_200()
    create_object_endpoint.check_data_is_not_empty()


@allure.feature("Objects")
@allure.story("Get single object")
@pytest.mark.smoke
def test_get_object(new_object_id, create_object_endpoint):
    create_object_endpoint.get_object(new_object_id)
    create_object_endpoint.check_status_200()
    create_object_endpoint.check_object_name("Мой объект")


@allure.feature("Objects")
@allure.story("Create object")
@pytest.mark.regression
@pytest.mark.parametrize("payload", [
    {"name": "Объект 1", "data": {"color": "red"}},
    {"name": "Объект 2", "data": {"color": "blue"}},
    {"name": "Объект 3", "data": {"key": "value123"}},
])
def test_create_object(payload, create_object_endpoint):
    create_object_endpoint.create_new_object(payload)
    create_object_endpoint.check_status_200()
    create_object_endpoint.check_object_name(payload["name"])


@allure.feature("Objects")
@allure.story("Update object PUT")
@pytest.mark.regression
def test_update_object_put(new_object_id, update_object_endpoint):
    payload = {"name": "Обновлённый объект", "data": {"key": "новое значение"}}
    update_object_endpoint.update_put(new_object_id, payload)
    update_object_endpoint.check_status_200()
    update_object_endpoint.check_object_name(payload["name"])


@allure.feature("Objects")
@allure.story("Update object PATCH")
@pytest.mark.regression
def test_update_object_patch(new_object_id, update_object_endpoint):
    payload = {"data": {"key": "частичное обновление"}}
    update_object_endpoint.update_patch(new_object_id, payload)
    update_object_endpoint.check_status_200()
