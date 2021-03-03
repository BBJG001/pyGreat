# assert expression
# 等价于
# if not expression:
#     raise AssertionError


def f_base():
    x = "hello"
    # x = "goodbye"

    #if condition returns True, then nothing happens:
    assert x == "hello"
    #if condition returns False, AssertionError is raised:
    assert x == "goodbye"

if __name__ == '__main__':
    f_base()