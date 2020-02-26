#Restriction enzyme
#calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI
# Minghao Guo
# Feb 26, 2020

###################################
#Basic Steps
###################################

# 1. Find the restriction enzyme cut site
# 2. count the size of the two fragments

# load the sequence 
seq = ("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT")

# find the restriciton enzyme site

cut_site = seq.find("GAATTC")

# get the total length of the sequence 

totalnum = len(seq)

# fragment 1 size
fragment1 = cut_site + 1
# fragment 2 size
fragment2 = totalnum - fragment1

print("The first fragement size is ", fragment1, "\n" , "The second fragment size is ", fragment2)

