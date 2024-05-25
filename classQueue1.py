from classUser import User

class Queue:
    def __init__(self):
        self.queue = []
        self.max_size = 20
        self.id = 0

    def add_user(self, user):
        if len(self.queue) <= self.max_size:
            self.id += 1
            user.id = self.id
            self.queue.append(user)

    def remove_user(self, user):
        self.queue.remove(user)
        User.total_removed_users += 1

    def print_queue(self):
        for user in self.queue:
            user.print_data()

    def user_count(self):
        return len(self.queue)
