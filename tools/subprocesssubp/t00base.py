import subprocess


def test1():
    subprocess.Popen(['sh', 'overtimep.sh'])  # 新开一个子进程，后续继续执行
    subprocess.run(['python', '--version'])

def testout():
    retp = subprocess.Popen(['sh', 'overtimep.sh'])  # 新开一个子进程，后续继续执行
    retr = subprocess.run(['python', '--version'])
    print(retp.returncode)  # None
    print(retr.returncode)  # 0

    obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    obj.stdin.write('print(1) \n'.encode())
    obj.stdin.write('print(2) \n'.encode())
    obj.stdin.write('print(3) \n'.encode())
    out, err = obj.communicate()

    print(out)
    pass

if __name__ == '__main__':
    testout()
    # test1()