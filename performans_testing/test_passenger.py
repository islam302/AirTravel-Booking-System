from locust import HttpUser, task, between
from random import randint


class TestPassenger(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_passenger_tickets(self):
        try:
            response = self.client.get('/Home/passengers/3/tickets/')
            if response.status_code != 200:
                print(f'Request failed with status code {response.status_code}')
        except Exception as e:
            print(f'An error occurred: {e}')





