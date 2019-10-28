import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
word = s.split(' ')
letter = []
swap = []
res = []

for i in range(len(word) - 1):
    if len(word[i]) <= 4:
        res.append(word[i])
    else:
        letter = list(word[i])
        swap = letter[1:len(letter) - 1]
        random.shuffle(swap)
        res.extend([letter[0], swap, letter[len(letter) - 1]])
        #res.append(letter)
print(res)