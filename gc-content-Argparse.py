# Homework for Argparse
# Minghao Guo	
# April 22, 2020 


#import random module
import random
import argparse

#####################################################
#           Arguments    ##
#####################################################

ap = argparse.ArgumentParser()

ap.add_argument("-l","--LENGTH", type=int, help="enter the length of the whole sequence")
ap.add_argument("-c","--CHUNK", type=int, help="enter the chunk size of samller sequence")

args = vars(ap.parse_args())



#randomly generate a sequence

def sequence(length):
	dna=""
	for count in range(length):
		dna+=random.choice("ATCG")
	return dna

seq=str(sequence(args["LENGTH"]))

print("The sequence randomly generated shows as below:\n",seq)

# break the sequence into smaller sequences 

# split the seuence by input chunk-size 

smallerseq=[seq[i:i+args["CHUNK"]] for i in range(0,args["LENGTH"],args["CHUNK"])]

print("List of smaller sequence are:",smallerseq)

# Calculate the CG content for each smaller sequence 

# define a function that calculate the GC content	
def gccontent(smaller):
		g=smaller.count("G")
		c=smaller.count("C")
		gc=(g+c)/args["CHUNK"]
		return gc

# Use list comprehension to generate a list that calculate the GC content for each samller sequence
gccontentlist=[gccontent(element) for element in smallerseq]

print("the GC content for each samller sequence re:",gccontentlist)

############################################################\
#creat a histogram

import numpy 
import matplotlib.pyplot as plt

fig=plt.hist(gccontentlist)
plt.title("GC-content histogram")
plt.xlabel("GC-content")
plt.ylabel("Frequency")
plt.savefig("GC-content.png")