import sys
with open('day1_data.txt', 'r') as f:
    data = f.read().splitlines()
    frequency = 0
    frequency_table = [0]

def go(data, frequency_table, frequency):
    for point in data:
        frequency += int(point)
        if frequency in frequency_table:
            print(frequency)
            sys.exit()
        frequency_table.append(frequency)
    go(data, frequency_table, frequency)


go(data, frequency_table, frequency)
