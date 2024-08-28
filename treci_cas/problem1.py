

# 1 

def divisible_by_digits(x):
    list_of_digits = [] 
    for letter in x:
        if letter != "0": 
            if int(letter) not in list_of_digits:   
                list_of_digits.append(int(letter))    
    
    for item in list_of_digits:
        if int(x) % item != 0:
            return False 
    return True 



n = input("Unesi neki broj: ") 

print(divisible_by_digits(n)) 