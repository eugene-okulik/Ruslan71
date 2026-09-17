import allure
import requests

from .endpoints import Endpoint


class DeleteMeme(Endpoint):

    @allure.step("Delete meme")
    def delete_meme(self, meme_id, headers=None):
        headers = headers or self.headers
        self.response = requests.delete(
            f"http://memesapi.course.qa-practice.com/meme/{meme_id}",
            headers=headers
        )
        return self.response
