class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __mul__(self,other):
        return Point(self.x * other.x, self.y + other.y)
N=int(input())
for i in range(0,N):
    x=int(input())
    y=int(input())
    a=Point(x,y)
    a = input().split()
    c = x + y
print(c)    
