


n = int(input("Unesi broj n: ")) 
m = int(input("Unesi broj m: "))  

for i in range(n):
    # prvo i=0, .... a posljednje je i=n-1 
    if i == 0 or i ==n-1:
        print("*"*m) 
    else: 
        print("*" + " "*(m-2) + "*")  



# for i in range(n): 
#     for j in range(m): 
#         if i==j: 
#             print("*", end="") 
#         else: 
#             print(" ", end="") 
#     print("") 