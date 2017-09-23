import random
import string

def lcs(X , Y):

    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    return L[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))
t = []
ans = []
for i in range(15):
    a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5,25)))
    b = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5,25)))
    t.append((a,b))
    ans.append(lcs(a,b))

print(t)
print(ans)    
