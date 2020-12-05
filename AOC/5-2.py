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
    ID = get_row(seat) * 8 + get_col(seat)
    if ID not in IDs:
        IDs.append(ID)

av_IDs = [i for i in range(46, 916)]
IDs.sort()
your_seat = 0

for i in range(len(IDs)-1):
    test_ID = IDs[i] + IDs[i + 1]
    if test_ID % 2 == 0:
        your_seat = test_ID // 2
print(your_seat)

for i in IDs:
    av_IDs.remove(i)
your_seat = max(av_IDs)
print(your_seat)