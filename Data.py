from LeaderboardTime import LeaderboardTime
import random
import gspread
import csv
from csv import reader

TIME_LIST = []

DEFAULT_TIME_CUTOFF = LeaderboardTime("15:00:000")

# List of all the possible Country values listed in the spreadsheet. Can be made dynamic, if needed
DEFAULT_COUNTRIES = frozenset(['Argentina', 'Australia', 'Belarus', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China',
                               'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hong Kong',
                               'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Lithuania', 'Mexico',
                               'Netherlands', 'Norway', 'Peru', 'Philippines', 'Poland', 'Russia', 'South Korea',
                               'Spain', 'Sweden', 'Taiwan', 'Turkey', 'Ukraine', 'United Kingdom', 'United States',
                               'Unspecified'])

DEFAULT_VERIFIED_ONLY = True


def verify_data():
    credentials = "credentials.json"
    sa = gspread.service_account(credentials)
    sh = sa.open("RSG 1.16+ Leaderboard")
    wks = sh.worksheet("1.16+ RSG")
    with open("website/data/Data_1_16", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(wks.get_all_values())


def initialize_data(time_cutoff=DEFAULT_TIME_CUTOFF, countries=DEFAULT_COUNTRIES, verified_only=DEFAULT_VERIFIED_ONLY):

    with open("website/data/Data_1_16", "r") as file:
        csv_reader = reader(file)
        data1_16 = list(csv_reader)

    for line in data1_16[2:]:
        if line[0] == ",":
            continue
        data_to_append = {
            "name": line[1],
            "time": LeaderboardTime(line[2]),
            "country": line[4]
        }
        if data_to_append["time"] > time_cutoff:
            break
        if verified_only and line[3] != "accepted":
            continue
        if data_to_append["country"] not in countries:
            continue
        TIME_LIST.append(data_to_append)


def generate_new_order():
    new_list = TIME_LIST.copy()
    random.shuffle(new_list)
    return new_list
