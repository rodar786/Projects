import random

again = True

while again:
    print(random.randint(1,6))
    another_roll = input("Do you Want To Roll Again? (y/n): ")
    if another_roll.lower() == "y":
        continue
    else:
        print ("Thanks for Playing!!!")
        break