# In Python, decision-making is done using if-elif-else blocks.
age = 14
if age < 13:
    print("You're a child!")
elif age < 18:
    print("You're a teenager!")
else:
    print("You're an adult!")
    

# Comparison & Logical Operators
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
score = 86
if score >= 80 and score <= 100 :
    print("Excellent!")
    
    
# ✅ For Loop – Iterates over a sequence (like a list or range)
for i in range(5):
    print("Number", i)
    
# ✅ While Loop – Repeats while condition is true
count = 0
while count < 5:
    print("Number is:", count)
    count+=1
    
# Exercise 1: Write a program that checks if a number is positive, negative, or zero.
number = 5
if number > 0:
    print(f"The Number {number} is positive")
elif number < 0:
    print(f"The Number {number} is negative")
else:
    print(f"The Number {number} is zero")
    
# Exercise 2: Loop through a list of numbers and print whether each is even or odd.
for i in range(1,8):
    if i % 2 == 0:
       print(f"The Number {i} is an Even number!")
    else:
        print(f"The Number {i} is an Odd number!")
        
# Exercise 3: Print numbers 1 to 10 using a while loop.
num = 1
while num <= 10:
    print(num)
    num+=1