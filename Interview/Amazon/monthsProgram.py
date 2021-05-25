'''
Write the number of days in months program so that the program prompts the user for the file name and reads the dates from the file.

The dates in the file are written in the format dd.mm.yyyy. The program looks for the month in each line (hint: use split) and prints out the number of days in that month.

Rewrite the function so that it does not contain conditional (if) statements for returning the number of days. The function should do it using a list. Do not add the check for a leap year (let’s say that there are 28 days in February).
'''
file = input("Enter file name:")
def fiindmonths(file):
    dates = {}
    monthToDay = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}



    with open("dates.txt", "r") as file:

        for line in file:
            month = line.split(".")[1]


        print(dates,monthToDay[dates])

