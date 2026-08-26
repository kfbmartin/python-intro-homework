#Linear Search: Find a name in a list
names = [
    "Liam",
    "Noah",
    "Oliver",
    "Theodore",
    "Henry",
    "JaKmes",
    "Elijah",
    "Mateo",
    "William",
    "Lucas",
    "Olivia",
    "Charlotte",
    "Emma",
    "Amelia",
    "Sophia",
    "Mia",
    "Isabella",
    "Evelyn",
    "Ava",
    "Elian"
]
#User input the name to be searched
username = input("Enter a name to search for: ")
found = False

for i, name in enumerate(names):
    if name == username:
        found = True
        break

if found: 
    print(f'Found "{username}" at index {i}.')

else:
    print (f'"{username}" was not found in the list.')