def fun(k, S, A):
    return 0
def updateS(S,A):
    return S
infile = open("in1.txt")
outfile = open("pout1.txt","w")
data = []
data = infile.readline().split(" ")
n = int(data[0])
k = int(data[1])
d = []
for i in range(n):
    str = infile.readline().split(" ") 
    d.append(str)
res = d
outfile.write(res.toByte())
outfile.flush()
infile.close()
outfile.close()

    

