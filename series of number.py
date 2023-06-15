total = 0
while True:
    print("Enter another positive value if you wish to continue. Enter a negative number to calculate the sum.")
    number = int(input("Enter a number: "))
    if number >= 0: 
        total += number
    else:
        break
print("The sum is", total)