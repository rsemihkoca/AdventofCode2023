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

    sorted_mapping = dict(sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True))


    total = 0

    for line in lines:

        print("LINE BEGINS: ", line, sep="")

        for key, value in sorted_mapping.items():
            line = line.replace(key, value)

        print("LINE REPLACED: ", line, sep="")
        
        line = ''.join([i for i in line if i.isdigit()])

        print("LINE PRODUCED: ", line, sep="")

        value = int(line[0] + line[-1])

        print("VALUE: ", value, sep="")

        print()

        total += value
    
    return total

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(Solution(lines))
    