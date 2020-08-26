def solution(s):
    t=0
    m=0
    for c in s:
        if c=='>': m+=1
        if c=='<': t+=2*m
    return t
