from locust import task, HttpUser


class ObjectUser(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            '/object',
            json={
                "name": "Locust object",
                "data": {"key": "value"}
            }
        )
        self.object_id = response.json()['id']

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{self.object_id}'
        )
