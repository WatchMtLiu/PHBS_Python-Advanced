for i in range(1,10):
    for j in range(1,i+1):
        if j!=i:
            print(str(j)+"*"+str(i)+"="+str(i*j)+" ",end="")
        else:
            print(str(j)+"*"+str(i)+"="+str(i*j),end="\n")
