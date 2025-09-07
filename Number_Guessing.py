#Program for Guessing Number
import random as rd
import sys
if len(sys.argv)!=2:
    print("Please Enter Number Between 1 to 10 as Argument!")
try:
    num=int(sys.argv[1]) #Using Compile time Value
except ValueError:
    print("Please Enter Numbers ")
numbers=[n for n in range (1,11)]
random_num=rd.choice(numbers)
if(num<1 or num>10):
    print("Enter Number Between 1 to 10")
else:
    if(num==random_num):
        print("Conguratulatiton You Guessed Correctly!!!")
        print("Thanks for Visiting !")
    elif (num>random_num):
        print("It's Too High")
    else:
        print("It's Too Low")


