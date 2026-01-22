import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step("Check that object name is correct")
    def check_object_name(self, expected_name):
        assert self.json["name"] == expected_name

    @allure.step("Check that status is 200")
    def check_status_200(self):
        assert self.response.status_code == 200

    @allure.step("Check that status is 204")
    def check_that_status_is_204(self):
        assert self.response.status_code == 204

    @allure.step("Check that data field is not empty")
    def check_data_is_not_empty(self):
        assert self.json["data"]
