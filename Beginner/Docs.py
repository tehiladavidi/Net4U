from Beginner.Doctors import *

idan = doctors("Eyes", "Haifa", "Sunday", ["14:00","15:00","16:00","17:00"])
amit = doctors("Hands", "Holon", "Monday", "[14:00]")

person = input("Hi, to which doctor you'd like to schedule an appointment?"
               "\nWe have Idan and Amit to your service")
if person == "idan":
    idan.print_details()
    idan.schedule()
else:
    amit.print_details()
    amit.schedule()



