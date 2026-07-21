#Input string from user
input_string = input("Enter a string: ")

# Initialize an empty string for the modified result
modified_string = ""

#define a set of vowels
vowels = "aeiouAEIOU"

# Use a for loop to iterate through the input string
for char in input_string:

    upper_char = char.upper()

    if upper_char in vowels:
        modified_string +="*"
    else:
        modified_string += upper_char

print("Modified string:", modified_string)