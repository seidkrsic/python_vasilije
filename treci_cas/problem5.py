

d = {
    "Strukture podataka" : "207", 
    "Matematika" : "106", 
    "Programiranje" : "207", 
    "Fizika" : "013", 
} 

help_dict = {} 

for sala in d.values():
    if sala not in help_dict.keys(): 
        help_dict[sala] = 1 
    else: 
        help_dict[sala] += 1


# print(max(help_dict)) 


# def fun(x): 
#     return x[1] 

# lista = [(1,2), (6,4), (5,6)] 

# print(max(lista, key=fun)) 
    