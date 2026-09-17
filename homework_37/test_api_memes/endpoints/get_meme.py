import allure
import requests

from .endpoints import Endpoint


class GetMeme(Endpoint):

    @allure.step("Get all memes")
    def get_all_memes(self, headers=None):
        headers = headers or self.headers
        self.response = requests.get(
            "http://memesapi.course.qa-practice.com/meme",
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Get single meme by ID")
    def get_meme(self, meme_id, headers=None):
        headers = headers or self.headers
        self.response = requests.get(
            f"http://memesapi.course.qa-practice.com/meme/{meme_id}",
            headers=headers
        )
        # 404 может вернуть HTML — JSON парсим только при успешном ответе
        if self.response.ok and self.response.content:
            self.json = self.response.json()
        else:
            self.json = None
        return self.response
