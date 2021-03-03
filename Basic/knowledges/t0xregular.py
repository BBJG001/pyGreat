import re

# 规则
# []    表示一个位置，[123]表示这一个位置或1或2或3
# [0123456789]  [0-9]   [a-z] [0-9a-fA-F]   必须是-前大，-后小
#----------- 元字符：就是在正则表达式中有特殊的意义
# . 	匹配除换行符以外的任意字符
# \w	匹配字母或数字或下划线
# \s	匹配任意的空白符
# \d	匹配数字
# \n	匹配一个换行符
# \t	匹配一个制表符
# \b	匹配一个单词的结尾
# ^	    匹配字符串的开始
# $	    匹配字符串的结尾
# \W    匹配非字母或数字或下划线
# \D    匹配非数字
# \S    匹配非空白符
# a|b   匹配字符a或字符b
# ()    匹配括号内的表达式，也表示一个组
# [...] 匹配字符组中的字符
# [^...]匹配除了字符组中字符的所有字符
#------------------ 重复匹配
# *? 重复任意次，但尽可能少重复
# +? 重复1次或更多次，但尽可能少重复
# ?? 重复0次或1次，但尽可能少重复
# {n,m}? 重复n到m次，但尽可能少重复
# {n,}? 重复n次以上，但尽可能少重复
#----------------- .*?
# 只对前面紧跟的一个字符起作用
# . 是任意字符
# * 是取 0 至 无限长度（贪婪匹配，尽可能多的匹配）
# ? 是非贪婪模式（尽可能短的匹配）
# 合在一起就是 取尽量少的任意字符，一般不会这么单独写，他大多用在：
# .*?x  就是取前面任意长度的字符，直到一个x出现

# re.search()   # 只匹配第1个符合的
# re.findall()  # 找到所有匹配结果
# re.match()

# 直接匹配


#----------------- 直接匹配
pattern1 = "cat"    # 匹配其中的cat
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))
# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(pattern1, string).group())
# cat
print(re.search(pattern2, string))
# None

#------------------ 拼接匹配
ptn3 = r"r[au]n"  # 匹配 ("run" or "ran")
ptn4 = r'r[a-c]n'   # 匹配ran、rbn、rcn
print(re.search(ptn3, "dog runs to cat"))
# <_sre.SRE_Match object; span=(4, 7), match='run'>
print(re.search(ptn4, "dog runs to cat"))
# None

#------------------- 元字符
print(re.search(r"r\dn", "run r4n"))    # \d匹配一位数字
# <_sre.SRE_Match object; span=(4, 7), match='r4n'>
print(re.search(r"r\Dn", "run r4n"))    # \D匹配一位非数字
# <_sre.SRE_Match object; span=(0, 3), match='run'>

#------------------- 多行匹配
string = '''
dog runs to cat.
I run to dog.
'''
print(re.search(r"^I", string))
# None
print(re.search(r"^I", string, flags=re.M))     # 通过指定flags属性为re.M可以在多行进行匹配
# <_sre.SRE_Match object; span=(18, 19), match='I'>

#-------------------- 重复匹配
# * : 重复零次或多次
# + : 重复一次或多次
# {n, m} : 重复 n 至 m 次
# {n} : 重复 n 次

# *：匹配0次或多次，尽可能多的匹配
print(re.search(r"ab*", "a"))   # 允许0个b
# <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.search(r"ab*", "abbbbb"))      # *对b起作用，即0或多个b，尽可能多的匹配
# <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# + : 匹配1次或多次，尽可能多匹配
print(re.search(r"ab+", "a"))   # 要求至少有1个b
# None
print(re.search(r"ab+", "abbbbb"))
# <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# {n, m} : 匹配n-m次，尽可能多匹配
print(re.search(r"ab{2,10}", "a"))
# None
print(re.search(r"ab{2,10}", "abbbbbabb"))
# <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

#------------------- 分组匹配
# 通过在小括号()中一部分匹配规则，这样可以在匹配结果中通过索引单独提取这部分结果
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())    # 获取整个匹配结果
# 021523, Date: Feb/12/2017
print(match.group(1))   # 提取索引1的结果（第1个括号），索引从1开始
# 021523
print(match.group(2))   # 提取索引2的结果（第2个括号）
# Date: Feb/12/2017

# 通过?P<名称>可以为匹配结果指定key/名称/属性索引，可以在结果中通过这么名称访问分组匹配结果
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))
# 021523
print(match.group('date'))
# Date: Feb/12/2017

#-------------------- re.findall()
# findall()
print(re.findall(r"r[ua]n", "run ran ren"))
# ['run', 'ran']

# | : or
print(re.findall(r"(run|ran)", "run ran ren"))
# ['run', 'ran']

#---------------------- re.sub()
# re.sub(a,b,string)    # a为正则式，b为替换值，匹配string中的所有a替换成b
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))
# dog catches to cat

#---------------------- re.split()
print(re.split(r'[,;\.]', 'a;b,c.d;e'))     # 按匹配到的字符进行分割
# ['a', 'b', 'c', 'd', 'e']

#---------------------- re.compile()
compiled_re = re.compile(r"r[ua]n")     # 把正则规则封装进一个正则对象
print(compiled_re.search("dog ran to cat")) # 在字符串上应用正则对象
# <_sre.SRE_Match object; span=(4, 7), match='ran'>