total = 0

while True:
    number = int(input("Enter a number to add: "))
    if number == 0:
        break
    total += number
print("Total: ", total)