from itertools import combinations_with_replacement


com=combinations_with_replacement(range(11), 5)
for c in com:
    print(c)

