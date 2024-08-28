

# set() 

# n = input("Unesi neki broJ: ") 
# set_of_numbers = set(n) 
# result = len(set_of_numbers) 
# print(f"Broj cifara je: {result}")   

# 2     tuple ----- ()
def fun(x): 
    return x[1] 

countries = [("Montenegro", 600000), ("serbia", 70000000)]   # lista sa elementima ( , )
 

def max_num_of_people(x): 
    result = max(x, key=fun) 
    return result 


# result = max_num_of_people(countries) 
# print(result) 


# # 3 
# d = {"Ana": "Marko", "Milica": "Stefan", "Dragana":"Milica", "Marko": "Dragana"} 

# for sef in d.values(): 
#     if sef not in d.keys(): 
#         print(sef) 


# 4 




def is_leap_year(x): 
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0): 
        return 29
    else: 
        return 28 
    
def year_before(x): 
    day, month, year = x.split(".") 
    februar = is_leap_year(int(year)) 
    list_of_months = {"01":31, "02" : februar, "03" : 31, "04": 30, "05": 31,  
                      "06":30, "07":31, "08": 31, "09":30, "10" :31, "11": 30, "12":31}
    if month == "01": 
        if day == "01": 
            return f"{31}.{12}.{int(year)-1}" 
        else: 
            return f"{int(day)-1}.{month}.{year}"
    else: 
        if day == "01": 
            new_day = f"{int(month)-1}"
            if len(new_day) == 1:
                new_day = f"0{int(month)-1}"
            return f"{list_of_months[new_day]}.{int(month) - 1}.{year}"
        else: 
            return f"{int(day)-1}.{month}.{year}"


date = input("Unesi neki datum: ") 
print(year_before(date)) 









