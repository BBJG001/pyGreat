# dir(obj)   # 返回obj的属性、方法列表

print(type(4.))
print(float(4))
print(dir(4))
# [... ,'__hash__', ...]
print(dir(int))
# [... ,'__hash__', ...]
print(dir('string'))
# [... ,'__hash__', ...]
print('x'.__hash__())
# -7586097397837927001
print((4,5).__hash__())
# 3713084879518070856

# 可哈希（hash），dir(obj)结果中有__hash__方法——不可变数据类型：int、str、bool、tuple
# 不可哈希（hash）——可变数据类型：list、dict、set