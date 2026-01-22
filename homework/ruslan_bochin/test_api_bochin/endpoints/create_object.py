import allure
import requests

from test_api_bochin.endpoints.endpoints import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step("Create new object")
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json["id"]
        return self.response

    @allure.step("Get single object")
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f"{self.url}/{object_id}",
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Get all objects")
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
