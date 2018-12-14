import numpy

with open('day3_data.txt', 'r') as f:
    data = f.read().splitlines()

spread_sheet = numpy.zeros((1000, 1000))

def list_of_parsed_claims(data):
    list_claims = []
    for claim in data:
        list_claims.append(parse_claim(claim))
    return list_claims

def parse_claim(claim):
    claim_number = claim[1:].split(" ", 1)
    in_from_left = claim_number[1][2:].split(',')
    in_from_right = in_from_left[1].split(':', 1)
    width = in_from_right[1].strip().split('x')
    height = width[1]
    return [int(claim_number[0]), int(in_from_left[0]), int(in_from_right[0]), int(width[0]), int(height)]

def find_box(parsed_claim):
    from_left = parsed_claim[1]
    from_top = parsed_claim[2]
    width = parsed_claim[3]
    height = parsed_claim[4]
    claim_number = parsed_claim[0]
    from_left_indicator = from_left
    from_top_indicator = from_top
    while (from_left_indicator <= (from_left + width - 1)) and (from_top_indicator <= (from_top + height - 1)):
        if spread_sheet[from_top_indicator][from_left_indicator] != 0:
            spread_sheet[from_top_indicator][from_left_indicator] = 0.5
        else:
            spread_sheet[from_top_indicator][from_left_indicator] = claim_number
        if from_left_indicator == from_left + width - 1:
            from_left_indicator = from_left
            from_top_indicator += 1
        else:
            from_left_indicator += 1

def fill_box(parsed_claim_list):
    for claim in parsed_claim_list:
        find_box(claim)

def find_number_overlapping():
    count = 0
    for j in range(1000):
        for i in range(1000):
            if spread_sheet[i][j] == 0.5:
                count += 1
    return(count)


parsed_claims = list_of_parsed_claims(data)
fill_box(parsed_claims)
count = find_number_overlapping()    
print("This is how many squares overlap if all elves try and cut their own peice: " + str(count))
