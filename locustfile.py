from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def search(self):
        self.client.get("/arama?q=iPhone")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 5000