total = 0
with open('day1_data.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        total += int(line)
    print(total)
