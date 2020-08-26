def solution(pegs):
    n = 2*rad(diffs(pegs))
    d = (3,1)[len(pegs)%2]
    r=n/d
    if n%d==0:
        n=r
        d=1
    if r<=1: return [-1,-1]
    for dist in diffs(pegs):
        r=dist-r
        if r<=1: return [-1,-1]
    return [n,d]
    
def rad(pegs):
    if len(pegs)==0: return 0
    return pegs[0]-rad(pegs[1:])

def diffs(l):
    return [a-b for a,b in zip(l[1:],l[:-1])]
