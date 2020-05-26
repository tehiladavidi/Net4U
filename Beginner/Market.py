tom=int(input ("How many Tomatoes you want? "))
cuc=int(input ("How many cucumbers you want? "))
cola=int(input ("How many colas you want? "))
chick=int(input ("How much chicken you want? "))

sum=(tom *3) + (cuc *2) + (cola *5) + (chick *20)
print("Sum withot fee:" + str(sum))
print ("sum with fee:" +str("%.2f" % (sum*1.17)))
