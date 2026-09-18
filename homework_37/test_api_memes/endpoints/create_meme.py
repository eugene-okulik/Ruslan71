import allure
import requests

from .endpoints import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step("Create meme")
    def create_meme(self, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.post(
            "http://memesapi.course.qa-practice.com/meme",
            json=payload,
            headers=headers,
        )
        self.json = self.response.json()
        self.meme_id = self.json["id"]
        return self.response
