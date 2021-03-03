from string import ascii_letters

pl = list(range(10))
pl = [str(key) for key in pl]
pl = pl + list(ascii_letters)

print(pl)
print('aasdfb'[0:-1])
n = 0

psw = ''
for i in pl:
    psw = psw+i
    for j in pl:
        psw = psw + j
        for k in pl:
            psw = psw + k
            for l in pl:
                psw = psw + l
                for m in pl:
                    psw = psw + m
                    n+=1
                    if n%10000000 == 0:
                        print(psw)
                    psw = psw[0:-1]
                psw = psw[0:-1]
            psw = psw[0:-1]
        psw = psw[0:-1]
    psw = psw[0:-1]