list = (3, 7, 8, -1, -2, -4, 3, 2)
total =0
for n in list:
    if n < 0:
        continue
    if n > 0:
        print (n)
    total = total + n
print("Sum pf positive numbers is ", total)