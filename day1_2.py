f = open("day1_1.txt", "r")

expenses = []

for line in f:
    expenses.append(int(line))

for each in expenses:
    for item in expenses:
            for num in expenses:
                if num + each + item == 2020:
                    print(num, each, item, num * each * item)


