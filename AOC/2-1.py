file = open("2", "r")
content = file.read()
file.close()
passwords = content.split("\n")
valid = 0

for i in passwords:
    password = i.split(" ")
    boundaries = password[0].split("-")
    n1 = int(boundaries[0])
    n2 = int(boundaries[1])
    letter = password[1][0]
    amount = 0

    for j in password[2]:
        if j == letter:
            amount += 1
    if n1 <= amount <= n2:
        valid += 1
print(valid)