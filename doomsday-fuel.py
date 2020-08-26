from fractions import Fraction, gcd
def solution(m):
    dim = len(m)
    tr  = [i for i in range(dim) if sum(m[i]) and m[i][i]!=sum(m[i])]
    end = [i for i in range(dim) if i not in tr]
    eqs = [[Fraction(m[i][j],sum(m[i]))-(j==i) for j in tr] +
           [Fraction(-m[i][j],sum(m[i])) for j in end] for i in tr]
    solve(eqs)
    if len(eqs) < 1: return [1,1]
    solution = eqs[0][len(tr):]
    denom = int(reduce(lcd, (p.denominator for p in solution)))
    return [int(p*denom) for p in solution]+[denom]

def lcd(a, b):
    return int(a*b/gcd(a,b))

def solve(mat):
    dim = len(mat)
    for i in range(dim):
        j = i
        while 0==mat[j][i]: j+=1
        if j != i:
            for k in range(i, len(mat[j])):
                mat[i][k] += mat[j][k]
        r = mat[i][i]
        mat[i] = [c/r for c in mat[i]]
        for j in range(i+1, dim):
            r = mat[j][i]
            for k in range(i,len(mat[j])):
                mat[j][k] -= r*mat[i][k]
    for i in range(dim-1,-1,-1):
        for j in range(i):
            r = mat[j][i]
            for k in range(i, len(mat[j])):
                mat[j][k] -= r*mat[i][k]
                
