from locust import HttpUser, task

class TestUser(HttpUser):
    @task
    def get_test(self):
        self.client.get('/get')
