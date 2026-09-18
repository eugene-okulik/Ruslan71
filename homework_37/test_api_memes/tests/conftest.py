import pytest

from test_api_memes.endpoints.authorize import Authorize
from test_api_memes.endpoints.create_meme import CreateMeme
from test_api_memes.endpoints.delete_meme import DeleteMeme
from test_api_memes.endpoints.get_meme import GetMeme
from test_api_memes.endpoints.update_meme import UpdateMeme


@pytest.fixture(scope="session")
def auth_token():
    auth = Authorize()

    if auth.token and auth.check_token(auth.token):
        return auth.token

    token = auth.authorize(name="Ruslan")
    return token


@pytest.fixture()
def create_meme_endpoint(auth_token):
    return CreateMeme(auth_token)


@pytest.fixture()
def get_meme_endpoint(auth_token):
    return GetMeme(auth_token)


@pytest.fixture()
def update_meme_endpoint(auth_token):
    return UpdateMeme(auth_token)


@pytest.fixture()
def delete_meme_endpoint(auth_token):
    return DeleteMeme(auth_token)


@pytest.fixture()
def new_meme_id(create_meme_endpoint, delete_meme_endpoint):
    meme_url = (
        "https://yandex.ru/images/search?from=tabbar"
        "&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg"
        "&lr=10313&pos=27&rpt=simage&text=mems"
    )
    payload = {
        "text": "Мой первый мем",
        "url": meme_url,
        "tags": ["funny", "ruslan"],
        "info": {"author": "Ruslan"},
    }

    create_meme_endpoint.create_meme(payload)
    meme_id = create_meme_endpoint.meme_id

    yield meme_id

    delete_meme_endpoint.delete_meme(meme_id)
