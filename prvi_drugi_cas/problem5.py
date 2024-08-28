

from string import punctuation 

n = "ovo je,neka recenica!python je super..." 
for letter in punctuation: 
    n = n.replace(f"{letter}"," ") 
result = n.split(" ") 
print(len(result)) 