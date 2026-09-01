person_count = (
        ('Ingrid Virgo','4587','Engineering'),
        ('Julia Rich','4588','Research'),
        ('Greg Young','4589','Marketing'),
        # ('Name: ', input('Name: ')),
        # ('ID number: ', input('ID number: ')),  
        # ('Department: ', input('Department: '))
)
with open('employees.txt', 'w') as emp_file:
    for name, id_number, department in person_count:
        emp_file.write(f'Name: {name}\n')
        emp_file.write(f'ID number: {id_number}\n')
        emp_file.write(f'Department: {department}\n')
        emp_file.write('\n')
        print()
print('Employee records written to employees.txt.')
