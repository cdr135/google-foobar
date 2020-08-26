from collections import deque
def solution(map):
    w = len(map)
    h = len(map[0])
    sdist = [[0 for c in r] for r in map]
    fdist = [[0 for c in r] for r in map]
    def fill(arr, x,y):
        q = deque([(1,x,y)])
        while q:
            d,i,j = q.pop()
            if 0<=i<w and 0<=j<h and arr[i][j]==0:
                arr[i][j]=d
                d+=1
                if map[i][j]==0:
                    q.extendleft(((d,i-1,j),(d,i+1,j),
                                  (d,i,j-1),(d,i,j+1)))
    fill(sdist, 0, 0)
    fill(fdist,w-1,h-1)
    return min(sdist[i][j]+fdist[i][j] for i in range(w) for j in range(h)
               if sdist[i][j] and fdist[i][j])-1
