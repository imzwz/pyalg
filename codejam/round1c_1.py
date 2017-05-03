# _*_ coding:utf-8 _*_
class Cake:
    def __init__(self, radius, high):
        self.radius = radius
        self.high = high

def com(i,j):
    return j.radius - i.radius

def fun(cakes,k):
    n = len(cakes)
    stack = []
    i=0
    result=0
    maxnum=0
    while stack or i<n:
        while len(stack) < k and i < n:
            stack.append(i)
            result = result + cakes[i].radius*2*pi*cakes[i].high
            i = i+1
        totalresult = result + cakes[stack[0]].radius * cakes[stack[0]].radius * pi
        if totalresult > maxnum:
            maxnum = totalresult
        i = stack.pop()
        result = result - cakes[i].radius*2*pi*cakes[i].high
        i = i+1
    return maxnum

pi = 3.14159265358979    
infile = open("in.txt")
outfile = open("pout.txt","w")
line = int(infile.readline())+1
data = []
for i in range(1,line):
    data = infile.readline().split(" ")
    n = int(data[0])
    k = int(data[1])
    cakes = []
    for j in range(n):
        sh = infile.readline().split(" ")
        cakes.append(Cake(int(sh[0]),int(sh[1])))
    cakes.sort(cmp=com)
    n = fun(cakes,k) 
    res="Case #%d: %f\n" % (i,n)
    #res="Case #"+i +": "+n+"\n"
    outfile.write(res)
    outfile.flush()
infile.close()
outfile.close()

    

