
import math 

def zapremina(x): 
    pi = math.pi 
    return x[0]**2 * pi * x[1]  


lista_valjaka = [(4,4), (5,4), (3,3), (10, 10)]  

lista_valjaka.sort(key=zapremina, reverse=True)  
print(lista_valjaka) 