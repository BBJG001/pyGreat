import re

def cutSeq():
    with open('./mian.py') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = re.sub(r'^[\s\d][\d][\d]|^[\s\d][\d]|^[\s\d]', '', lines[i])
    with open('./mian.py', 'w') as f:
        f.write(''.join(lines))

if __name__ == '__main__':
    cutSeq()