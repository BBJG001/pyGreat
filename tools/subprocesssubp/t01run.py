import subprocess



def test1():
    # 顺序执行
    # subprocess.run(['sh', 'overtimep.sh'])
    ret = subprocess.run(['echo', 'balabalabala'])
    print(ret.returncode)   # 0 success; 负值表明子进程被终止
    print(ret.check_returncode())

if __name__ == '__main__':
    test1()