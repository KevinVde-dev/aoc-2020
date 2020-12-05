file = open("4", "r")
content = file.read()
file.close()
contents = content.split("\n\n")

passports = {}
for i, p in enumerate(contents):
    line = p.replace("\n", " ")
    new = line.split(" ")
    passports[i] = {}
    for j in new:
        passport = j.split(":")
        passports[i][passport[0]] = passport[1]

creds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for item in passports.values():
    ok = True
    for key in creds:
        if key not in item.keys():
            ok = False
    if ok:
        valid += 1