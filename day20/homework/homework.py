#  1. Check if the first letter of a string is uppercase
# my_string = "HelloWorld"
# if my_string[0].isupper():
#     print(my_string.upper())
# else:
#     print(my_string.lower())

#  2. Check if the user's input contains at least one uppercase letter
# user_name = input("Enter your name: ")
# contains_upper = any(char.isupper() for char in user_name)
# if contains_upper:
#     print(user_name.lower())
# else:
#     print(user_name.capitalize())

#  3. Check a list of animal names for specific conditions
# animal_names = ["Tiger", "cat", "Dog", "Elephant", "Ant"]
# for name in animal_names:
#     if len(name) < 5 and name[0].isupper():
#         print(name[:3])
#     else:
#         print(f"{name} is long")

#    4. Convert a list of lowercase names to uppercase
# lowercase_names = ["john", "jane", "doe"]
# uppercase_names = [name.upper() for name in lowercase_names]
# print(uppercase_names)

# 5. Process a list with mixed data types
mixed_list = ["hello", 123, 45.6, "world", True, "python"]
for item in mixed_list:
    if isinstance(item, str):
        print(item.upper()[-3:])
 