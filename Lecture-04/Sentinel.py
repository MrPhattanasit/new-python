keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the item wholesale cost: '))

    retail = sales*2.5

    print(f'Retail price ${retail:.2f}')

    keep_going = input('Do you have another' + \
                       ' item (Enter y for yes): ')