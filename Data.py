from LeaderboardTime import LeaderboardTime
import random
import gspread

sa = gspread.service_account("credentials.json")
sh = sa.open("RSG 1.16+ Leaderboard")
wks = sh.worksheet("1.16+ RSG")

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


def initialize_data(time_cutoff=DEFAULT_TIME_CUTOFF, countries=DEFAULT_COUNTRIES, verified_only=DEFAULT_VERIFIED_ONLY):

    data1_16 = wks.get()

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
