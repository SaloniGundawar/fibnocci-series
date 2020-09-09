x=int(input("Number of terms?"))
fiblist=[0,1]
if(x<=0):
    print("Enter a positive no.!!")
elif(x==1):
    print (fiblist[0])
elif(x==2):
    print (fiblist)

else:
    for i in range (2,x):
        fib= fiblist[i-1] + fiblist[i-2]
        fiblist.append(fib)
    print(fiblist)
