

raspored = { 
    "ponedeljak" : [("Strukture podataka", 3)], 
    "utorak" : [("Matematika", 2), ("Engleski", 2)], 
    "srijeda" : [("principi programiranja", 3)], 
    "cetvrtak" : [("Matematika", 2), ("Strukture podataka", 3)], 
    "petak" : [("Python", 2), ("principi programiranja",2)] 
} 
new_dict = {}
for key, value in raspored.items(): 
    temp_value = 0 
    for subject in value: 
        temp_value += subject[1] 
    new_dict[key] = temp_value  


result = max(new_dict, key=new_dict.get) 
print(result)    