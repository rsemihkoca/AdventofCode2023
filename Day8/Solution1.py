


from pprint import pprint

def cycle(iterable):
    while True:
        for item in iterable:
            yield item

with open("input.txt") as f:
    lines = f.read()


input  = lines.strip().split("\n")
directions = cycle([*input[0]])
map = input[2:]


val_dict = dict()

for val in map:
    val = val.split(" = ")
    left, right = val[1][1:4], val[1][6:9]
    val_dict[val[0]] = {"L": left, "R": right}

# pprint(val_dict, sort_dicts=False)

result = 0

def go_to_direction(direction, val):
    next_prov = val_dict[val][direction]
    return next_prov

new_prov = 'AAA'
while dir:=next(directions):
    print(dir, new_prov)

    new_prov = go_to_direction(dir, new_prov)
    result += 1

    if new_prov == 'ZZZ':
        break
print(result)
"""
new_prov = 'AAA'
yerine ilk satır TFZ'yi yazmışım
"""