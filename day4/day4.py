import datetime

with open('day4_data.txt', 'r') as f:
    data = f.read().splitlines()


sorted_data =  sorted(data, key=lambda k: datetime.datetime(int(k[1:5]), int(k[6:8]), int(k[9:11]), int(k[12:14]), int(k[15:17])))
def make_chart():
    print("Date    ID      Minute\n                000000000011111111112222222222333333333344444444445555555555")
    print("                012345678901234567890123456789012345678901234567890123456789")
    single_entry(sorted_data)

def single_entry(sorted_data):
    time_dots = ['.' for i in range(60)]
    for time_point in sorted_data:
        temp_guard_number = time_point[25:29]
        description = time_point[19:]
        if time_point[25] == '#':
            guard_number = time_point[25:29]
            print(''.join(time_dots))
            time_dots = ['.' for i in range(60)]
            print("   " + guard_number, end="")
        else:
            if "falls" in description:
                sleep_time = time_point[15:17]
                time_dots[int(sleep_time) - 1] = "#"
            if "wakes" in description:
                awake_time = time_point[15:17]
                time_dots[int(awake_time) - 2] = "#"
                count = 0
                for dot in time_dots:
                    import pdb; pdb.set_trace()
                    #if dot == "#" and count != (int(awake_time) - 2):
                    while i   
                        time_dots[] = "#"
                    count+= 1


make_chart()
