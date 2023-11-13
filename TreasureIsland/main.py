#print("Let's write a simple program which tells us whether the integer value entered is odd or even")
#value = int(input("Enter the integer value: "))
#odd_even = value % 2
#if odd_even == 1:
#    print(f"The value, {value}, is odd")
#else:
#    print(f"The value, {value}, is even")

#weight = float(input("Please enter your weight: "))
#height = float(input("Please enter your height: "))
#BMI = round(weight / height**2, 2)
#if BMI < 18.5:
#    print(f"BMI: {BMI}, you are underweight.")
#elif BMI < 25:
#    print(f"BMI: {BMI}, you are normal weight.")
#elif BMI < 30:
#    print(f"BMI: {BMI}, you are overweight.")
#elif BMI < 35:
#    print(f"BMI: {BMI}, you are obese.")
#else:
#    print(f"BMI: {BMI}, you are clinically obese.")

#print("Let's calculate your compatibility with your partner")
#my_name = str(input("Enter your name: ")).lower()
#lover_name = str(input("Enter your partner's name: ")).lower() #to make the capital case letters lower letters

#true_count_my = my_name.count("t") + my_name.count("r") + my_name.count("u") + my_name.count("e")
#true_count_partner = lover_name.count("t") + lover_name.count("r") + lover_name.count("u") + lover_name.count("e")
#true_count = true_count_my + true_count_partner

#love_count_my = my_name.count("l") + my_name.count("o") + my_name.count("v") + my_name.count("e")
#love_count_partner = lover_name.count("l") + lover_name.count("o") + lover_name.count("v") + lover_name.count("e")
#love_count = love_count_my + love_count_partner

#percentage = str(true_count) + str(love_count)

#if int(percentage) > 90 or int(percentage) < 10:
#    print("You were meant for each other")
#elif int(percentage) > 70:
#    print("You are really for each other")
#elif int(percentage) > 50:
#    print("There is nothing stopping you from being with each other")
#else:
#    print(f"You are {percentage} percent compatible with your partner")



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are standing at a crossroads, you need to pick your path, will you go left or right: ")
if direction == "left":
    swim = input("There is a lake in your way and you need to cross it, will you swim or look around: ")
    if swim == "look":
        print("While looking around, you found yourself a boat and crossed the lake safely")
        print("As you disembarked your boat, you got yourself in front of three doors")
        door = input("Each door is coloured differently, one is red, one is yellow, the other is blue, which one do you want to open: ")
        if door == "red":
            print("You opened the door and a sudden burst of flame from the inside engulfed you and burned you to crisp, game over :(")
        elif door == "yellow":
            print("The door contains a treasure so bright, it could burn your eyes, you've done it, the treasure is yours")
        else:
            print("You died of natural causes, game over :(")

    else:
        print("There were man eating piranhas in the lake, you got eaton, game over :(")
else:
    print("You went in the wrong direction and could not find anything, game over :(")



