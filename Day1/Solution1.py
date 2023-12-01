from __future__ import annotations

def Solution() -> int:
    with open("input.txt", "r") as f:
        lines = f.read()


        total = 0

        for line in lines.strip().split("\n"):
            value = 0

            line = ''.join([i for i in line if i.isnumeric()])
    
            value = int(line[0] + line[-1])

            total += value
        
        return total

print(Solution())
"""
53857
54636
"""