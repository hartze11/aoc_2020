f = open("day1_1.txt", "r")

expenses = []

for line in f:
    expenses.append(int(line))

for each in expenses:
    for item in expenses:
        if each + item == 2020:
            print(each, item, each * item)


