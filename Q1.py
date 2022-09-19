n = 100
fact = 1
  
for i in range(1, n+1): 
    fact = fact * i

# print(fact)

# # Convert number to string
text_fact = str(fact)

# print(text_fact)
# Initialize empty list for every letter of factorial string 
summ = []

for letter in text_fact:
    summ.append(int(letter))
print(sum(summ))