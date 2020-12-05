import re

passports = []

file = 'd4_invalid.txt'
#file = 'd4_input.txt'

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

invalid = 0

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def sanity_checks(line):
    if byr(line) and iyr(line) and eyr(line):
        return True
    else:
        return False
  
def byr(line):
    spl_line = line.split()
    for item in spl_line:
        if 'byr' in item:
            year = re.search("byr:[1-2][0-9][0-9][0-9]", item)
            try:
                year = int(year.group()[4:])
            except:
                return False
            if year >= 1920 and year <= 2002:
                return True
            else:
                print(f"failed sanity check byr: {item}")
                return False

def iyr(line):
    spl_line = line.split()
    for item in spl_line:
        if 'iyr' in item:
            year = re.search("iyr:2[0-9][0-9][0-9]", item)
            try:
                year = int(year.group()[4:])
            except:
                return False
            if year >= 2010 and year <= 2020:
                return True
            else:
                print(f"failed sanity check iyr: {item}")
                return False

def eyr(line):
    spl_line = line.split()
    for item in spl_line:
        if 'eyr' in item:
            year = re.search("eyr:[2][0-9][0-9][0-9]", item)
            try:
                year = int(year.group()[4:])
            except:
                return False
            if year >= 2020 and year <= 2030:
                return True
            else:
                print(f"failed sanity check eyr: {item}")
                return False

for item in pass_clean:
    for field in fields:
        if field not in item:
            print(f"Missing {field} in   {item}")
            invalid += 1
            break
    if sanity_checks(item) == False:
        #print(f"Sanity check failed.  {item}")
        invalid += 1

print(f"invalid: {invalid}")
        

