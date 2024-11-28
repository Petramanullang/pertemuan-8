# Rp. 1.000.000, interest 2% / month.
# After 1 month -> from Rp. 1.000.000 to Rp. 1.020.000
# After 2 month -> from Rp. 1.020.000 to Rp. 1.040.400

import os

os.system('clear')

month = int(input("How Many Months : "))

starting_money = 1000000

print("=======================================================")
print(f"{("Month").ljust(8)} | {("Starting Money").ljust(15)} | {("Interest").ljust(15)} | {("Total").ljust(15)}")

for i in range(0, month):
    print("{:>3}".format(i + 1), end="")
    print("{:17,.0f}".format(starting_money), end="")
    interest = 0.02 * starting_money
    print("{:15,.0f}".format(interest), end="")
    starting_money = starting_money + interest
    print("{:20,.0f}".format(starting_money))
print("=======================================================")
print()
print("Final Amount Of Savings = Rp. {:10,.2f}".format(starting_money))
print()