f_name = "hightemp.txt"
line = 0

with open(f_name) as data:
    for i in data:
        line += 1
    print(line)