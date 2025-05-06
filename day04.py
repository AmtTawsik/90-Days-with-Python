# # 📘 Day 4: Lists, Tuples, and Sets in Python
# # 🧠 Focus: Understanding and using Python’s core collection types

# fruits = ["Apple", "Orange", "Cherry"]
# print(fruits[0])
# fruits.append("Banana")
# print(fruits)
# fruits.remove("Apple")
# print(fruits)

# # You can iterate over lists:
# for fruit in fruits:
#     print(fruit)
    
# # Tuples: A tuple is ordered and immutable (cannot be changed).
# dimensions = (10,20)
# print(dimensions[0])
# # **Useful when you want data to remain constant.

# # Sets: A set is unordered, mutable, and contains only unique values.
# languages = {"Python", "JavaScript", "Python"}
# print(languages)
# languages.add("C++")
# print(languages)
# # **Sets are great for removing duplicates.


# ✅ Exercise 1:
# Create a list of 5 fruits. Add one more, remove one, and print the final list.

my_favourite_fruits = ["Apple","Orange", "Banana", "Grape", "Pineapple"]
my_favourite_fruits.append("Avocado")
my_favourite_fruits.remove("Pineapple")
print(f"My favourite Fruits are: {my_favourite_fruits}")


# ✅ Exercise 2:
# Create a tuple of 3 colors and print each item using a loop.

colors = ("Red", "Green", "Blue")
for color in colors:
    print(color)
    
    
# ✅ Exercise 3:
# Create a set of programming languages with duplicates, remove a language, and print the unique values.

my_favourite_languages = {"Python", "Java", "JavaScript", "Rust", "Java", "C++"}
my_favourite_languages.remove("Rust")
print(f"My favourite languages are: {my_favourite_languages}")