users = [{"name" : "Mansimran", "scores" : [85, 95, 75, 89], "roles" : {"Editor", "Admin"}},
         {"name" : "Diya", "scores" : [94, 97, 65, 79], "roles" : {"Viewer", "Writer"}}]

def user(users):
    averages = []

    for i in users:
        score = i["scores"]
        avg = sum(score) / len(score)
        averages.append((i["name"],avg))

    return averages


def access(roles):
        if "Admin" in roles:
            return True

def main():
    averages = user(users)
    for u in users:
        name =  u["name"]
        scores = u["scores"]
        roles = u["roles"]

        avg = sum(scores) / len(scores)
        admin = access(roles)
    
        print("Name:", name)
        print("Average Score:", avg)
        print("Admin Access:", "True" if admin else "False")

main()