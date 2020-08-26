from fractions import Fraction,gcd

# As much as I wish I was, I'm not proficient enough in group theory to
# have solved this myself.
# Reference: https://math.stackexchange.com/a/2057828/627474

def collect(x):
    terms = {t for t,c in x}
    return {t:sum(c for t2,c in x if t2==t) for t in terms}
    
ci1_cache={}
def cind1(n):
    if n in ci1_cache:
        return ci1_cache[n]
    if n==0: return {tuple(0 for i in range(20)):Fraction(1)}
    return collect([(tuple((t[j]+(j+1==n-i) for j in range(20))),c/n)
                    for i in range(n) for t,c in cind1(i).items()])

def solution(w, h, s):
    in1 = cind1(w)
    in2 = cind1(h)
    return str(sum(in1[x]*in2[y]*
                   s**sum(x[u]*y[v]*gcd(u+1,v+1)
                          for u in range(20) if x[u]
                          for v in range(20) if y[v])
                   for x in in1 for y in in2))
