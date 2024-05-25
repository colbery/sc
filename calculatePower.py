import math

def calculate_power_B1(distance, generator):
    random_noise = generator()
    base_power = 4.56
    path_loss = 22 * math.log10(distance)
    received_power = base_power - path_loss + random_noise
    return received_power

def calculate_power_B2(distance, generator):
    random_noise = generator()
    base_power = 4.56
    path_loss = 22 * math.log10(distance)
    received_power = base_power - path_loss + random_noise
    return received_power
