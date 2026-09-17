import allure
import pytest


@allure.feature("Memes")
@allure.story("Get all memes")
@pytest.mark.smoke
def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_status_200()
    get_meme_endpoint.check_data_is_not_empty()


@allure.feature("Memes")
@allure.story("Get single meme")
@pytest.mark.smoke
def test_get_single_meme(new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_200()
    assert int(get_meme_endpoint.json["id"]) == int(new_meme_id)


@allure.feature("Memes")
@allure.story("Create meme")
@pytest.mark.regression
def test_create_meme(create_meme_endpoint):
    text = "Мой первый мем"
    url = (
        "https://yandex.ru/images/search?from=tabbar"
        "&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg"
        "&lr=10313&pos=27&rpt=simage&text=mems"
    )
    tags = ["funny", "ruslan"]
    author = "Ruslan"

    payload = {
        "text": text,
        "url": url,
        "tags": tags,
        "info": {"author": author},
    }

    create_meme_endpoint.create_meme(payload)

    create_meme_endpoint.check_status_200()
    assert create_meme_endpoint.json["text"] == text
    assert create_meme_endpoint.json["url"] == url
    assert create_meme_endpoint.json["tags"] == tags
    assert create_meme_endpoint.json["info"]["author"] == author


@allure.feature("Memes")
@allure.story("Update meme")
@pytest.mark.regression
def test_update_meme(new_meme_id, update_meme_endpoint):
    url = (
        "https://yandex.ru/images/search?from=tabbar"
        "&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg"
        "&lr=10313&pos=27&rpt=simage&text=mems"
    )

    payload = {
        "id": new_meme_id,
        "text": "Обновлённый мем",
        "url": url,
        "tags": ["funny", "ruslan"],
        "info": {"author": "Ruslan"},
    }

    update_meme_endpoint.update_put(new_meme_id, payload)
    update_meme_endpoint.check_status_200()
    assert int(update_meme_endpoint.json["id"]) == int(payload["id"])
    assert update_meme_endpoint.json["text"] == payload["text"]
    assert update_meme_endpoint.json["url"] == payload["url"]
    assert update_meme_endpoint.json["tags"] == payload["tags"]
    assert update_meme_endpoint.json["info"]["author"] == payload["info"]["author"]


@allure.feature("Memes")
@allure.story("Delete meme")
@pytest.mark.extended
def test_delete_meme(new_meme_id, delete_meme_endpoint, get_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_status_200()
    get_meme_endpoint.get_meme(new_meme_id)
    assert get_meme_endpoint.response.status_code == 404
