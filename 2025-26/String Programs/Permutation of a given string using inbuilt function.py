import itertools

s = "Ayusman"
li = [''.join(p) for p in itertools.permutations(s)]
print(li)