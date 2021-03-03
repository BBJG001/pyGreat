# id()内存地址
a = 1000000000000000000000000000
a_ = a
b = 1000000000000000000000000000
c = a.copy()
print(id(a))
print(id(a_))
print(id(b))
print('a_==a:',a_==a)
print('b ==a:',b ==a)
print('a_ is a:',a_ is a)
print('b is a:',b is a)

la = [5,6]
la_ = la
lb = [5,6]

print(id(la))
print(id(la_))
print(id(lb))
print('la_==la:',la_==la)
print('lb ==la:',lb ==la)
print('la_ is la:',la_ is la)
print('lb is la:',lb is la)

print(2**64)