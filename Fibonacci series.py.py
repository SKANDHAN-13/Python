a=0
b=1
c=[0,1]
n=int(input("Enter the number of terms : "))
if n==1:
    c=[0]
    print(c)
elif n==2:
    c=[0,1]
    print(c)
else:
    
    for i in range(0,n-2):
        c.append(c[i]+c[i+1])
    print(c)
