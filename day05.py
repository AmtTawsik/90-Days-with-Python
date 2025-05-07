# 📘 Day 5: Dictionaries in Python
# 🧠 Focus: Key-value storage, accessing, adding, updating, and looping

# 🔹 Part 1: What is a Dictionary?
# A dictionary stores data in key-value pairs. Keys must be unique.

person = {
    "name": "Abdullah",
    "age": 24,
    "city": "Dhaka"
}
print(person["name"])

# 🔹 Part 2: Adding and Updating Values
person["email"] = "amttawsik.cse@gmail.com"
person["age"] = 25


# 🔹 Part 3: Looping Through a Dictionary
# You can loop through keys, values, or both:
for key, value in person.items():
    print(key,":",value)


# ✅ Exercise 1:
# Create a dictionary called student with keys name, id, and department. Print each key and value using a loop.

student = {
    "name" : "Rahul",
    "id": 7,
    "department": "CSE"
}
for key, value in student.items():
    print(key, ":", value)
    
# ✅ Exercise 2:
# Update the department key to a new value, and add a new key called cgpa.
student["department"]="EEE"
student["cgpa"] = 3.84

for key, value in student.items():
    print(key, ":", value)
    
# ✅ Exercise 3:
# Create a dictionary of 3 countries and their capitals. Remove one country and print the final dictionary.
countries = {
    "Bangladesh": "Dhaka",
    "India": "Delli",
    "Pakistan": "Islamabad"
}
countries.pop("India")

for key, value in countries.items():
    print(key, ":", value)