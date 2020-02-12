#Input your three bat species

bat1=input("type your bat species 1:")
bat2=input("type your bat species 2:")
bat3=input("type your bat species 3:")

#covert to a new string with first three letters
newbat1=bat1[0:3]+bat1[(bat1.find(" ")):(bat1.find(" ")+4)]
newbat2=bat2[0:3]+bat2[(bat2.find(" ")):(bat2.find(" ")+4)]
newbat3=bat3[0:3]+bat3[(bat3.find(" ")):(bat3.find(" ")+4)]

# replace the space 
spacebat1=newbat1.replace(" ","")
spacebat2=newbat2.replace(" ","")
spacebat3=newbat3.replace(" ","")

#upper the letter
upperbat1=spacebat1.upper()
upperbat2=spacebat2.upper()
upperbat3=spacebat3.upper()

#print out with different line 
print(upperbat1,upperbat2,upperbat3,sep="\n")
