infile = open("in.txt")
outfile = open("pout.txt","w")
line = int(infile.readline())+1
data = []
for i in range(1,line):
    data = infile.readline().split(" ")
    r = int(data[0])
    c = int(data[1])
    cake = [[]]*
    for j in range(r):
        string = infile.readline()
        for k in range(c):
            cake[j][k]=string[k]

    res="Case #%d:\n" % (i)
    #res="Case #"+i +": "+n+"\n"
    outfile.write(res)
    for j in range(r):
        outfile.write(cake[j]+"\n")
    outfile.flush()
infile.close()
outfile.close()

    

