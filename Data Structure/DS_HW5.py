class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] 
                         for row in range(V)]
  
    def isBicolorable(self, src): 
  
        colorArr = [-1] * self.V 
        colorArr[src] = 1
        queue = [] 
        queue.append(src) 

        while queue: 
            u = queue.pop()
            
            if self.graph[u][u] == 1: 
                return False; 
            
            for v in range(self.V): 
                if self.graph[u][v] == 1 and colorArr[v] == -1: 
                    colorArr[v] = 1 - colorArr[u] 
                    queue.append(v) 
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]: 
                    return False
        return True

answer=[]
while True: 
    A=[]
    V=int(input())
    if V==0:
        break
    L=int(input())
    for i in range(L):
        a=input().split()
        a=[int(j) for j in a]
        A.append(a)

    g = Graph(V) 

    for i in range(L):
        g.graph[A[i][0]][A[i][1]]=1
        g.graph[A[i][1]][A[i][0]]=1
  
    answer.append("BICOLORABLE." if g.isBicolorable(0) else "NOT BICOLORABLE." )

for element in answer:    
      print(element)





