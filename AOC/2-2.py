file = open("2", "r")
content = file.read()
file.close()
passwords = content.split("\n")
valid = 0

for i in passwords:
    password = i.split(" ")
    indexes = password[0].split("-")
    i1 = int(indexes[0])
    i2 = int(indexes[1])
    letter = password[1][0]
    password = password[2]

    if password[i1-1] == letter or password[i2-1] == letter:
        if password[i1-1] == letter and password[i2-1] == letter:
            pass
        else:
            valid += 1

print(valid)