with open('test.txt', 'r') as f:
    data = f.read().splitlines()
new_list_letters = []
list_letters = [letter for letter in data[0]]
def remove_letters():
    last_letter = 'a'
    last_letter_modified = False
    count = 0
    letter_count = len(list_letters) - 1
    for letter in list_letters:
        if letter.lower() == last_letter.lower():
            if ((letter.istitle() and (last_letter.istitle() == False)) or ((letter.istitle() == False) and last_letter.istitle())):
                list_letters.pop(count)
                list_letters.pop(count - 1)
                if len(list_letters) < count:
                    import pdb; pdb.set_trace()
                last_letter = list_letters[count + 1]
                letter_count -= 2
                last_letter_modified = True

        if count == 7 and letter_count == 13:
            import pdb; pdb.set_trace()
        if last_letter_modified == False:
            last_letter = list_letters[count - 1]
        print(count)
        print(letter_count)
        print(list_letters)
        print()
        if count == letter_count:
            print(list_letters)
            remove_letters()

        count += 1


def still_continue():
    leng = len(list_letters)
    count_ = 0
    for letter in list_letters:
        if letter.lower() == last_letter.lower():
            if ((letter.istitle() and (last_letter.istitle() == False)) or ((letter.istitle() == False) and last_letter.istitle())):
                remove_letters()
        if count_ == leng:
            print(list_letters)
            still_continue()
        count_ += 1
remove_letters()
