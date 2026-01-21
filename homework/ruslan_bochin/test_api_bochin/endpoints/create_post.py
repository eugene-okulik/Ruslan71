import allure
import requests

from homework.ruslan_bochin.test_api_bochin.endpoints.endpoints import Endpoint


class CreatePost(Endpoint):
    object_id = None

    @allure.step("Create new object")
    def create_new_object(self, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
