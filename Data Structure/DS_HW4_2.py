def heapreplace(heap, item):
    returnitem = heap[0]
    heap[0] = item
    _siftup(heap, 0)
    return returnitem


def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
    
    
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem    

           
            
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
            
    
heapify(A) # heapify the list based on first element i.e priority

x=[]
for i in range(add):
    x.append(heapreplace(A,a[i]))
    
for i in range(n):  
    x.append(heapq.heappop(A))
    
y=[e[1] for e in x]  
print(*y)             