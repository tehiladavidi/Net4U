class doctors:
    def __init__(self, prof, city, days, hours):
        self.prof = prof
        self.city = city
        self.days = days
        self.hours = hours

    def print_details(self):
        print("Specializes in: " + self.prof + "\nWorks at: " + self.city + "\nOn days: " + self.days + ""
              "\nWhich Hours: " + str(','.join(self.hours)))

    def schedule(self):
        while True:
            sch = input("please choose an hour from: " + str(','.join(self.hours)))
            if sch in self.hours:
                self.hours.remove(sch)
                print("Your appointment is scheduled to " + sch)
                break
            else:
                print("Please choose a valid hour!")
                continue

