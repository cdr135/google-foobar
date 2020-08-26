from collections import deque
def solution(n):
    t = {int(n):0}
    q = deque([int(n)])
    while 1 not in t:
        n = q.popleft()
        if n%2: op = (n+1,n-1)
        else: op = (n/2,)
        for v in op:
            if v not in t:
                t[v]=t[n]+1
                q.append(v)
    return t[1]

'''from collections import deque
def solution(n):
    t = {int(n):0}
    q = deque([int(n)])
    while 1 not in t:
        n = q.popleft()
        op = [n+1,n-1] if n%2 else [n/2]
        for v in op:
            if v not in t:
                t[v]=t[n]+1
                q.append(v)
    return t[1]


def s2(n):
    t = {int(n):0}
    q = deque([int(n)])
    while 1:
        n = q.popleft()
        op = [n+1,n-1] if n%2 else [n/2]
        for v in op:
            if v==1: return t[n]+1
            if v not in t:
                t[v]=t[n]+1
                q.append(v)

def solution2(n):
    n=int(n)
    s=0
    while n>1:
        s+=1
        if n%8==7:
            n+=1
        else:
            s+=n&1
            n>>=1
    return s
'''
