from LeaderboardTime import LeaderboardTime
import random

TIME_LIST = []

TIME_CUTOFF = LeaderboardTime("15:00:000")


def initialize_data():
    data1_16 = open("data/1.16RSG.csv")

    for line in data1_16:
        if line[0] == "#" or line[0] == ",":
            continue
        line_values = line.split(",")
        data_to_append = {
            "name": line_values[1],
            "time": LeaderboardTime(line_values[2]),
            "country": line_values[4]
        }
        if data_to_append["time"] > TIME_CUTOFF:
            break
        TIME_LIST.append(data_to_append)


def generate_new_order():
    new_list = TIME_LIST.copy()
    random.shuffle(new_list)
    return new_list
