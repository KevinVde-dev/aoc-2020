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
numbers = "0123456789"
colorlist = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valids = 0

for item in passports.values():
    for key in creds:
        if key not in item.keys():
            continue
    try:
        byr = int(item["byr"])
        iyr = int(item["iyr"])
        eyr = int(item["eyr"])
        hgt = item["hgt"]
        hcl = item["hcl"]
        ecl = item["ecl"]
        pid = item["pid"]
    except:
        continue
    if not (1920 <= byr <= 2002):
        continue
    if not (2010 <= iyr <= 2020):
        continue
    if not (2020 <= eyr <= 2030):
        continue
    if "in" is hgt[-2:]:
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            continue
    elif "cm" is hgt[-2:]:
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            continue
    try:
        int(hcl[1:], 16)
    except:
        continue
    if ecl not in colorlist:
        continue
    if not (len(pid) == 9):
        continue
    else:
        for i in pid:
            if i not in numbers:
                continue
    valids += 1
print(valids)