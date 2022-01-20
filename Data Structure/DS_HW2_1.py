#capacity = int(input("Enter the number of frames: "))
capacity = int(input())
f,fault,top = [],0,0
#print("Enter the reference string: ",end="")
L=input()
s = list(map(int,input().strip().split()))
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity
        fault += 1
print(fault)