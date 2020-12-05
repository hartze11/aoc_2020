"""
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
"""

import math
import sys

#code = "FBFBBFFRLR"
#code = "BFFFBBFRRR"
#code = "BBFFBBFRLL"
#code = "FFFBBBFRRR"

file = 'd5_input.txt'

passes = []

with open(file, 'r') as f:
    for line in f:
      line = line.strip()
      passes.append(line)

count = 0

max = 0

for code in passes:

    count += 1

    row = code[0:7]
    col = code[7::]

    pair = 0, 127


    def upper(pair):  # 82, 83
        if pair[0] + 1 == pair[1]:
            return (pair[1], pair[1])

        lower = pair[0] # 82
        upper = pair[1] # 83
        new_lower = round(((upper - lower) / 2) + lower) # 
        return (new_lower, upper)  # 40, 47

    def lower(pair):  # 32, 63 
        lower = pair[0] # 32
        upper = pair[1] # 63 
        new_upper = math.floor((upper - lower) / 2) + lower # 32 + 15
        return (lower, new_upper)  # 32, 47


    def seat_upper(pair):  # 4, 5
        lower = pair[0] # 4
        upper = pair[1] # 5
        new_lower = round( (upper - lower) / 2 + lower) # 
        return (new_lower, upper)  # 

    def seat_lower(pair):  # 32, 63 
        lower = pair[0] # 32
        upper = pair[1] # 63 
        new_upper = math.floor((upper - lower) / 2 + lower) # 32 + 15
        return (lower, new_upper)  # 32, 47

    for letter in row:
        #print(pair)

        if letter == 'F':
            pair = lower(pair)

        if letter == 'B':
            pair = upper(pair)

        #print(f"{letter} - lower: {pair[0]} upper: {pair[1]}  ")


    if pair[0] == pair[1]:
        row = pair[0]
    else: 
        print("Error calculating row.  quitting")
        sys.exit(1)


    #print("check seat pairs")
    pair = 0, 7

    for letter in col:

        #print(pair)

        if pair[0] == (pair[1] - 1):
            if letter == 'R':
                pair = (pair[1], pair[1])
                #print('breaking due to right seat match')
                break
            if letter == 'L':
                pair = (pair[0], pair[0])
                #print('breaking due to Left seat match')
                break

        if letter == 'R':
            pair = seat_upper(pair)

        if letter == 'L':
            pair = seat_lower(pair)

        #print(f"{letter} - lower: {pair[0]} upper: {pair[1]}  ")

    if pair[0] == pair[1]:
        seat = pair[0]
    else: 
        print("Error calculating row.  quitting")
        sys.exit(1)

    id = row * 8 + seat

    if id > max:
        max = id

    #print(f"row {row}, col {seat}, seat ID: {id}")
    print(f"{row}, {seat}, {id}")
    #print(f"max: {max}")