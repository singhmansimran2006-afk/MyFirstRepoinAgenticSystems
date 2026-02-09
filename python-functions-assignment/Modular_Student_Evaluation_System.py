def names(name):
    return f"Hello, {name}"



def subjects(scores):
    subject = len(scores)
    avg = sum(scores) / subject
    return subject, avg



def results(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    

def main():
    student = input("Enter Name: ")
    scores = [50, 85, 90, 65]

    greetings = names(student)
    subject , average = subjects(scores)
    result = results(average)

    print(greetings)
    print(f"Number of Subjects: {subject}")
    print(f"Average Score: {average}")
    print(f"Result: {result}")

main()