def find_set_from_point(list, point, number):
    tmp_numb = 0
    counter = -1
    while tmp_numb != number:
        counter += 1
        tmp_list = list[point:counter]
        tmp_numb = sum(tmp_list)
        if tmp_numb > number:
            return False
    return counter

file = open("9", "r")
content = file.read()
file.close()

numbers = [int(i) for i in content.split("\n")]

for i in range(len(numbers)):
    tmp = find_set_from_point(numbers, i, 69316178)
    if tmp:
        print(min(numbers[i:tmp]) + max(numbers[i:tmp]))
        break