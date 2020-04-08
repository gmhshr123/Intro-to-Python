# Practice with loop and list comprehension
# Minghao Guo 
# April 8, 2020

# Creat the list 
mylist = "The quick brown fox jumped over the lazy dog"

print(mylist)
#################################################################################
# Count the number of spaces in the list
# with loop

countspace1 = 0
for letter in str(mylist):
		if letter.isspace():
			countspace1=countspace1+1
print("Using the loop, the number of space is: ",countspace1)

# with list comprehension

countspace2 = 0

comprehension1= [letter for letter in str(mylist) if letter.isspace()] 
print("Using the list comprehension, the number of space is: ",len(comprehension1))

###################################################################################
# Find all the words that have the letter “o” in the above string  
# Creat a newlist with all the word separate
newlist = mylist.split(" ")
print(newlist)

# with loop

letter_o1=[]

for element in newlist:
		if element.find("o")!= -1: 
			letter_o1.append(element)

print("Using the loop, all the words that have the letter o are: ",letter_o1)

# with list comprehension

letter_o2 = [element for element in newlist if element.find("o")!=-1]

print("Using list comprehension, all the words that have the letter o are :",letter_o2)

###################################################################################
#Find all the words that have at least 5 letters in the above string

letter51=[]

for element in newlist:
		if len(str(element))>4:
			letter51.append(element)

print("Using the loop, all the words that have at least 5 letters :",letter51)

letter52 = [element for element in newlist if len(str(element))>4]

print("Using list comprehension, all the words that have at leastr 5 letters",letter52)

###################################################################################
#Find all the numbers from 1 to 1000 that have a “3” in it. Ex: 23, 37, 903
# with loop
thousands1 = []

for element in range(1,1001):
		if str(element).find("3") != -1:
			thousands1.append(element)
print("Using loop,", thousands1)

# with list comprehension

thousands2 = [element for element in range(1,1001) if str(element).find("3")!= -1 ]

print("Using list comprehension", thousands2)