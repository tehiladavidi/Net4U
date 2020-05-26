#
# קליטה מהמשתמש חמישה שמות מלאים עם גילאים ומספרי טלפון ולשמור בתוך קובץ
# לאחר מכן, יקלוט שם חדש ותהיה בדיקה אם השם נמצא בקובץ או לא
#
# אם השם בקובץ, להדפיס למסך שהשם קיים
# ולהדפיס בצורה יפה את השם, גיל ומס טלפון של כל הרשימות
#
# אם הוא לא נמצא להוסיף עם גיל ומס
filename = "/Users/tehilad/Desktop/name.txt"
file = open(filename, "a")

for i in range(5):
    name = (input("Enter your full name"))
    age = (input("Enter your age"))
    phone = (input("Enter your phone number"))
    file.write(name)
    file.write(age)
    file.write(phone)

new_name = input("Enter a new name")
file = open(filename, "r")
line = file.readline()
for line in file:
    if new_name in file:
        print("This name is already exist")
else:
    age = (input("Enter your age"))
    phone = (input("Enter your phone number"))
    file = open(filename, "a")
    file.write(age + phone)
    file.close()



