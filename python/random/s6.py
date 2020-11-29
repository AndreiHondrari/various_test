import itertools as its

l1 = [
    (1, 22),
    (1, 33),
    (1, 44),
    (2, 22),
    (2, 33),
    (2, 77),
    (2, 99),
]

z1 = its.groupby(l1, key=lambda x: x[0])

print({i[0]: list(i[1]) for i in z1})
