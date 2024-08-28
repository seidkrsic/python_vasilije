import sys 

s = input("Unesi neki string: ")    # string oblika a^2n - b^n 

if s.count("-") != 1:
    sys.exit("Ne") 
else:  
    first, last = s.split("-") 
 
first_set = set(first)
last_set = set(last) 

if len(first_set) > 1 or len(last_set) > 1: 
    print("ne") 
else: 
    if len(first) == 2 * len(last): 
        print("Da") 
    else: 
        print("Ne") 
