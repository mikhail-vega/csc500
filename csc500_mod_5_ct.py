def calculate_rainfail():
    import calendar
    
    MONTHS = list(calendar.month_name[1:])

    while True:
        try:
            years = int(input("Please input number of years: "))
        except ValueError:
            print("Incorrect input - please input a valid integer")
        else:
            break

    total_months = years * len(MONTHS)
    total_rainfall = 0

    for year in range(1,(years + 1)):
        print(f"Enter rainfall for year {year}")
        for month in MONTHS:
            while True:
                try:
                    rainfall = float(input(f"Please input the number of inches of rainfall for the month of {month}: "))
                except ValueError:
                    print("Incorrect input - please input a valid float")
                else:
                    total_rainfall += rainfall
                    break
        print()
    
    print(f"Number of Months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall(inches) per month: {total_rainfall/total_months}")

    return

def calculate_rewards():
    while True:
        try:
            books = int(input("Please input number of books purchases this month: "))
        except ValueError:
            print("Incorrect input - please input a valid integer")
        else:
            if books < 0:
                print("Please enter 0 or more books")
            else:
                break
    
    points = None

    if books == 0:
        points = 0
    elif books <= 3:
        points = 5
    elif books <= 5:
        points = 15
    elif books <= 7:
        points = 30
    else:
        points = 60
    
    print(f"You have earned {points} points.")
    
    return


if __name__ == '__main__':

    while True:
        try:
            print("\nInput 1 to calculate rainfall (Part 1)")
            print("Input 2 to calculate reward points at CSU Global Bookstore (Part 2)")
            print("Input 3 to exit program\n")

            selection = int(input("Please input your choice: "))
        except ValueError:
            print("Incorrect input - please input a valid response")
        else:
            print()
            match selection:
                case 1:
                    calculate_rainfail()
                case 2:
                    calculate_rewards()
                case 3:
                    break
                case _:
                    print("Please input a valid selction\n")
