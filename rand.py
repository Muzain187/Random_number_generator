#Author:Mohmmad Ashraf

import random

rand_number = random.randint(1,10)
chance = 5

while(chance >= 1):
    try:
        guess_number = int(input("\nGuess the Number from 1-10 :"))
        chance -= 1
        if (chance == 0):
            print("Better Luck Next Time")
            print("The Actual number is ", rand_number)
            break
        if(guess_number > 10 or guess_number < 1):
            print("Error: Not Possible\nPlease Enter the value between 1 - 10")
        elif(rand_number == guess_number):
            print("Well Done U won ,congrats")
            break
        elif(guess_number > rand_number):
            print("Try lesser value ")
        elif(guess_number < rand_number):
            print("Try greater value ")

        print("No try again u have ", chance, " chances :")

    except:
        print("Error occured :(")
        print("Unexpected Input ")
        print("Note That u have pressed only Integer value")
