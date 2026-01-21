import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step("Check that object name is correct")
    def check_object_name(self, expected_name):
        assert self.json['name'] == expected_name

    @allure.step("Check that status is 200")
    def check_status_200(self):
        assert self.response.status_code == 200
