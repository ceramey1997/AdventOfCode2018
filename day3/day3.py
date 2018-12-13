import numpy

with open('day3_data.txt', 'r') as f:
    data = f.read().splitlines()

spread_sheet = numpy.zeros((1000, 1000), int)

def list_of_parsed_claims(data):
    list_claims = []
    for claim in data:
        list_claims.append(parse_claim(claim))
    print(list_claims)

def parse_claim(claim):
    claim_number = claim[1:].split(" ", 1)
    in_from_left = claim_number[1][2:].split(',')
    in_from_right = in_from_left[1].split(':', 1)
    width = in_from_right[1].strip().split('x')
    height = width[1]
    return [claim_number[0], in_from_left[0], in_from_right[0], width[0], height]

def fill_sheet(parsed_claim):
    from_left = parsed_claim[1]
    from_top = parsed_claim[2]
    width = parsed_claim[3]
    height = parsed_claim[4]
    claim_number = parsed_claim[0]
    if spread_sheet[from_top][from_left] != 0:
        spread_sheet[from_top][from_left] = 'x'
        i = 0
        while i < width:

    else:
        spread_sheet[from_top][from_left] = claim_number
list_of_parsed_claims(data)
