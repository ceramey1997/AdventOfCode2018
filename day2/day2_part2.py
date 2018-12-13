import sys
with open('day2_data.txt', 'r') as f:
    data = f.read().splitlines()

def compare_two(id1, id2):
    index = 0
    new_id1 = []
    for letter in id1:
        if letter == id2[index]:
            new_id1.append(letter)
            if len(new_id1) == 25:
                print(''.join(new_id1))
                sys.exit()
        index += 1

last_id = []
for id_ in data:
    last_id.append(id_)
    if len(last_id) == 0:
        continue
    for id__ in last_id:
        if id__ == id_:
            continue
        compare_two(id_, id__)

