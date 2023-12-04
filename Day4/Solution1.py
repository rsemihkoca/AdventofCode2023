with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0

for line in lines:

    line = line.split(':')[1].strip()

    card = line.split('|')
    left = card[0].strip()
    right = card[1].strip()

    count = len((set(left.split()) & set(right.split())))

    total += 2**(count-1) if count > 0 else 0
        

print(total)