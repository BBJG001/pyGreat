import time

time.sleep(2)

with open('code7.txt', 'w') as f:
    print('code7 txt content', file=f)