# start condon 
# Minghao Guo	
# April 1

#import random module
import random

#randomly generate a sequence

def sequence(length):

       mrna=""
       for count in range(length):
          mrna+=random.choice("CGUA")
       return mrna
	 
seq=str(sequence(1000))

#print out the sequence 
print("The randomly generated sequence are:\n",seq)

#split the mRNA sequence with "AUG"
separate = seq.split("AUG")

#print out the list list of genes separated by start codon
print("List of genes that are separated by start codon:\n",separate)

#create a largegene list

largegene=[element for element in separate if len(str(element))>50]

# print out a list only contain gene length larger than 50
print("The list of large genes are:\n", largegene[1:])

print("The length of big genes are:")	
for x in largegene[1:]:
		print(len(x))





