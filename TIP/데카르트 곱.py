from itertools import product

a=['123','abc','!@#']
s=list(product(*a))
print(s)
#[('1', 'a', '!'), ('1', 'a', '@'), ('1', 'a', '#'), ('1', 'b', '!'), ('1', 'b', '@'), ....

a=[(1,-1),(2,-2)]
s=list(map(sum,product(*a)))
print(s)
#[3, -1, 1, -3]
