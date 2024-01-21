from locust import HttpUser, task, between
from random import randint

class TestPassenger(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_passenger_list(self):
        print('view passenger list')
        self.client.get('Home/passengers/',
                        name='Home/passengers')

    @task(4)
    def view_passenger_detail(self):
        print('view passenger detail')
        self.client.get('Home/passengers/1/',
                        name='Home/passengers/:id')

    @task(6)
    def create_passenger(self):
        print('create passenger')
        passenger_id = randint(2, 20)
        self.client.post('Home/passengers/',
                         name='Home/passengers/',
                         json={'passenger_id': passenger_id, 'quantity': 1})
