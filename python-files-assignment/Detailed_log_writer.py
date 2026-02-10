numbers = []

with open("numbers.txt", "r") as file:
    for integer in file:
        numbers.append(int(integer.strip()))

total = len(numbers)
add = sum(numbers)
avg = add / total

with open("results.log", "a") as file:
    file.write("File Opened Successfully\n")
    file.write(f"Read {total} Numbers\n")
    file.write(f"Sum: {add}\n")
    file.write(f"Average: {avg}\n")
    file.write("Process Completed\n")
    file.write("\n") # i added this line to make space between 2 logs to seperate them so its easily readable and differentiable