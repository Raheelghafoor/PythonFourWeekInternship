# locustfile_q10.py
from locust import HttpUser, task, between

class HelloUserQ10(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_hello_q10(self):
        self.client.get("/hello")
    