file = open("5", "r")
seats = [line[:-1] for line in file.readlines()]
file.close()

def get_row(input):
    start = 0
    end = 127
    for letter in input[:-3]:
        if letter is "F":
            end = (start + end) // 2
        elif letter is "B":
            start = (start + end + 1) // 2
    return start

def get_col(input):
    start = 0
    end = 7
    for letter in input[-3:]:
        if letter is "L":
            end = (start + end) // 2
        elif letter is "R":
            start = (start + end + 1) // 2
    return start

IDs = []

for seat in seats:
    IDs.append(get_row(seat) * 8 + get_col(seat))

print(max(IDs))