#dodge-the-lasers
from decimal import *
getcontext().prec = 400
def solution(n):
    return str(b2(Decimal(n)))

def b2(n):
    if n==0: return 0
    s = Decimal(2).sqrt()*n
    l = s.to_integral_value(ROUND_FLOOR)
    h = s.to_integral_value(ROUND_CEILING)
    return l*h/Decimal(2) - bc((h/(Decimal(2)+Decimal(2).sqrt())).to_integral_value(ROUND_FLOOR))

def bc(n):
    return b2(n) + n*(n+1)
