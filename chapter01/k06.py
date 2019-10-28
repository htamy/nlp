from k05 import n_gram
s1="paraparaparadise"
s2="paragraph"
n=2

b1=n_gram(s1, n)
b2=n_gram(s2, n)

X=set(b1)
Y=set(b2)

print(X)
print(Y)

print(X|Y)
print(X&Y)
print(X-Y)

print('se' in b1, 'se' in b2)