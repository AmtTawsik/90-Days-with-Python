# Basic syntax:
def great():
    print("Hello, Mubin")
    
# To call it:
great()


# Function with Parameters let you pass values into the function:
def hello(name):
    print(f"Hello, {name}")
hello("Rahul")


# Function with Return Value. Functions can return data using the return statement:
def add(a,b):
    return a+b

result = add(7,5)
print(f"The adition is: {result}")



# Exercise 1:
# Write a function called welcome_user that takes a name as input and prints:
# "Welcome, <name>!"
def welcome_user(name):
    print(f"Welcome, {name}!")
    
welcome_user("Abdullah Al Mubin")


# Exercise 2:
# Write a function called is_even that takes a number as input and returns True if it’s even, otherwise False.
def is_even(number):
    if(number % 2 == 0):
        return True
    else:
        return False
check_your_number = is_even(5)
print(check_your_number)


# Exercise 3:
# Write a function called multiply_list that takes a list of numbers and returns the product of all elements.
def multiply_list(number_list):
    store = 1
    length = len(number_list)
    count = 0
    while count < length:
        store = store * number_list[count]
        count+=1
    return store
multiply_list_result = multiply_list([4,3,2,5])

print(f"The multiplication of all number is: {multiply_list_result}")
    
    