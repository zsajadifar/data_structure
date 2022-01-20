class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False

class Trie: 
    
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self):  
        return TrieNode() 

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a') 


    def insert(self,key): 
        A = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            
            if not A.children[index]: 
                A.children[index] = self.getNode() 
            A = A.children[index]  
        A.isEndOfWord = True


    def search(self, key): 
        A = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not A.children[index]: 
                return False
            A = A.children[index]  
        return A != None and A.isEndOfWord 


keys = [line.rstrip('\n') for line in open('Q2.txt','r')]
output = ["Not present in trie", "Present in trie"] 
t = Trie() 
for key in keys: 
    t.insert(key) 
# Search for different keys 
print("{} ---- {}".format("the",output[t.search("amir")])) 
print("{} ---- {}".format("these",output[t.search("all")])) 
print("{} ---- {}".format("their",output[t.search("allah")])) 
print("{} ---- {}".format("thaw",output[t.search("aminiii")])) 




