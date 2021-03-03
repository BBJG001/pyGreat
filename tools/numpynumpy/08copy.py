import numpy as np

a1 = np.array([1,2,3])
# [1 2 3]
b1 = np.array([1,2,3])
# [1 2 3]

a2 = a1
a3 = a2

print('a3 is a2:',a3 is a2)
print('a3 is a1:',a3 is a1)
print('b1 is a1:',b1 is a1)
# a3 is a2: True
# a3 is a1: True
# b1 is a1: False



print('id(a1)',id(a1))
print('id(a2)',id(a2))
print('id(a3)',id(a3))
print('id(b1)',id(b1))
# id(a1) 1942484624608
# id(a2) 1942484624608
# id(a3) 1942484624608
# id(b1) 1942485290080

a3[1] = 8
print('a3 is a1:',a3 is a1)
print('a1=', a1)
print('a2=', a2)
print('a3=', a3)
# a3 is a1: True
# a1= [1 8 3]
# a2= [1 8 3]
# a3= [1 8 3]

print()

ca = a1.copy()
print('id(ca)',id(ca))
print('ca is a1:',ca is a1)
# id(ca) 1942500165392
# ca is a1: False

print()

oa = a1[:]
print('id(oa)',id(oa))
print('oa is a1:',oa is a1)
# id(oa) 1942500165472
# oa is a1: False

la = np.array([x for x in a1])
print('id(la)',id(la))
print('la is a1:',la is a1)
# id(la) 1562574014384
# la is a1: False

