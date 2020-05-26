a=9876
print("The tho num is " + str(int(a/1000)))
print ("The hun num is " + str(int(a%1000 / 100)))
print ("The ten num is " + str(int(a%1000 %100 /10)))
print ("The unit num is "+ str(int(a%1000 %100 %10)))