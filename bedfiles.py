# bedfiles
# Manipulate with the bedfile data
# Minghao Guo
# March 4th , 2020

##########################################

# import pandas module

import pandas as pd 

# read file 

# create columns names

fields = ["scaffold","start","stop","element","score","strand","family","sub-family","divergence"]

# read the file and add the column names to this file, sep with \t. 
te = pd.read_csv("aVan_rm.bed", names = fields, sep="\t")

# get unique family names

family_name = str(te.family.unique())

print("Families: ", family_name)


# create a new dataframe that only for SINE family

sine = te.loc[te["family"] == "SINE"]

# Drop columns “Strand” and “Score”

newsine = sine.drop(["strand","score"], axis = 1)

# Ceate new column "length"

newsine["length"] = newsine["stop"] - newsine["start"]

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

