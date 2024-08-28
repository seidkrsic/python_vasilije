

n = 357 
s = str(n)  # "357" 
m = int(s[::-1]) 
print(m) 


# 3 
d = "17.03.2023" 
a = d.split(".") 
a[0] = str(int(a[0])+1) 
s = "-".join(a) 
print(s) 

# 4 

e = 0.5 
t = 1 
s = 0 
i, j = 1, 1 
while t>=e: 
    s+=t 
    i+=2 
    j+=1 
    t = i/(j**2) 
print(s) 

# 5 

n, i = 5, 1 
while i<=n: 
    j = 1 
    s = "" 
    while j<=i: 
        s += "*" 
        j += 1 
    print(s) 
    i+=1 


""" 
       * 
      ***
     ***** 
      ***
       *

""" 

# 6 
# {"aksj": akjsf, ...}
n = 1223
s = str(n) 
x = set(s) # {1,2,3} 
print(len(x)) 


# 7 

s1 = "aakdjfk" 
s2 = "kdjfk" 
st1 = set(s1) 
st2 = set(s2) 


