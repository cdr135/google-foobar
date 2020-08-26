from itertools import combinations
def solution(num_buns, num_required):
    b = [[] for i in range(num_buns)]
    for n,buns in enumerate(combinations(range(num_buns), num_buns-num_required+1)):
        for i in buns:
            b[i]+=[n]
    return b
