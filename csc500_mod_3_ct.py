def calculate_restaurant_meal() -> float:
    while True:
        try:
            amount = float(input("Please input the total amount at the restaurant: "))
        except ValueError:
            print("Incorrect input - please input a valid response")
        else:
            break

    tax = amount * .07
    tip = amount * .18

    print(f"Amount: {amount:.2f}")
    print(f"   Tip: {tip:.2f}")
    print(f"   Tax: {tax:.2f}")
    print(f" Total: {(amount + tax + tip):.2f}")
    
    return

def calculate_military_time():
    while True:
        try:
            print("Please enter military hour ie 1 (1 AM), 13 (1 PM)")
            military_hour = int(input("Current hour: "))
        except ValueError:
            print("Incorrect input - please input a valid number")
        else:
            if 0 > military_hour > 23:
                print("Military time must be between 0-23")
                continue
            else:
                break

    while True:
        try:
            print("Please enter how many hours till alarm")
            hours = int(input("Hours: "))
        except ValueError:
            print("Incorrect input - please input a valid number")
        else:
            if 0 > hours:
                print("Please input a postive number")
                continue
            else:
                break
    
    while hours > 23:
        hours -= 24
    
    for _ in range(hours):
        if military_hour == 23:
            military_hour = 0
        else:
            military_hour +=1
    
    return print(f"Alarm will go off at {military_hour}:00")


calculate_restaurant_meal()
calculate_military_time()