maxp = []

def GenerateMax(d,dp,c,cp,i,n):
    global maxp
    if(i >= n):
        return 0
    elif(maxp[i] > -1):
        return maxp[i]
    
    max_num = 0
    if(i+dp[i]+1 >= n):
        max_num = d[i]
    else:
        for x in range(i+dp[i]+1,i+dp[i]+cp[i]+1):
            a = d[i] + GenerateMax(d,dp,c,cp,x,n)
            if(a > max_num):
                max_num = a
    if(i+dp[i]+cp[i]+1 >= n):
        a = d[i] + c[i]
        if(a > max_num):
            max_num = a
    else:
        for x in range(i+dp[i]+cp[i]+1,n):
            a = d[i] + c[i] + GenerateMax(d,dp,c,cp,x,n)
            if(a > max_num):
                max_num = a
    
    maxp[i] = max_num
    return max_num

n = input()
d = raw_input().split(' ')
dp = raw_input().split(' ')
c = raw_input().split(' ')
cp = raw_input().split(' ')
for i in range(n):
    d[i] = int(d[i])
    dp[i] = int(dp[i])
    c[i] = int(c[i])
    cp[i] = int(cp[i])
    maxp.append(-1)
for i in range(0,dp[0]+cp[0]+1):
    GenerateMax(d,dp,c,cp,i,n)
print(max(maxp))
