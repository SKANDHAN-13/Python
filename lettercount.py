a=[]
d={}
s=str(input("Enter the string : "))
s=s.lower()
list_s=list(s)
n=len(list_s)
for i in list_s:
    if i not in a:
        a.append(i)

for j in a:
    n=list_s.count(j)
    d[j]=n
print(d)
