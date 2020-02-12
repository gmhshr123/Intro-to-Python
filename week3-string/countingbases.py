import random
bases=["A","C","T","G"]
sequence=random.choices(bases,k=100)
print(sequence)
numberG=sequence.count("G")
numberA=sequence.count("A")
nubmerC=sequence.count("C")
nubmerT=sequence.count("T")

ACtogether=sequence.count("A")+sequence.count("C")

print("The number of G is ", numberG)
print("The number of A is", numberA)
print("The total number of A and C is", ACtogether)