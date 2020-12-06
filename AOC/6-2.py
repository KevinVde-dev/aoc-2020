file = open("6", "r")
content = file.read()
file.close()

answers = content.split("\n\n")
for i in range(len(answers)):
    answers[i] = answers[i].split("\n")

def count(word, char):
    count = 0
    for l in word:
        if l is char:
            count += 1
    return count

def count_all_answered_yes(group_answer):
    if type(group_answer) is str:
        return len(group_answer)
    elif type(group_answer) is list:
        no_dupl = ""
        long_a = ""
        length = len(group_answer)
        for a in group_answer:
            long_a += a
        for l in long_a:
            if count(long_a, l) == length and l not in no_dupl:
                no_dupl += l
        return len(no_dupl)

s = 0
for answer in answers:
    s += count_all_answered_yes(answer)
print(s)