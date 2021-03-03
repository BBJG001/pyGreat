ll = [1,2,3,4]

for i in ll.__iter__():
    print(i)

print(ll.__iter__().__next__())