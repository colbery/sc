from classUser import User

class Queue2:
    def __init__(self):
        self.queue2 = []
        self.max_size = float("inf")
        self.id = 0

    def add_user(self, user):
        self.id += 1
        user.id = self.id
        self.queue2.append(user)

    def print_queue(self):
        for user in self.queue2:
            user.print_data()

    def user_count2(self):
        return len(self.queue2)
