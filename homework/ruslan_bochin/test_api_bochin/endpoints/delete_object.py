import allure
import requests

from test_api_bochin.endpoints.endpoints import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object")
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f"{self.url}/{object_id}",
            headers=headers
        )
        return self.response
