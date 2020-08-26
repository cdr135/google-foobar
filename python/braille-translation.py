import math
def solution(s):
    return ''.join(map(braille,s))
    
def braille(c):
    if ord('A')<=ord(c)<=ord('Z'):
        return '000001'+braille(chr(ord(c)^32))
    if c==' ': return '000000'
    n = ord(c)-ord('a')
    d=math.floor(n/10)
    if 0<=n<22:
        p = n%10
    elif n>22:
        p = (n-1)%10
    else:
        p = 9
    code = (('10','00'),
            ('11','00'),
            ('10','10'),
            ('10','11'),
            ('10','01'),
            ('11','10'),
            ('11','11'),
            ('11','01'),
            ('01','10'),
            ('01','11'))[p]
    return code[0]+str(int(d>0&&n!=22))+code[1]+str(int(d>1))
