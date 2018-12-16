with open('day5_data.txt', 'r') as f:
    data = f.read().splitlines()
new_list_letters = []
list_letters = [letter for letter in data[0]]

def remove_letters(list_letters):
    count = 0
    last_letter = 'a'
    for letter in list_letters:
        if letter.lower() == last_letter.lower():
            if ((letter.istitle() and (last_letter.istitle() == False)) or ((letter.istitle() == False) and last_letter.istitle())):
                list_letters.pop(count)
                list_letters.pop(count - 1)
                break
        last_letter = letter
        count += 1
    #keep_or_stop()

def keep_or_stop(list_letters):
    count = 0
    last_letter = 'a'
    for letter in list_letters:
        if letter.lower() == last_letter.lower():
            if ((letter.istitle() and (last_letter.istitle() == False)) or ((letter.istitle() == False) and last_letter.istitle())):
                count += 1
    index = 0
    while (count >= index):
        remove_letters(list_letters)
        index += 1
    return list_letters

def again(list_letters):
    for i in range(10000):
        g = keep_or_stop(list_letters)
        print(i)
        if i > 2500:
            print(g)
    return list_letters
g = again(list_letters)
print(g)
