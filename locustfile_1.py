from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Wait between 7 and 15 seconds per request per user
    wait_time = between(7, 15)
        
    @task(1)
    def load_test(self):
        # Request / on your Host
        # self.client.get("/")
        self.client.get("/")