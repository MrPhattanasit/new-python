#Program to compare the strings "Mary" and "Mark"

#Define the strings
string1 = "Mary"
string2 = "Mark"

#Compare the strings for equality
if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

#Lexicographical comparision
if string1 < string2:
    print(f'"{string1}" comes before "{string2}" inlexicographical order.')

#Case-insensitive comparision
if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
     print(f'"{string1}" and "{string2}" are not equal when case is ignored.')