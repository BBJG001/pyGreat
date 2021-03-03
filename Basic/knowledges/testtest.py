import pickle

class A:
    def __init__(self):
        self.a = 1
        self.b = 1
    def get_a(self):
        return self.a

xx = A()

with open('../data/testpickleobj.model', 'wb') as f:
    pickle.dump(xx, f)

with open('../data/testpickleobj.model', 'rb') as f:
    res = pickle.load(f)

print(type(res))
print(res.a)
print(res.get_a())