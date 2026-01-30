age = int(input("Enter your Age: "))
has_id = (input("Do you have ID? True/False: "))

has_id = has_id == "True"

if age >= 18 and has_id:
    print("Entry Allowed")