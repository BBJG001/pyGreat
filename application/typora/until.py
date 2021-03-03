
def doUpper():
    res = ''
    file = '__init__.py'
    with open(file, 'r') as rf:
        while True:
            line=rf.readline()
            if not line:
                break
            linelist = line.split('=')
            newline = '{}={}'.format(linelist[0].upper(), linelist[1])
            res+=newline
    with open(file, 'w') as wf:
        wf.write(res)

if __name__ == '__main__':
    doUpper()