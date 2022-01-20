class Graph(): 
  
    def __init__(self,x, V): 
        self.V = V 
        self.graph = x
        
    def printAllPathsUtil(self, u, d, visited, path): 
        visited[u]= True
        path.append(u) 
        if u == d: 
            print(path,len(path)-1)
        else: 
            y=self.graph[u]
            i=[i for i in range(len(y)) if y[i]!= 0]
            for element in i:
                if visited[element]==False: 
                    self.printAllPathsUtil(element, d, visited, path) 
        
            
        path.pop() 
        visited[u]= False
        

    def printAllPaths(self,s, d): 
        visited =[False]*(self.V) 
        path = [] 
        self.printAllPathsUtil(s, d,visited, path) 
        
x=[]
keys = [line.rstrip('\n').split() for line in open('Q1.txt','r')]
for j in range(len(keys)):
    x.append([int(i) for i in keys[j]])

g = Graph(x,len(x)) 

s = 5; d = 7
print ("paths from %d to %d :" %(s, d)) 
g.printAllPaths(s, d) 
