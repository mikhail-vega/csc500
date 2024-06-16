def multiply_divide(num_1, num_2):
    multi_answer = num_1 * num_2
    div_answer = num_1/num_2
    return multi_answer, div_answer

def add_subtract(num_1, num_2):
    add_answer = num_1 + num_2
    sub_answer = num_1 - num_2
    return add_answer, sub_answer

while True:
    try:
        print("Select 1 for addition/subtract. Select 2 for multiplication/division.")
        prompt = int(input("Please select your choice: "))
    except ValueError:
        print("Incorrect input - please input a valid response")
    else:
        if prompt not in [1,2]:
            print("Please select 1 or 2")
            continue
        else:
            break

while True:
    try:
        print("Please input 2 numbers (The 1st number will be the dividend for division, the minuend for subtraction)")
        num_1 = int(input("Number 1: "))
        num_2 = int(input("Number 2: "))
    except ValueError:
        print("Incorrect input - please input valid numbers.")
    else:
        break

if prompt == 1:
    addition, subtraction = add_subtract(num_1 ,num_2)
    print(f'{num_1} + {num_2} = {addition}; {num_2} - {num_1} = {subtraction}')
else:
    multiplication, division = multiply_divide(num_1, num_2)
    print(f'{num_1} * {num_2} = {multiplication}; {num_1}/{num_2} = {division}')