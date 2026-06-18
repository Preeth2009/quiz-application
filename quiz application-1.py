def start():

    s = 0

    print("Question 1:")
    print("What is the capital of India?")
    print()
    print("1. Chennai")
    print("2. Mumbai")
    print("3. New Delhi")
    print("4. Kolkata")
    print()

    a = int(input("Enter answer: "))
    if a == 3:
        print("Correct!")
        s += 1
    else:
        print("Incorrect! Correct answer is 3")

    print()

    print("Question 2:")
    print("Which keyword is used to create a function in Python?")
    print()
    print("1. function")
    print("2. define")
    print("3. def")
    print("4. fun")
    print()

    a = int(input("Enter answer: "))
    if a == 3:
        print("Correct!")
        s += 1
    else:
        print("Incorrect! Correct answer is 3")

    print()

    print("Question 3:")
    print("Which data type is used to store multiple values in square brackets []?")
    print()
    print("1. Tuple")
    print("2. List")
    print("3. Dictionary")
    print("4. String")
    print()

    a = int(input("Enter answer: "))
    if a == 2:
        print("Correct!")
        s += 1
    else:
        print("Incorrect! Correct answer is 2")

    print()

    print("Question 4:")
    print("What is the output of:")
    print("print(5 + 3)")
    print()
    print("1. 53")
    print("2. 8")
    print("3. 15")
    print("4. Error")
    print()

    a = int(input("Enter answer: "))
    if a == 2:
        print("Correct!")
        s += 1
    else:
        print("Incorrect! Correct answer is 2")

    print()

    print("Question 5:")
    print("Which loop is used when we want to repeat a block of code multiple times?")
    print()
    print("1. if")
    print("2. def")
    print("3. while")
    print("4. class")
    print()

    a = int(input("Enter answer: "))
    if a == 3:
        print("Correct!")
        s += 1
    else:
        print("Incorrect! Correct answer is 3")

    print()
    print("Final Score:", s, "/5")
    print("Percentage:", (s / 5) * 100, "%")

    return s


def view(c):
    if c == -1:
        print("No quiz attempted yet.")
    else:
        print("Last Score:", c, "/5")


def exi():
    print("Thank you for using Quiz Application")


c = -1

while True:

    print("===== Quiz Application =====")
    print()
    print("1. Start Quiz")
    print("2. View Score")
    print("3. Exit")
    print()

    b = int(input("Enter choice: "))

    if b == 1:
        c = start()

    elif b == 2:
        view(c)

    elif b == 3:
        exi()
        break

    else:
        print("Enter valid choice.")
