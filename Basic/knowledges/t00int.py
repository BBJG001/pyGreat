
# 进制转换
print(150)      # 十进制
print(0xaa)     # 十六进制
print(0b101)    # 二进制
print(0o77)     # 八进制

## 使用内置函数
print(bin(150))
print(oct(150))
print(hex(150))


def convert(var, scale):
    res = ''
    while var != 0:
        res += str(var%scale)
        var //= scale
    # return str(''.join(list(reversed(res))))
    return res[::-1]


if __name__ == '__main__':
    x = 50
    print(convert(x, 8))
    print(convert(x, 2))
    print(convert(x, 16))