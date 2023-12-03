
import re
from pprint import pprint

total = 0


def check_and_get_number_in_indice(key, indice:int):

    for interval in number_indices[key]:
        if indice in range(interval[0], interval[1]):
            return int(s[key][interval[0]:interval[1]])


with open('input.txt') as f:


    star_indices = []

    s = f.read()

    s = s.strip().split('\n')
    number_indices = {}
    # pprint(s)
    for key, line in enumerate(s):

        if key == 0 or key ==(len(s) - 1):
            continue

        sequence = line
        # Define a regular expression pattern to match numbers
        pattern = r'\d+'

        # Find all matches in the sequence
        matches = re.finditer(pattern, sequence)

        # Get starting and ending indices for each match
        number_indices[key] = [(match.start(), match.end()) for match in matches]
        # find indices of *
        for i, char in enumerate(s[key]):
            if char == '*':
                star_indices.append((key, i))

    pprint(number_indices)
    for value_star in star_indices:

        list_of_numbers = set()
        key = value_star[0]
        indice = value_star[1]

        if key == 0 or key ==(len(s) - 1):
            continue

        prev_indice = indice - 1
        indice = indice
        next_indice = indice + 1

        prev_key = key - 1
        key = key
        next_key = key + 1

        possible_numbers = [
        (prev_key, prev_indice),
        (key, prev_indice),
        (next_key, prev_indice),
        (prev_key, indice),
        (key, indice),
        (next_key, indice),
        (prev_key, next_indice),
        (key, next_indice),
        (next_key, next_indice),]

        for x, y in possible_numbers:
            # print(x, y)
            # farklı koordinat aynı sayıya denk gelebilir
            number = check_and_get_number_in_indice(x, y)
            if number:
                # print(number)
                list_of_numbers.add(number)
        print(list_of_numbers)

        if len(list_of_numbers) == 2:
            total += list(list_of_numbers)[0] * list(list_of_numbers)[1]

    print("total", total)
"""
80936937
"""