def add(a, b):
    answer = a + b
    print(str(a) + " + " + str( b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b ) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

# these are the functions with the user options to add,multiply,subtract or divide

while True:
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")
    choice = input("input your choice: ")

    #while Loop used to keep the loop running

    if choice == "a" or choice == "A": #either lowercase a or uppercase A will be accepted using this if statement
        print("Addition")
        a = int(input("Please input your first number: ")) #we then print a user input request to ask the user to give us the two numbers to add
        b = int(input("Please input your second number"))
        add(a, b) # we run the function here that we established before

    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Please input your first number"))
        b = int(input("Please input your second number"))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Please input your first number"))
        b = int(input("Please input your second number"))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Division" )
        a = int(input("Please input your first number"))
        b = int(input("Please input your second number"))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("Thank You for Using My Calculator!!")
        quit()