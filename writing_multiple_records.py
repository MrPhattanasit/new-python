import struct
num_records = int(input('How many records do you want to create? '))
with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id_number = int(input('Enter ID : '))
        name = input('Enter Name: ')
        age = int(input('Age: '))
        gpa = float(input('Enter GPA: '))
        data = struct.pack('i20sif', id_number, name.encode(), age, gpa)
        file.write(data)
print(f'{num_records} records written to records.bin.')