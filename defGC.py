# Homework for function
# Minghao Guo	
# April 15, 2020 


#import random module
import random

#randomly generate a sequence
a
def sequence(length):c
	dna=""
	for count in range(length):
		dna+=random.choice("ATCG")
	return dna

seq=str(sequence(5000))

print("The sequence randomly generated shows as below:\n",seq)

# break the sequence into smaller sequences 100bp long

# split the seuence by 100 chunk-size 

smallerseq=[seq[i:i+100] for i in range(0,5000,100)]

print("List of smaller sequence are:",smallerseq)

# Calculate the CG content for each smaller sequence 

# define a function that calculate the GC content	
def gccontent(smaller):
		g=smaller.count("G")
		c=smaller.count("C")
		gc=(g+c)/100
		return gc

# Use list comprehension to generate a list that calculate the GC content for each samller sequence
gccontentlist=[gccontent(element) for element in smallerseq]

print("the GC content for each samller sequence re:",gcontentlist)