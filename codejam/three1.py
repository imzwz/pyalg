class Cake:
    def __init__(self, radius, high):
        self.radius = radius
        self.high = high

def com(i,j):
    return i.radius - j.radius

def fun(cakes,k):
    n = len(cakes)
    for i in range(n-k):
        tempAns = 0
        tempAns = cakes[i].radius*pi + cakes[i].radius*2*pi*cakes[i].high

            tempAns = values[i][0] * values[i][0] * PI;
            tempAns += values[i][0] * 2 * PI * values[i][1];
            int[][] tempValue = Arrays.copyOf(values, values.length - i - 1);
            for (int j = 0; j < tempValue.length; j++) {
                tempValue[j] = values[i + 1 + j];
            }
            Arrays.sort(tempValue, new Com1());
            for (int j = 0; j < K - 1; j++) {
                tempAns += tempValue[j][0] * 2 * PI * tempValue[j][1];
            }
            res = Math.max(res, tempAns);
        }
    
    
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
    sorted(cakes, cmp=com)
    n = fun(cakes,n, k) 
    res="Case #%d: %d\n" % (i,n)
    #res="Case #"+i +": "+n+"\n"
    outfile.write(res)
    outfile.flush()
infile.close()
outfile.close()

    

