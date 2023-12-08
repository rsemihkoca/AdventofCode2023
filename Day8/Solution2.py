from pprint import pprint

def cycle(iterable):
    while True:
        for item in iterable:
            yield item

with open("input.txt") as f:
    lines = f.read()


input  = lines.strip().split("\n")
map = input[2:]
directions = cycle([*input[0]])

val_dict = dict()

X_X_A = []

for val in map:
    val = val.split(" = ")
    left, right = val[1][1:4], val[1][6:9]

    if val[0][-1] == 'A':
        X_X_A.append(val[0])

    val_dict[val[0]] = {"L": left, "R": right}

# pprint(val_dict, sort_dicts=False)

result = []

def go_to_direction(direction, val):
    next_prov = val_dict[val][direction]
    return next_prov

for x in X_X_A:
    new_prov = x
    prev_res = 0
    directions = cycle([*input[0]])
    print(dir)

    while dir:=next(directions):


        prev_res += 1


        new_prov = go_to_direction(dir, new_prov)

        if new_prov[-1] == 'Z':
            print(x, new_prov, prev_res)
            break
    result.append(prev_res)


from math import gcd
lcm = 1
for i in result:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)