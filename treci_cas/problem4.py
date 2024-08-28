


i_love_python = 0   # snake_case 
iLovePython = 0    # camel_case 


def snake_case_to_camel_case(x): 
    list_of_words = x.split("_")
    help_list = list_of_words[1:] 
    # help_list2 = []
    # for element in help_list: 
    #     help_list2.append(element.capitalize()) 
    
    # return list_of_words[0] + "".join(help_list2) 

    return list_of_words[0] + "".join([item.capitalize() for item in help_list]) 


string = "snake_case_to_camel_case"
print(snake_case_to_camel_case(string)) 