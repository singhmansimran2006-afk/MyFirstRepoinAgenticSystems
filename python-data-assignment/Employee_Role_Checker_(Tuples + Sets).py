employee = (1, "Mansimran", "HR")
roles = {"Admin", "Editor", "Viewer"}

print("Employee Details: ")
print("ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])

if "Admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")