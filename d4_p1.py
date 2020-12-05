
passports = []

#file = 'd4_sample.txt'
file = 'd4_input.txt'

with open(file, 'r') as f:
    for line in f:
      line = line.strip()
      passports.append(line)

pass_clean = []
counter = 1
var = ''

# Make sure input file ends with a blank line!

for line in passports:
    if line != '':
        var = var + ' ' + line
    if line == '':
        counter += 1
        pass_clean.append(var)
        var = ''

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

total = 0
invalid = 0

for item in pass_clean:
    for field in fields:
        if field not in item:
            print(f'field {field} not found in item: {item}')
            invalid += 1
    total += 1


