rom locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Wait between 7 and 15 seconds per request per user
    wait_time = between(7, 15)
