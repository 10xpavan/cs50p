names = []

with open("names.txt") as file:
    for lines in file:
        names.append(lines.rstrip())

for name in sorted(names, reverse=False):
    print(f"hello, {name}")