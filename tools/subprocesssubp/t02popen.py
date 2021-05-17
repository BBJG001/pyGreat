import subprocess

'''
poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。
wait(timeout): 等待子进程终止。
communicate(input,timeout): 和子进程交互，发送和读取数据。
send_signal(singnal): 发送信号到子进程 。
terminate(): 停止子进程,也就是发送SIGTERM信号到子进程。
kill(): 杀死子进程。发送 SIGKILL 信号到子进程。
'''

def test1():
    pass

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print("失败")



if __name__ == '__main__':
    test1()
    cmd('python --version')
    cmd('exit 1')