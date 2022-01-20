import heapq
n=int(input())
l=(input())
l=l.split()
l=[int(i) for i in l]
p=input()
p=p.split()
p=[int(i) for i in p]
add=int(input())
a=[]
for i in range(add):
    aa=input().split()
    aa=[int(i) for i in aa]
    aa[0],aa[1]=aa[1],aa[0]
    a.append(aa)

A=[]    
for i in range(n):
    A.append([p[i],l[i]])
            
heap=[]
for item in p:
    heapq.heappush(heap,item)
 
heapq.heapify(A) # heapify the list based on first element i.e priority

x=[]
for i in range(add):
    x.append(heapq.heapreplace(A,a[i]))
    
for i in range(n):  
    x.append(heapq.heappop(A))
    
y=[e[1] for e in x]  
print(*y)  