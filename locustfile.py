from locust import FastHttpUser, task, between


class InferenceTestUser(FastHttpUser):
    wait = between(1, 3)

    @task
    def predict(self):
        self.client.post(
            "/predict",
            json={
                "queries": [
                    "Bloomberg has decided to publish a new report on the global economy."
                ]
            },
        )
