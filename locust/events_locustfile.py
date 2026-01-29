from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.user_id = "locust_user"

    @task
    def view_events(self):
        self.client.get(
            "/events",
            params={"user": self.user_id},
            name="/events"
        )
