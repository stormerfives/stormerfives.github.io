rom locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Wait between 7 and 15 seconds per request per user
    wait_time = between(7, 15)

    def on_start(self):
        self.client.headers.update({'Authorization': 'Basic aWNzc3VwcG9ydDppY3M='})
        
    @task(1)
    def index_page(self):
        # Request / on your Host
        # self.client.get("/")
        self.client.get("/api/MobileCall?id=0x000000002AC9CDFF")
        self.client.get("/api/MobileUnitInService?id=0x000000002ACFB31E")