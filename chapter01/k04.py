s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word = s.split(' ')
num = {1, 5, 6, 7, 8, 9, 15, 16, 19}
element = {}

for i, word in enumerate(word):
    if i + 1 in num:
        element[i + 1] = word[0]
    else:
        element[i + 1] = word[:2]

print(element)