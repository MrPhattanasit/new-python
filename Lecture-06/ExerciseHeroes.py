heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']
heroes.append('Black Panther')
print(heroes)
heroes.insert(1,'Spiderman')
print(heroes)
heroes.remove('Hulk')
print(heroes)
heroes.sort()
while 'Spiderman' in heroes:
    heroes.remove('Spiderman')
print(heroes)