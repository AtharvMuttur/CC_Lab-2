from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.user = "locust_user"

    @task
    def view_my_events(self):
        self.client.get(
            "/my-events",
            params={"user": self.user},
            name="/my-events"
        )
