import allure
import requests

from .endpoints import Endpoint


class UpdateMeme(Endpoint):

    @allure.step("Update meme via PUT")
    def update_put(self, meme_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.put(
            f"http://memesapi.course.qa-practice.com/meme/{meme_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Update meme via PATCH")
    def update_patch(self, meme_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.patch(
            f"http://memesapi.course.qa-practice.com/meme/{meme_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
