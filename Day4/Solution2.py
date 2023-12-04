with open('input.txt', 'r') as file:
    lines = file.readlines()

result = dict()
card_matches = dict()

for line in lines:

    id, line = line.split(':')
    id = int(id.split()[1].strip())

    card = line.split('|')
    left = card[0].strip()
    right = card[1].strip()

    count = len((set(left.split()) & set(right.split())))
    card_matches[id] = count
    result[id] = 1



for key,value in card_matches.items():

    add_count = result[key]
    def_key = key + 1
    
    while value > 0:
        result[def_key] += add_count
        value -= 1
        def_key += 1
    
    
print(sum(result.values()))