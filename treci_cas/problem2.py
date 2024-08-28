


def average_list(x): 
    empty_list = [] 
    average = sum(x)/len(x) 
    for item in x:
        if item >= average:
            empty_list.append(item) 
    
    return empty_list 




print(average_list([25, 30, 20, 35, 28])) 