file = open("3", "r")
content = file.read()
file.close()
lines = content.split("\n")
matrix = []
treelist = []

for i in lines:
    matrix.append(i)

dx = [1, 3, 5, 7, 1] # Right value
dy = [1, 1, 1, 1, 2] # Down Value

for i in range(5):
    y = 0
    x = 0
    trees = 0
    while y < len(matrix):
        if matrix[y][x] == "#":
            trees += 1
        y += dy[i]
        x += dx[i]
        if x > len(matrix[0])-1:
            x = x - len(matrix[0])
    print(i+1, trees)
    treelist.append(trees)

number = 1
for i in treelist:
    number *= i
print(number)

