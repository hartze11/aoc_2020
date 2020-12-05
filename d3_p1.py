f = open("d3_input.txt", "r")
#f = open("d3_sample.txt", "r")

hill = []

for row in f:
    row = row.strip()
    hill.append(row)

hill_len = len(hill)
row_len = len(hill[0])

row_pos_step = 1
hits = 0

row_pos = row_pos_step

line_start = 1
line_step = 2

for line in hill[line_start::line_step]:

    #print(line)
    print(f'row pos: {row_pos}, line: {line_start}')

    if line[row_pos] == '#':
        print('hit')
        hits += 1
    
    row_pos = (row_pos + row_pos_step) % row_len
    line_start += line_start + line_step

print(f'Total hits: {hits}')