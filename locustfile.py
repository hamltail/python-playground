from locust import HttpUser, task, between
import time

class TestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_test(self):
        print(f"[{time.strftime('%H:%M:%S')}] sending request...")
        self.client.get('/get')
