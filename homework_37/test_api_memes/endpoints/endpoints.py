import allure
import requests


class Endpoint:
    response = None
    json = None
    headers = {"Content-Type": "application/json"}
    BASE_URL = "http://memesapi.course.qa-practice.com"
    TIMEOUT = 5

    def __init__(self, token):
        self.headers["Authorization"] = token

    def _set_json(self):
        self.json = self.response.json()

    @allure.step("Send GET request")
    def send_get(self, path: str, params: dict | None = None):
        self.response = requests.get(
            self.BASE_URL + path,
            headers=self.headers,
            params=params,
            timeout=self.TIMEOUT,
        )
        self._set_json()
        return self.response

    @allure.step("Send POST request")
    def send_post(self, path: str, json: dict | None = None):
        self.response = requests.post(
            self.BASE_URL + path,
            headers=self.headers,
            json=json,
            timeout=self.TIMEOUT,
        )
        self._set_json()
        return self.response

    @allure.step("Send PUT request")
    def send_put(self, path: str, json: dict | None = None):
        self.response = requests.put(
            self.BASE_URL + path,
            headers=self.headers,
            json=json,
            timeout=self.TIMEOUT,
        )
        self._set_json()
        return self.response

    @allure.step("Send DELETE request")
    def send_delete(self, path: str):
        self.response = requests.delete(
            self.BASE_URL + path,
            headers=self.headers,
            timeout=self.TIMEOUT,
        )
        self._set_json()
        return self.response

    @allure.step("Check status is 200")
    def check_status_200(self):
        assert self.response.status_code == 200

    @allure.step("Check data is not empty")
    def check_data_is_not_empty(self):
        assert self.json
        assert self.json["data"]
