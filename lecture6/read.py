with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"helow!! ", line.rstrip())