# Homework for Fasta	
# Minghao Guo
# April 29, 2020 

###########################################

import math
from Bio import SeqIO

import argparse

#####################################################
#           Arguments    ##
#####################################################
ap = argparse.ArgumentParser()

ap.add_argument("-f","--FASTA",required = True, help="Input the fasta file that you want to analyze")
ap.add_argument("-t","--TAXON",required=True, help="enter the taxon name, in this case, dIul")


args = vars(ap.parse_args())

# Numbers of records in this fasta file
i=0
for record in SeqIO.parse(args["FASTA"],"fasta"): 
		i=i+1
print("There are",i,"records in this fasta file")

# Determine the shortest and longest record. 
lengthlist=[]
for record in SeqIO.parse(args["FASTA"],"fasta"): 
	lengthlist.append(len(record))

print("the shortest length are:",min(lengthlist))
print("the longest length are:",max(lengthlist))

for record in SeqIO.parse(args["FASTA"],"fasta"): 
		if len(record) == min(lengthlist):
			print(record.id,len(record)) 
		if len(record) == max(lengthlist):
			print(record.id,len(record))

# GC content for each record

def gccontent (seq):
	g=seq.count("G")
	c=seq.count("C")
	a=seq.count("A")
	t=seq.count("T")
	gc=(g+c)/(a+t+c+g)
	return gc

gccontentlist=[]
for record in SeqIO.parse(args["FASTA"],"fasta"): 
	gccontentlist.append(gccontent(str(record)))
print(gccontentlist)

############################################################\
#creat a histogram

import numpy as np 
from matplotlib import pyplot as plt

bins=np.arange(0,1,0.05)

fig=plt.hist(gccontentlist,bins=bins)
plt.title("GC-content histogram")
plt.xlabel("GC-content")
plt.ylabel("Frequency")
plt.savefig("GC-content.png")

##################################

# determine which record have most and least GC content

print("The least GC content are", min(gccontentlist))
print("THe most GC content are",max(gccontentlist))

for record in SeqIO.parse(args["FASTA"],"fasta"): 
		if gccontent(str(record))==min(gccontentlist):
			print(record.id,gccontent(str(record)))
		if gccontent(str(record))==max(gccontentlist):
			print(record.id,gccontent(str(record)))

# Translate each record 
for record in SeqIO.parse(args["FASTA"],"fasta"):
		record.translate()

stopcondon=[]
for record in SeqIO.parse(args["FASTA"],"fasta"):
		stopcondon.append(str(record.translate()).count("*"))
print("List of numbers of stop condons for each record are: ",stopcondon)

print("Number of least stop condons is",min(stopcondon))
print("Number of most stop condons is",max(stopcondon))

for record in SeqIO.parse(args["FASTA"],"fasta"):
		if str(record.translate()).count("*")==min(stopcondon):
			print(record.id, min(stopcondon))
		if str(record.translate()).count("*")==max(stopcondon):
			print(record.id,max(stopcondon))
