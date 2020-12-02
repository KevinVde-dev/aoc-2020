file = open("1", "r")
content = file.read()
file.close()
letters = content.split("\n")
multiple = 0
for i in letters:
    for j in letters:
        for k in letters:
            if int(i) + int(j) + int(k) == 2020:
                multiple = int(i)*int(j)*int(k)
print(multiple)