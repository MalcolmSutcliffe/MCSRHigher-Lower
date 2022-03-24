from functools import total_ordering


@total_ordering
class LeaderboardTime:
    __display_name = ""
    __minutes = 0
    __seconds = 0
    __milliseconds = 0

    # Assume time is of the form: MM:SS:MLS <-- milliseconds optional
    def __init__(self, input_value, input_format="MM:SS.MLS"):

        if input_format != "MM:SS.MLS":
            raise ValueError("unknown leaderboard time input format")

        split_value = input_value.split(":")
        self.__minutes = int(split_value[0])
        split_value2 = split_value[1].split(".")
        self.__seconds = int(split_value2[0])

        if len(split_value2) > 1:
            if len(split_value2[1]) == 1:
                self.__milliseconds = 100 * int(split_value2[1])
            elif len(split_value2[1]) == 2:
                self.__milliseconds = 10 * int(split_value2[1])
            elif len(split_value2[1]) == 3:
                self.__milliseconds = int(split_value2[1])

        self.generate_display_name()

    def generate_display_name(self):
        milli_string = str(self.__milliseconds)
        if 0 <= self.__milliseconds < 10:
            milli_string = "00" + milli_string
        if 10 <= self.__milliseconds < 100:
            milli_string = "0" + milli_string

        seconds_string = str(self.__seconds)
        if 1 <= self.__seconds < 10:
            seconds_string = "0" + seconds_string
        self.__display_name = str(self.__minutes) + ":" + seconds_string + "." + milli_string

    def __str__(self):
        return self.__display_name

    def __eq__(self, other):
        return self.__minutes == other.get_minutes() \
               and self.__seconds == other.get_seconds() \
               and self.__milliseconds == other.get_seconds

    def __gt__(self, other):
        return self.__milliseconds + 1000*self.__seconds + 60000*self.__minutes > \
               other.get_milliseconds() + 1000*other.get_seconds() + 60000*other.get_minutes()

    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds

    def get_milliseconds(self):
        return self.__milliseconds
