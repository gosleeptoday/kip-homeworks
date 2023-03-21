x = open('chisla.txt', 'r')
ch = x.readlines()
res = 0
for i in range(len(ch)):
    res += int(ch[i])
    i += 1
x.close()
y = open('res.txt', 'a')
y.write(str(res))
y.close()