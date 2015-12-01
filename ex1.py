class Point:
    def __init__(self, s='0,0'):
        coord=list(map(float, s.split()))
        self.x=coord[0]
        self.y=coord[1]
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __mul__(self,other):
        return Point(self.x * other.x, self.y + other.y)
N=int(input())
xm=0
ym=0
rmax=0
cmx=0
cmy=0
    s=input()
    a=Point(s)
    rm=((a.x)**2 + (a.y)**2)**0.5 
    cmx=cmx + a.x
    cmy=cmy + a.y
    if rm>rmax:
        rmax=rm
        xm=a.x
        ym=a.y   
def maxPerimetr(coord):
    maxPer = 0
    for i in range(len(coord)):
        for j in range(1, len(coord)):
            for k in range(2, len(coord)):
                per = dist(coord[i], coord[j]) + dist(coord[i], coord[k]) + dist(coord[k], arr[j])
                if per > maxPer:
                    maxPer = per
    return maxPer                   
def rast(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5
print(xm,ym,cmx/N,cmy/N)  
