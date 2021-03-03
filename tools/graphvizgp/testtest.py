import os

# os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz\bin'
print(os.pathsep)
print(os.environ['PATH'])
print(len(os.environ['PATH'].split(';')))
print('raph' in os.environ['PATH'])
ll = os.environ['PATH'].split(';')
# for i in ll:
#     print(i)