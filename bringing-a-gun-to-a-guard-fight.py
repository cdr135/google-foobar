from fractions import gcd
def solution(dimensions, your_position, guard_position, distance):
    sx,sy=your_position
    def direction(x,y):
        dx=x-sx
        dy=y-sy
        if dx==dy==0: return (0,0)
        if dx==0: return (0,1)
        if dy==0: return (1,0)
        d = abs(gcd(dx,dy))
        return (dx/d,dy/d)
    def sqdist(x,y):
        return (x-sx)**2+(y-sy)**2
    def dirs(x,y):
        d = {}
        xdim,ydim = dimensions
        targets = ([ x, y],
                   [-x, y],
                   [ x,-y],
                   [-x,-y])
        xoff = 2*xdim
        yoff = 2*ydim
        nx = distance/xoff+2
        ny = distance/yoff+2
        for i in range(-nx,nx+1):
            for j in range(-ny,ny+1):
                for a,b in targets:
                    tx=a+i*xoff
                    ty=b+j*yoff
                    sqd = sqdist(tx,ty)
                    if sqd<=distance**2:
                        drc = direction(tx,ty)
                        if drc not in d or d[drc]>sqd:
                            d[drc]=sqd
        return d

    gd=dirs(*guard_position)
    sd=dirs(sx,sy)
    return sum(1 for d in gd if d not in sd or gd[d]<sd[d])
