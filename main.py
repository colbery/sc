from generatorGaussian import RandomGaussianGenerator
from generatorUniform import RandomUniformGenerator
from generatorExponential import RandomExponentialGenerator
from calculatePower import calculate_power_B1, calculate_power_B2
from transferFromQueue import transfer_from_queue2_to_queue1
import configValues
from classUser import User
from classQueue1 import Queue
from classQueue2 import Queue2

# ---------------generatory------------------
generator1 = RandomGaussianGenerator(seed=configValues.SEEDS[0])
generator2 = RandomGaussianGenerator(seed=configValues.SEEDS[1])
generator3 = RandomExponentialGenerator(seed=configValues.SEEDS[2], scale=configValues.LAMBDA)
generator4 = RandomUniformGenerator(seed=configValues.SEEDS[3])

# --------------- Kolejki ------------------
queue1 = Queue()
queue2 = Queue2()
# --------------- Flagi ------------------
do_update = True
conditional_check = True
# --------------- Dodanie 1 osoby ------------------
time_z = configValues.GLOBAL_TIME + configValues.REPORT_INTERVAL
user = User(time_z)
#user.speed = 5  # gdy predkosc na sztywno
queue1.add_user(user)
print(f"User {user.id} added to queue. Time:", time_z)
random_wyk = generator3()
configValues.GLOBAL_TIME += random_wyk

def handle_user_exit(queue1, queue2, user):
    if User.get_total_removed_users() > configValues.INITIAL_PHASE:
        configValues.SWITCH_COUNT += user.switch_count
    queue1.remove_user(user)
    configValues.INITIALIZATION_COUNT += 1
    if len(queue2.queue2) > 0:
        transfer_from_queue2_to_queue1(queue2, queue1, configValues.GLOBAL_TIME)

def handle_user_disconnection(queue1, queue2, user):
    if User.get_total_removed_users() > configValues.INITIAL_PHASE:
        configValues.DISCONNECTIONS += 1
        configValues.SWITCH_COUNT += user.switch_count
    queue1.remove_user(user)
    if len(queue2.queue2) > 0:
        transfer_from_queue2_to_queue1(queue2, queue1, configValues.GLOBAL_TIME)

def handle_user_handover(user, Pb_B1, Pb_B2):
    def perform_handover_logic(new_base_station):
        if user.get_ttt_counter() == configValues.TTT:
            user.reset_ttt_counter()
            user.base_station = new_base_station
            user.switch_count += 1
            
            if User.get_total_removed_users() > 5:
                configValues.TOTAL_DISTANCE += user.distance
        else:
            user.increase_ttt_counter(1)

    def evaluate_handover(condition, new_base_station):
        if condition:
            perform_handover_logic(new_base_station)
        else:
            user.reset_ttt_counter()

    Pb_diff = abs(Pb_B2 - Pb_B1)

    if Pb_B2 > Pb_B1 and Pb_diff >= configValues.ALPHA:
        if user.base_station == 1:
            evaluate_handover(True, 2)
        else:
            evaluate_handover(False, None)
    elif Pb_B1 > Pb_B2 and Pb_diff >= configValues.ALPHA:
        if user.base_station == 2:
            evaluate_handover(True, 1)
        else:
            evaluate_handover(False, None)
    else:
        evaluate_handover(False, None)

def update_user_report(user, generator4):
    random_row = generator4()
    user.distance += 0.02 * random_row
    # gdy predkosc na sztywno user.distance += user.speed * (configValues.REPORT_INTERVAL / 1000.0)
    user.time += configValues.REPORT_INTERVAL
    return user

def process_user_exit(queue1, queue2, user):
    handle_user_exit(queue1, queue2, user)
    return True

