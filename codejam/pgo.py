infile = open("in.txt")
outfile = open("pout.txt","w")
line = int(infile.readline())+1
data = []
for i in range(1,line):
    data = infile.readline().split(" ")
    r = int(data[0])
    c = int(data[1])
    n = (r+c)/2
    res="Case #%d: %d\n" % (i,n)
    #res="Case #"+i +": "+n+"\n"
    outfile.write(res)
    outfile.flush()
infile.close()
outfile.close()

    

