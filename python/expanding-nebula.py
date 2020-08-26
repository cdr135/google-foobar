#expanding-nebula
from collections import deque
from itertools import product
def solution(g):
    pr = deque()
    return sum(rows(zip(*g)).values())

col_cache={}
sr=[[[0,0]],[[0,1]],[[1,0]],[[1,1]]]
def col(c):
    c=tuple(c)
    if c in col_cache: return col_cache[c]
    if len(c)==0: return sr
    return [p+r for r in sr for p in col(c[:-1])
            if (sum(r[0],sum(p[-1]))==1)==c[-1]]

def rows(r):
    cr = [zip(*c) for c in col(r[-1])]
    e  = {c[1] for c in cr}
    if len(r)==1:
        return {c:sum(1 for a,b in cr if b==c) for c in e}
    pv = rows(r[:-1])
    return {c:sum(pv[a] for a,b in cr if b==c and a in pv) for c in e}
