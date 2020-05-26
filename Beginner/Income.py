from money.money import Money
from money.currency import Currency
e=Money('3.88' ,Currency.EUR)

from money.money import Money
from money.currency import Currency
d=Money('3.47' ,Currency.USD)

gerapt=int(500)
israpt=int(3000)
virtcoin=int(2)

print ("Hi Ben! this program will calculate your total income from your apartments and virtual coins")
g=int(input( ("Please specifiy the months you own your apartment in Germany")))
c=int(input("Please specify how many virtual coins you own"))
i=int(input( ("Please specifiy the months you own your apartment in Israel")))


z=(g*gerapt/e.amount) + (c*virtcoin/d.amount) + (i*3000)
print ("Your total income is: " + "%.2f" %z)


