#use loop and range

sum=0
for i in range(1,21):
	sum=sum+i
average=sum/20
print(average)


# the other way
import statistics
data=range(1,21)
x= statistics.mean(data)
print(x)
