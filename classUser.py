import configValues

class User:
    total_users = 0
    total_removed_users = 0

    def __init__(self, time, base_station=1):
        self.id = configValues.GLOBAL_ID
        configValues.GLOBAL_ID += 1
        self.time = time
        self.distance = configValues.DISTANCE_X
        self.ttt_counter = 0
        self.base_station = base_station
        self.switch_count = 0
        User.total_users += 1

    @staticmethod
    def get_total_users():
        return User.total_users

    @staticmethod
    def get_total_removed_users():
        return User.total_removed_users

    def get_switch_count(self):
        return self.switch_count

    def get_ttt_counter(self):
        return self.ttt_counter

    def increase_ttt_counter(self, value):
        self.ttt_counter += value

    def reset_ttt_counter(self):
        self.ttt_counter = 0

    def switch_to_B2(self):
        if self.base_station == 1:
            self.base_station = 2
            self.switch_count += 1

    def switch_to_B1(self):
        if self.base_station == 2:
            self.base_station = 1
            self.switch_count += 1

    def print_data(self):
        print(f"Id: {self.id}, time: {self.time}, distance: {self.distance}, base_station: {self.base_station}, ttt_counter: {self.ttt_counter}")
