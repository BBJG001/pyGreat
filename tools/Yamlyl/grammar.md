参考 https://blog.csdn.net/lmj19851117/article/details/78843486

## 语法

 1. 大小写敏感
 2. 使用缩进表示层级关系
 3. 缩进时不允许使用Tab，只允许使用空格
 4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可
 5. \# 表示注释，从它开始到行尾都被忽略
 
 ### yaml表示字典
 
 ```yaml
# 下面格式读到Python里会是个dict
name: 灰蓝
age: 0
job: Tester
```
load到Python中
```python
{'name': '灰蓝', 'age': 0, 'job': 'Tester'}
```

### yaml表示列表

```yaml
# 下面格式读到Python里会是个list
- 灰蓝
- 0
- Tester
```
load到Python中
```python
['灰蓝', 0, 'Tester']
```

### 复合结构
```yaml
grade:
  boy:
  - name: 二狗蛋
    age: 20
  - name: 王三
    age: 18
  girl:
  - name: 李红
    age: 18
```
load到python中
```python
{'grade': {'boy': [{'name': '二狗蛋', 'age': 20}, {'name': '王三', 'age': 18}], 'girl': [{'name': '李红', 'age': 18}]}}
```

### 基本类型

> 字符串
  整型
  浮点型
  布尔型
  null
  时间
  日期
>

```yaml
# 这个例子输出一个字典，其中value包括所有基本类型
str: "Hello World!"
int: 110
float: 3.141
boolean: true  # or false
None: null  # 也可以用 ~ 号来表示 null
time: 2016-09-22t11:43:30.20+08:00  # ISO8601，写法百度
date: 2016-09-22  # 同样ISO8601
```
load到python中
```python
{'str': 'Hello World!', 'int': 110, 'float': 3.141, 'boolean': True, 'None': None, 'time': datetime.datetime(2016, 9, 22, 3, 43, 30, 200000), 'date': datetime.date(2016, 9, 22)}
```

### 其他
- 如果字符串没有空格或特殊字符，不需要加引号，但如果其中有空格或特殊字符，则需要加引号了
  ```yaml
  str: 灰蓝
  str1: "Hello World"
  str2: "Hello\nWorld"
  ```
  这里要注意单引号和双引号的区别，单引号中的特殊字符转到Python会被转义，也就是到最后是原样输出了，双引号不会被Python转义，到最后是输出了特殊字符；
  
- 引用
  ```yaml
  name: &name 灰蓝  # 标记引用
  tester: *name     # 使用引用
  ```
  load到python中
  ```python
  {'name': '灰蓝', 'tester': '灰蓝'}
  ```
  
- 类型强转

  通过`!!type`实现
  ```yaml
  str: !!str 3.14
  int: !!int "123"
  ```
  load到python中
  ```python
  {'int': 123, 'str': '3.14'}
  ```
  
- 分段
  ```yaml
  ---
  name: James
  age: 20
  ---
  name: Lily
  age: 19
  ```
  load时该yaml文件将会被分割为多个流文件，需要用load_all()加载成生成器
  
 ## 构造器、解析器、表示器