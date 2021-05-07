######################################
# Engineer Gaming Username Generator #
#                                    #
# Authors:                           #
# Engineer Gaming                    #
# Laranc                             #
# Engineer Gaming                    #
# Engineer Gaming                    #
# Engineer Gaming                    #
# Engineer Gaming                    #
#                                    #
# Last Modified:                     #
# Fri 7 May 2021                     #
######################################

import random # this imports random

gaming = "engineer gaming"

print("So it's time for you to join us? Good. A random username will generate, try it and if it's taken then select try again. if it isn't taken then leave getouttahere.") # <- user input
while(True):
    engineergaming = ""
    for engineer in gaming:
        dispenser = random.randint(0,1)
        if dispenser == 1:
            engineergaming += engineer.upper()
        else:
            engineergaming += engineer.lower()
    print(engineergaming)
    engineergamer = input("     Try again? y/n") # sonetimes you just need a little less gun
    if engineergamer == "n" or engineergamer == "N":
        print("Bye, bye")
        break; # me please