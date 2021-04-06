import sys

phonems = set()
with open(sys.argv[1], "r") as file_dict:
    for line in file_dict:
        line = line.strip()
        for p in line.split()[1:]:
            phonems.add(p)

phonems = sorted(list(phonems))
print(phonems)
