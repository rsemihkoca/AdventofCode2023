
import re
from pprint import pprint

total = 0

list_of_numbers = []
with open('input.txt') as f:


    spec_char = ['-', '$', '&', '*', '=','@', '/', '#', '+',  '%']


    s = f.read()

    s = s.strip().split('\n')
    
    pprint(s)
    for key, line in enumerate(s):

        if key == 0 or key ==(len(s) - 1):
            continue

        sequence = line
        # Define a regular expression pattern to match numbers
        pattern = r'\d+'

        # Find all matches in the sequence
        matches = re.finditer(pattern, sequence)

        # Get starting and ending indices for each match
        indices = [(match.start(), match.end()) for match in matches]

        # Print the result
        print(indices)

        for indice in indices:
            char_set = []
            first_element = indice[0]
            second_element = indice[1]

            number = int(s[key][first_element:second_element])
            print(number)
            list_of_numbers.append(number)

            prev = [*s[key-1][first_element-1:second_element+1]]
            curr = [*s[key][first_element-1:second_element+1]]
            nexti = [*s[key+1][first_element-1:second_element+1]]

            char_set.extend(prev)
            char_set.extend(curr)
            char_set.extend(nexti)

            print("number", number)
            print(prev)
            print(curr)
            print(nexti)

            for i in set(char_set):
                if i in spec_char:
                    total += number
                    
print("total", total)
print("list_of_numbers", list_of_numbers)
pprint(s)

"""
522726 spec charda . unutmusum allah kahretmesin
"""