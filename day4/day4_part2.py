import six
import datetime

with open('day4_data.txt', 'r') as f:
    data = f.read().splitlines()


sorted_data =  sorted(data, key=lambda k: datetime.datetime(int(k[1:5]), int(k[6:8]), int(k[9:11]), int(k[12:14]), int(k[15:17])))

gaurd_dict = {}

gaurds = []

for time_point in sorted_data:
    description = time_point[19:]
    if time_point[25] != '#':
        gaurd_number = gaurds[len(gaurds) - 1]
    if time_point[25] == '#':
        gaurd_number = time_point.split(" ")[3]
        if gaurd_number not in gaurds:
            gaurd_dict[gaurd_number] = []
        gaurds.append(gaurd_number)
    elif "falls" in description:
        sleep_time = time_point[15:17]
        gaurd_dict[gaurd_number].append(int(sleep_time))
    elif "wakes" in description:
        awake_time = time_point[15:17]
        sleep_time = gaurd_dict[gaurd_number][len(gaurd_dict[gaurd_number]) - 1]
        for i in range((int(sleep_time) + 1), int(awake_time)):
                gaurd_dict[gaurd_number].append(i)

def get_list_len():
    longest = 0
    long_gaurd = None
    for gaurd in gaurd_dict:
        if len(gaurd_dict[gaurd]) > longest:
            longest = len(gaurd_dict[gaurd])
            long_gaurd = gaurd
    return long_gaurd 

def get_most_often_min(gaurd):
    mi = {}
    minutes = gaurd_dict[gaurd]
    for minute in minutes:
        if minute not in mi:
            mi[minute] = []
            mi[minute].append(1)
        elif minute in mi:
            mi[minute].append(1)
    longest = 0
    long_minute = None
    for minute in mi:
        if len(mi[minute]) > longest:
            longest = len(mi[minute])
            long_minute = minute
    return (gaurd, long_minute, longest)


def get_most_frequent_asleep():
    longest = 0
    longest_guard = None
    long_minute = None
    for gaurd in gaurd_dict:
        gaurd, longest_minute, frequency = get_most_often_min(gaurd)
        if frequency > longest:
            longest = frequency
            longest_guard = gaurd
            long_minute = longest_minute
    return longest_guard, long_minute, longest



answer = get_most_frequent_asleep()
print("gaurd: " + str(answer[0]) + "\nlonest minute: " + str(answer[1]) +  "\nfrequncy: " + str(answer[2]))
