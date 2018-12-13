with open('day2_data.txt', 'r') as f:
    data = f.read().splitlines()
    id_with_2 = 0
    id_with_3 = 0
    for id_ in data:
        two_used = 0
        three_used = 0
        for letter in id_:
            count = id_.count(letter)
            if count == 2:
                if two_used!= 1:
                    id_with_2 += 1
                    two_used += 1
            elif count == 3:
                if three_used != 1:
                    id_with_3 += 1
                    three_used += 1

print(id_with_2 * id_with_3)
