# bedfiles
# Practice with Argparse
# Minghao Guo
# April 22th , 2020

##########################################

# import pandas module

import pandas as pd 
import argparse

#####################################################
#           Arguments    ##
#####################################################

ap = argparse.ArgumentParser()

ap.add_argument("-r","--READ",  help="put the file that you want to read")
ap.add_argument("-f","--FAMILY", help="indicate a family")
ap.add_argument("-g","--GENOME",type=int, help="Enter the genome size")

args = vars(ap.parse_args())

# read file 

# create columns names

fields = ["scaffold","start","stop","element","score","strand","family","sub-family","divergence"]

# read the file and add the column names to this file, sep with \t. 

te = pd.read_csv(args["READ"], names = fields, sep="\t")
# get unique family names

family_name = str(te.family.unique())

print("Families: ", family_name)

# create a new dataframe that only for SINE family

sine = te.loc[te["family"] == args["FAMILY"]]

# Drop columns “Strand” and “Score”

newsine = sine.drop(["strand","score"], axis = 1)

# Ceate new column "length"

newsine["length"] = newsine["stop"] - newsine["start"]

###

#create new column proportion which is Length/genome size 
newsine["proportion"] = newsine["length"]/args["GENOME"]

# Determine min, max and mean for all SINEs

minsine = newsine["length"].min()

print ("The minimum value of length is :" , minsine)

maxsine = newsine["length"].max()

print ("The maxium value of lenght is :", maxsine)

meansine = newsine["length"].mean()

print ("The mean value of length is :", meansine)


# Determine min, max and mean for all subfamilies
# remove extra information

minsub = str(newsine.groupby("sub-family")["length"].min())

minsub = minsub.replace("Name: length, dtype: int64","")

print("The minimum lenght value for each sub-family is: \n",minsub)

maxsub = str(newsine.groupby("sub-family")["length"].max())

maxsub = maxsub.replace("Name: length, dtype: int64","")

print("The maxium lenght value for each sub-family is : \n", maxsub)

meansub = str(newsine.groupby("sub-family")["length"].mean())

meansub = meansub.replace("Name: length, dtype: float64","")

print("The mean lenght value for each sub-family is : \n", meansub)



################################################
#  save the SINEs dataframe as "aVan.csv"
newsine.to_csv("aVan.csv")