# Guess_the_number
# User guess a number randomly chosen by computer
# Minghao Guo
# Feb 26, 2020

##################################
#Basic steps
##################################
# 1. Computer randomly choose a number 
# 2. User guess a number
# 3. Compare the user's number and computer's number
# 4. Print to tell the user if it's high or low
# 5. let users try again until user get the right answer

#import a module
import random

# computer randomly choose an integer between 1 to 100

com_choice = random.randint(1,100)

# user input a integer in that range

user_num = int(input("Guess a number between 1 to 100:"))

# start a loop, while users cannot guess the number, ask user to input again, until user guess the number

while user_num != com_choice:
	if user_num > com_choice:
		print(" your choice is higher")
	elif user_num < com_choice:
		print(" your choice is lower")
	user_num=int(input("Guess again!:"))

print(" you got it! ")
