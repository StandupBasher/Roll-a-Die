import random

import time

def main():

    min = 1

    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":

        print("Rolling the dice...")

        time.sleep(1)
        
        print("The values are....")

        print(random.randint(min, max))

        #Rolls die

        roll_again = input("Roll the dice again?")

    if roll_again == "yes" or roll_again == "y":
        
        main()
    else:
        exit()
        #Ask user if they want to roll again.
main()
