import math


def maths_calculator():
    def again_maths():
        print("Do you wanna exit or quit (yes/no)")
        gid = input("> ").lower().strip()
        if (gid == 'n') or (gid == "no"):
            maths_calculator()
        elif (gid == 'y') or (gid == "yes"):
            print("Hope to see you again")
        else:
            print("I don't know that")
            again_maths()
    try:
        print("Welcome to Maths Mania")
        print('\n')
        print("""Pls specify us what you wanna do:
1)Square finder
    
2)Square root finder
    
3)Cube finder
    
4)Cube root finder
    
5)Calculator 

6)Quit  (you can also write numbers in place of full sentence)
""")
        user_input = input("> ").lower().strip()
        if (user_input == "square finder") or \
                (user_input == '1'):
            print("Please enter your number below")
            number = int(input("> "))
            square = pow(number, 2)
            print(f"square of {number} is {square}")
        elif (user_input == "square root finder") or \
                (user_input == '2'):
            print("Please enter your number below")
            number_root = int(input("> "))
            square_root = math.sqrt(number_root)
            print(f"Square root of {number_root} is {square_root}")
        elif (user_input == "3") or \
                (user_input == "cube finder"):
            print("Please enter your number below")
            number_cube = int(input("> "))
            cube = pow(number_cube, 3)
            print(f"Cube of {number_cube} is {cube}")
        elif (user_input == "4") or (
                user_input == "cube root finder"):
            print("Please enter your number below")
            number_cube_root = int(input("> "))
            cube_root = (number_cube_root ** (1 / 3)).__round__()
            print(f"Cube root of {number_cube_root} is {cube_root}")
        elif (user_input == "5") or (user_input == "calculator"):
            try:
                print("Hi I am the Most Modified Calculator")
                y = input("Please write your number here with operations:   ").strip()
                print(f"Your number is {eval(y)}")
                print("Thank you for using Most Modified Calculator")
                print("\n")
            except SyntaxError:
                print("You have entered a wrong or an invalid operator")
        elif (user_input == "quit") or (user_input == "6"):
            again_maths()
        else:
            print("I don't know that")
        again_maths()
    except ValueError:
        print("You have entered words instead of numbers.")


maths_calculator()
