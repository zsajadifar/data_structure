import math
s = []
#item=input("Enter your postfix or prefix expression: ")
L=input()
item=input()
s=item.split() #Adding items to stack 

j=[]
if(s[0]=='*' or s[0]=='/' or s[0]=='+' or s[0]=='-' or s[0]=='^'): #prefix
    for i in range(len(s),0,-1):
        i=i-1
        if(s[i]!='*' and s[i]!='/' and s[i]!='+' and s[i]!='-' and s[i]!='^'):
            j.append(int(s[i]))
            
        elif(s[i]=='*'): 
        	x=j.pop()
        	y=j.pop()
        	res = x * y
        	j.append(res)
            
        elif(s[i]=='+'):
        	x=j.pop()
        	y=j.pop()
        	res = x + y
        	j.append(res)
            
        elif(s[i]=='-'):
        	x=j.pop()
        	y=j.pop()
        	res = x - y
        	j.append(res)
            
        elif(s[i]=='/'):
        	x=j.pop()
        	y=j.pop()
        	res=math.floor(x/y)
        	j.append(res)
        
        elif(s[i]=='^'):
        	x=j.pop()
        	y=j.pop()
        	res = x**y
        	j.append(res)

else: # postfix
    for i in range(len(s)):       
        if(s[i]!='*' and s[i]!='/' and s[i]!='+' and s[i]!='-' and s[i]!='^'):
            j.append(int(s[i]))
            
        elif(s[i]=='*'): 
        	x=j.pop()
        	y=j.pop()
        	res = y * x
        	j.append(res)
            
        elif(s[i]=='+'):
        	x=j.pop()
        	y=j.pop()
        	res = y + x
        	j.append(res)
            
        elif(s[i]=='-'):
        	x=j.pop()
        	y=j.pop()
        	res = y - x
        	j.append(res)
            
        elif(s[i]=='/'):
        	x=j.pop()
        	y=j.pop()
        	res=math.floor(y/x)
        	j.append(res)
        
        elif(s[i]=='^'):
        	x=j.pop()
        	y=j.pop()
        	res = y**x
        	j.append(res)

print(j[0])