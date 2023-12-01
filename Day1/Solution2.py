from __future__ import annotations

def Solution(lines: list[str]) -> int:
    mapping = {

        "zero" : "zero0zero",
        "one" : "one1one",
        "two" : "two2two",
        "three" : "three3three",
        "four" : "four4four",
        "five" : "five5five",
        "six" : "six6six",
        "seven" : "seven7seven",
        "eight" : "eight8eight",
        "nine" : "nine9nine",
  
    }

    total = 0

    for line in lines:


        for key, value in mapping.items():
            line = line.replace(key, value)
        
        line = ''.join([i for i in line if i.isdigit()])

        value = int(line[0] + line[-1])

        total += value
    
    return total

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(Solution(lines))
    