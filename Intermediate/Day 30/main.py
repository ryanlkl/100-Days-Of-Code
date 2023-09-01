# FileNotFound

# try:
#     file = open("Day 30\\a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("Something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("I created this error.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3m")

bmi = weight / height ** 2
print(bmi)
