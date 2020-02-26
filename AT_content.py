# AT content
# Minghao Guo
# Feb 26, 2020

###################################
#Basic Steps
###################################

# 1.count the number of A 
# 2.count the number of T
# 3.add the number of A and T together and get the content


seq = ("ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT")

# print out the sequence for users
print("The sequence is ",seq)

#count the number of A

numA = seq.count("A")

#count the number of T
numT = seq.count("T")

# add the total number of As and Ts
numAT= numA + numT

# count the total length of this sequence
totalnum = len(seq)

# calculate the AT content
ATcontent = numAT/totalnum

# Print out the AT content 
print("AT content of this sequence is ", ATcontent)