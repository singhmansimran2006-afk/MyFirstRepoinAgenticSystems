marks = [80, 68, 69, 75, 55, 95, 86, 97]

print("Full List: ", marks)
print("First 3 Marks: ", marks[0:3])
print("Last 3 Marks:", marks[5:])

print("Highest: ",max(marks))
print("Lowest: ",min(marks))

avg = sum(marks) / len(marks)
print("Average: ", avg)