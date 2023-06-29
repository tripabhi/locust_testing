from locust import FastHttpUser, task, between


class InferenceTestUser(FastHttpUser):
    wait = between(1, 3)

    @task
    def predict(self):
        self.client.post(
            "/predict",
            json={"queries": ["Hello, how are you doing today?"]},
        )
