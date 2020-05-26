import csv


def fatal_hotel():
    fatal = "/Users/tehilad/Desktop/fatal.csv"
    price = {'Couple': '200$', 'Couple with breakfast': '250$', 'Three people': '350$',
             'Three people with breakfast': '420$'}
    rooms = open("fatal.csv", "w")
    w = csv.writer(rooms)
    for key, val in price.items():
        w.writerow([key, val])
    rooms.close()

    print("These are the rooms that are available for you: ")
    with open('fatal.csv', newline='') as price:
        reader = csv.reader(price)
        for row in reader:
            print("Room type: " + '  \nPrice: '.join(row))

    rooms.close()


fatal_hotel()


def isrotel_hotel():
    isrotel = "/Users/tehilad/Desktop/isrotel.csv"
    price = {'Single': '100$', 'Couple without breakfast': '170$', 'Couple with breakfast': '200$',
             'Three people without breakfast': '380$', 'Four people without breakfast': '450$',
             'Four people with breakfast': '550$'}

    rooms = open("isrotel.csv", "w")

    w = csv.writer(rooms)
    for key, val in price.items():
        w.writerow([key, val])
    rooms.close()

    print("These are the rooms that are available for you: ")
    with open('isrotel.csv', newline='') as price:
        reader = csv.reader(price)
        for row in reader:
            print("Room type: " + ' \nPrice: '.join(row))

    rooms.close()


isrotel_hotel()

