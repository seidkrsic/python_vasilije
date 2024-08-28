

from datetime import datetime, timedelta

# Get the input date from the user in the format "DD.MM.YYYY"
input_date = input("Unesite datum u formatu 'DD.MM.YYYY': ")
day, month, year = map(int, input_date.split(".")) 
# Get the number of days K
K = int(input("Unesite broj dana K: "))

# Convert the input string into a datetime object
date_object = datetime(year, month, day) 
print(date_object) 

# Add K days to the date
new_date = date_object + timedelta(days=K)

# Print the new date in the same format "DD.MM.YYYY"
print(f"Datum nakon dodavanja {K} dana je: {str(new_date)[:10]}") 

