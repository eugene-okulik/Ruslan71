import pytest
import requests


@pytest.fixture()
def new_object_id():
    body = {"name": "Мой объект", "data": {"key": "value"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    print(object_id)
    yield object_id
    print('deleting the object')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session')
def start_scope():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def test_scope():
    print('before test')
    yield
    print('after test')


@pytest.mark.smoke
@pytest.mark.critical
def test_get_all_objects(start_scope, test_scope):
    print('GET all objects')
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    print(f"Объектов: {len(response['data'])}")
    assert len(response['data']) > 0, 'Not all posts returned'


@pytest.mark.smoke
def test_get_object(new_object_id, start_scope, test_scope):
    print('GET один объект')
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    print(f"Объект {new_object_id}:", response['name'])
    assert response['id'] == new_object_id


@pytest.mark.regression
@pytest.mark.parametrize('create_data', [
    ({"name": "Объект 1", "data": {"color": "red", "size": "big"}},),
    ({"name": "Объект 2", "data": {"color": "blue", "size": "small"}},),
    ({"name": "Объект 3", "data": {"key": "value123"}},)
])
def test_create_object(create_data, start_scope, test_scope):
    print('CREATE объект')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=create_data[0],
        headers=headers
    )
    created_object = response.json()
    print("Создан:", created_object)
    assert response.status_code == 200, 'Status code is incorrect'
    assert created_object['name'] == create_data[0]['name']


@pytest.mark.regression
@pytest.mark.medium
def test_update_object_put(new_object_id, start_scope, test_scope):
    print('PUT обновление')
    body = {"name": "Обновлённый объект", "data": {"key": "новое значение"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()
    print("PUT результат:", response['name'])
    assert response['name'] == 'Обновлённый объект'


@pytest.mark.regression
def test_update_object_patch(new_object_id, start_scope, test_scope):
    print('PATCH обновление')
    body = {"data": {"key": "частичное обновление"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    ).json()
    print("PATCH результат:", response)
    assert 'частичное обновление' in str(response['data'])


@pytest.mark.regression
def test_delete_object(new_object_id, start_scope, test_scope):
    print('DELETE')
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    print(response.status_code)
