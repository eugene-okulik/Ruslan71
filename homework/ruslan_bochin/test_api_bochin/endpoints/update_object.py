import allure
import requests

from test_api_bochin.endpoints.endpoints import Endpoint


class UpdateObject(Endpoint):

    @allure.step("Update object via PUT")
    def update_put(self, object_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.put(f"{self.url}/{object_id}", json=payload, headers=headers)
        self.json = self.response.json()
        return self.response

    @allure.step("Update object via PATCH")
    def update_patch(self, object_id, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.patch(f"{self.url}/{object_id}", json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
