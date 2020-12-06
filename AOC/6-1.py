file = open("6", "r")
content = file.read()
file.close()

answers = content.split("\n\n")
for i in range(len(answers)):
    answers[i] = answers[i].replace("\n", "")

def count_yes(answer):
    no_dupl = ""
    for l in answer:
        if l not in no_dupl:
            no_dupl += l
    return len(no_dupl)

s = 0
for answer in answers:
    s += count_yes(answer)

print(s)