countries = [
    'Argentina',
    'Brazil',
    'Chile',
    'Colombia',
    'Ecuador',
]

countries.append("India") # adds this in the last position
print(countries)

countries.insert(0, "Mexico") # adds this in the first position
print(countries)

countries.insert(-1, "Swiss")
countries.sort()
print(countries)