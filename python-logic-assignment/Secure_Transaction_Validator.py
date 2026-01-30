balance = int(input("Enter your Account Balance: "))
withdraw = int(input("Enter your withdrawl amount: "))
status = (input("Enter Verification Status, True/False: "))

status = status == "True"

if withdraw <= balance and status:
    print("Transaction Successful")
else:
    print("Transaction Denied")