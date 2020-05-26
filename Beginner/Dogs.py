print("Welcome to dogshop!")
husk=int(input ("How many Huskey dogs you'd like to buy? "))
hage= int(input ("What age would you like your Huskey?"))
rott=int(input ("How many Rottweilers dogs you'd like to buy? "))
rage= int(input ("What age would you like your Rottweiler?"))
pinch=int(input ("How many Pinchers dogs you'd like to buy? "))
page= int(input ("What age would you like your Pincher?"))

print("Dogs in total: " + str(husk + rott + pinch))
price= ((husk*300) + (rott*200) +(pinch*100))
print ("Bill Summery: " + str(int(price)))

print ("The average age of the dogs in human life: " + str("%.2f" %(hage+rage+page/3 *7)))

