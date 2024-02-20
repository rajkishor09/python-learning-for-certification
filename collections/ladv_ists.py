countries = [
    'Argentina',
    'Brazil',
    'Chile',
    'Colombia',
    'Ecuador',
    'Peru',
    'Uruguay',
]

new_countries = countries.copy() # creates a copy of the list
# new_countries2 = countries.copy[:] # creates a copy of the list

new_countries.append('Venezuela')
print(countries)
print(new_countries)
print([nc + ":-" for nc in new_countries]) # comprehension is like map in JS
print([nc + ":-" for nc in new_countries if nc.endswith("a")]) # print only which endswith "a"