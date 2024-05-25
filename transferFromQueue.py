def transfer_from_queue2_to_queue1(queue2, queue1, global_time):
    try:
        first_user = queue2.queue2.pop(0)
        first_user.time = global_time + 20
        queue1.add_user(first_user)
        # print("Osoba przeniesiona z kolejki 2 do kolejki 1")
    except IndexError:
        pass  # Kolejka 2 jest pusta, nic nie robimy
