

# 1 
a = [1,2,3,4,5] 
b = [] 
for index, element in enumerate(a):  
    b.append(index*element)

print(b) 

# 2 
a = [1,2,3,2,1,4,3] 
i=0 
while i<len(a): 
    if a[i] in a[i+1:]: 
        a.pop(i) 
    else: 
        i+= 1 
print(a) 
# a = [1,2,3,4] 
# print(a[-3:])   

# 5 
def fun(x): 
    return x % 2 == 1

l = [12673, 28532] 
l.sort(key=fun, reverse=True)    
print(l) 



# 6 
a = "Strukture    podataka u Pythonu" 
d = {} 
for b in a.split(): 
    d[b] = len(b) 

print(d) 
#d = {"Strukture": 8} 


d1 = {"a": 50, "b": 30} 
d2 = {"b": 30, "c": 20, "d": 2000}  

for k in d2.keys():      
    if k in d1.keys():
        d1[k] += d2[k] 
    else: 
        d1[k] = d2[k] 
print(d1) 