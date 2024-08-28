

n = input("Unesi neki broj: ") 
new_number = ""
for digit in n: 
    if int(digit) % 2 != 0:     # "2" -- > 2 
        new_number = new_number + digit 

print(new_number) 