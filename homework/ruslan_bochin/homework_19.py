import requests


def get_all_objects():
    print("GET all objects")
    response = requests.get("http://objapi.course.qa-practice.com/object")
    data = response.json()
    print(f"Объектов: {len(data['data'])}")
    assert len(data['data']) > 0, 'Not all posts returned'


def get_object():
    print("GET один объект")
    post_id = new_object()
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{post_id}").json()
    print(f"Объект {post_id}:", response['name'])
    assert response['id'] == post_id


def create_object():
    print("CREATE объект")
    body = {"name": "Мой объект", "data": {"key": "value"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    print("Создан:", response.json())
    assert response.status_code == 200, 'Status code is incorrect'


def new_object():
    body = {"name": "Мой объект", "data": {"key": "value"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object", json=body, headers=headers)
    return response.json()['id']


def clear(post_id):
    print(f"Очистка объекта {post_id}")
    requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


def update_object_put():
    print("PUT обновление")
    post_id = new_object()
    body = {"name": "Обновлённый объект", "data": {"key": "новое значение"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{post_id}", json=body, headers=headers).json()
    print("PUT результат:", response['name'])
    assert response['name'] == 'Обновлённый объект'
    clear(post_id)


def update_object_patch():
    print("PATCH обновление")
    post_id = new_object()
    body = {"data": {"key": "частичное обновление"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{post_id}", json=body,
                              headers=headers).json()
    print("PATCH результат:", response)
    clear(post_id)


def delete_object():
    print("DELETE")
    post_id = new_object()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")
    print("{}")
    print(response.status_code)


get_all_objects()
get_object()
create_object()
update_object_put()
update_object_patch()
delete_object()
