finput = open("info.txt","r")
output = open("infoo.txt","w") #w is to write

count = 0
for line in finput:
    count += 1
    output.write("{:2d} {}".format(count,line))
output.close()