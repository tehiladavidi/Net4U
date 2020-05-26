# תרגיל ראשון:
# מערכת:
# 1. מגרילה חמישה מספרים, במידה והסכום הכולל של כל המספרים הוא זוגי המערכת תדפיס למסך הודעה בהתאם 1-30
# 2. במידה ולא המערכת תחשב את המספר בחזקה של עצמו של הסכום ותדפיס למסך
# 3. עושה הזמנה של פיצות
# 4. קולטת מהמשתמש כמה אנשים יש, יודעת שכל בנאדם אוכל שלוש פיצות. מחשבת כמה פיצות צריך, 8 משולשים כל פיצה. לאחר מכן היא תבצע הזמנה. בהזמנה, כל פיצה תוספת אחרת. אפשריות - בלי כלום, תירס, זיתים, עגבניה
# 5. עלות מגש = 20 שקלים
# 6. הדפסה למסך של ההזמנה פלוס העלות בלי מע״מ ועם מע״מ

import random

num = []
choose = input("Hello! Please choose what you'd like to do. \n1.Enroll Numbers"
               "\n2.Order Pizza")

if choose == 1:
    for i in range(5):
        a = random.randint(1, 30)
        num.append(a)
    result = sum(num)
    print(result)
    if result % 2 == 0:
        print("Your number is Zugi: " + (str(result)))

    else:
        print("The power of your list sum is: " + str(result ** result))

else:
    people = (int(input("How many people will eat Pizza?")))
    pizza = int(people * 3 / 8)
    top = input("Which toppings would you like? we have: \n1.corn \n2.olives \n3.cheese \n4.tomato \n5.empty")
    price = int(pizza * 20)
    fee = int(price * 1.17)
    if top == "1":
        print("You've ordered corn Pizza. The price is: \nWithout fee: " + str(price) + "\nWith fee: " + str(fee))
    elif top == "2":
        print("You've ordered olives Pizza. The price is: \nWithout fee: " + str(price) + "\nWith fee: " + str(fee))
    elif top == "3":
        print("You've ordered cheese Pizza. The price is: \nWithout fee: " + str(price) + "\nWith fee: " + str(fee))
    elif top == "4":
        print("You've ordered tomato Pizza. The price is: \nWithout fee: " + str(price) + "\nWith fee: " + str(fee))
    elif top == "5":
        print("You've ordered empty Pizza. The price is: \nWithout fee: " + str(price) + "\nWith fee: " + str(fee))

