contacts = {
    "Mansimran" : "9451384185",
    "Diya" : "9918715454",
    "Nakul" : "8121454626"
}

print(contacts)

search = input("Search Name: ")

if search in contacts:
    print(f"Contact Found: {contacts[search]}")
else:
    print("Contact not Found")