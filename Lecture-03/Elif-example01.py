#input the number of employees from the user
num_employees = int(input("Enter the number of employees: "))
if num_employees < 50:
    print("This is a small company.")
elif num_employees < 250:
    print("This is a meduim-sized company.")
elif num_employees >=250:
    print("This is a large company.")