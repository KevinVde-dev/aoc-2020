file = open("3", "r")
content = file.read()
file.close()
lines = content.split("\n")
matrix = []
x = 0
y = 0
trees = 0

for i in lines:
    matrix.append(i)

while y != len(matrix):
    if matrix[y][x] == "#":
        trees += 1
    y += 1
    x += 3
    if x > len(matrix[0])-1:
        x = x - len(matrix[0])

print(trees)