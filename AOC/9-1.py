def sum_of_prev_numbers(list, number):
    for i in list:
        for j in list:
            if i + j == number and i != j:
                return True
    return False

file = open("9", "r")
content = file.read()
file.close()

numbers = [int(i) for i in content.split("\n")]
p_len = 25
run = True
first_idx = 0

while run:
    preamble = numbers[first_idx: first_idx + p_len]
    number = numbers[first_idx + p_len]
    if sum_of_prev_numbers(preamble, number):
        first_idx += 1
    else:
        run = False

print(numbers[first_idx + p_len])