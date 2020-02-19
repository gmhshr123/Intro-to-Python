#import a random module
import random

name=input("what's your name?:")

yourchoice=input("hello, "+ name+ ", choose from rock,paper,scissors:")

com_choice_set=["rock","paper","scissors"]
com_choice=random.choice(com_choice_set)

print("computer chooses "+ com_choice)

if yourchoice=="rock":
	if com_choice=="scissors":
		print("you win!")
	elif com_choice=="paper":
		print("you loose!")
	else:
		print("tie!")

if yourchoice=="paper":
	if com_choice=="scissors":
		print("you loose!")
	elif com_choice=="rock":
		print("you win!")
	else:
		print("tie!")


if yourchoice=="scissors":
	if com_choice=="paper":
		print("you win!")
	elif com_choice=="rock":
		print("you losse!")
	else:
		print("tie!")