def process_user_disconnection(queue1, queue2, user, Pb_B1, Pb_B2):
    if Pb_B1 - Pb_B2 <= configValues.DISCONNECT_THRESHOLD and user.base_station == 1:
        handle_user_disconnection(queue1, queue2, user)
        return True
    elif Pb_B2 - Pb_B1 <= configValues.DISCONNECT_THRESHOLD and user.base_station == 2:
        handle_user_disconnection(queue1, queue2, user)
        return True
    return False

def process_user_handover(user, Pb_B1, Pb_B2):
    handle_user_handover(user, Pb_B1, Pb_B2)
    return True

def add_user_to_system(queue1, queue2):
    time = configValues.GLOBAL_TIME + configValues.REPORT_INTERVAL
    user = User(time)
   # gdy predkosc na sztywno user.speed = 5  
    added = False
    if len(queue1.queue) < queue1.max_size:
        queue1.add_user(user)
        added = True
    elif len(queue2.queue2) < queue2.max_size:
        queue2.add_user(user)
        added = True

    if added:
        random_wyk = generator3()
        configValues.GLOBAL_TIME += random_wyk

# --------------- Pętla głowna ------------------
while True:
    # --------------- wyznaczanie czasu symulacji ------------------
    times = list(map(lambda user: user.time, queue1.queue))
    smallest_time_value = min(times)
    smallest_time_user = next(user for user in queue1.queue if user.time == smallest_time_value)

    do_update = configValues.GLOBAL_TIME != smallest_time_value
    czas_systemu = min(smallest_time_value, configValues.GLOBAL_TIME)

    # --------------- Zdarzenia czasowe - Raport użytkownika ------------------
    if czas_systemu == smallest_time_value:
        smallest_time_user = update_user_report(smallest_time_user, generator4)
        Pb_B1 = calculate_power_B1(smallest_time_user.distance, generator1)
        Pb_B2 = calculate_power_B2(configValues.B2_LOCATION - smallest_time_user.distance, generator2)
        conditional_check = False

    # --------------- Zdarzenia warunkowe - Użytkownik wyszedł z systemu ------------------
    if not conditional_check and smallest_time_user.distance >= configValues.END_OF_PATH:
        conditional_check = process_user_exit(queue1, queue2, smallest_time_user)

    # --------------- Zdarzenia warunkowe - Użytkownik stracił połączenie ------------------
    if not conditional_check:
        conditional_check = process_user_disconnection(queue1, queue2, smallest_time_user, Pb_B1, Pb_B2)

    # --------------- Zdarzenia warunkowe - Użytkownik przełącza się do stacji bazowej ------------------
    if not conditional_check:
        conditional_check = process_user_handover(smallest_time_user, Pb_B1, Pb_B2)

    # --------------- Zdarzenia czasowe - Dodanie użytkownika do systemu ------------------
    if czas_systemu == configValues.GLOBAL_TIME:
        add_user_to_system(queue1, queue2)

    # --------------- warunki zakończenia pętli ------------------
    if User.get_total_removed_users() > configValues.USER_LIMIT:
        break

    if do_update:
        czas_systemu = 0
    else:
        do_update = True

L_przelaczen = configValues.SWITCH_COUNT
sr_od_przelaczenia = configValues.TOTAL_DISTANCE / L_przelaczen
print("-------------------średnia odległość")
print(sr_od_przelaczenia)
print("-------------------rozłączenia")
print(configValues.DISCONNECTIONS)
l_usunietych = User.get_total_removed_users() - configValues.INITIAL_PHASE
print(f"liczba użytkowników po odjęciu początkowego {l_usunietych}")
srednia_roz = configValues.DISCONNECTIONS / l_usunietych
print("------------------- średnia rozłączeń")
print(srednia_roz)
print("------------------- stworzeni użytkownicy")
print(User.get_total_users())
print("------------------- przełączenia")
print(configValues.SWITCH_COUNT)
print("------------------- średnia przełączeń na użytkownika")
print(configValues.SWITCH_COUNT / l_usunietych)
print("------------------- usunięci z systemu")
print(User.get_total_removed_users())
print("-------------------")
print("kolejka_2")
