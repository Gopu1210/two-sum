  a = int(input())
l=[]
for i in range(a):
    l.append(int(input()))
print(l)
target = int(input())
b=[]
for i in range(len(l)-1):
    for j in range(i+1):
        if(l[j]==target-l[i]):
            print(j,i)
