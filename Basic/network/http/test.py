import hashlib

def testSha():
    code='54188'
    print(hashlib.sha256(code.encode()).hexdigest())

def test():
    testSha()

if __name__ == '__main__':
    test()