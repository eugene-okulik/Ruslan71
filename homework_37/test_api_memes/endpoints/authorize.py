import allure
import requests


class Authorize:
    token = None

    @allure.step("Authorize user")
    def authorize(self, name):
        response = requests.post(
            "http://memesapi.course.qa-practice.com/authorize",
            json={"name": name},
            headers={"Content-Type": "application/json"}
        )
        self.token = response.json()["token"]
        return self.token

    @allure.step("Check if token")
    def check_token(self, token):
        response = requests.get(f"http://memesapi.course.qa-practice.com/authorize/{token}")
        return response.status_code == 200
