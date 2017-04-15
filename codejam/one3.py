infile = open("in3.txt")
outfile = open("out3.txt","w")
line = int(infile.readline())+1
data = []
for i in range(1,line):
    data = infile.readline().split(" ")
    hd = int(data[0])
    ad = int(data[1])
    hk = int(data[2])
    ak = int(data[3])
    b = int(data[4])
    d = int(data[5])
    n = getRes(hd,ad,hk,ak,b,d) 
    if n = -1:
        outfile.write("Case #%d: IMPOSSIBLE" % (i))
    #res="Case #"+i +": "+n+"\n"
    else:
        outfile.write("Case #%d: %d" % (i,n))
    outfile.flush()
infile.close()
outfile.close()
def getRes(hd,ad,hk,ak,b,d):
    if ad > hk:
        return 1
    if hd < ak-d:
        return -1
    if ad+b > hk:
        return 2
    if hd < 2*ak -b:
        return -1



    

