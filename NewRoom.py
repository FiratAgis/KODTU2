inp = input()
t = int(inp)
numberlist = []

for x in range(0, t):
    numberlist.append(int(input()))
for x in range(0, t):
    if(numberlist[x]<0):
        print "NO"
    elif((360 % (180 - numberlist[x])) == 0):
        print "YES"
    else:
        print "NO"
