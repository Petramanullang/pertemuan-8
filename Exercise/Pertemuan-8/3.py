# Rp. 1.000.000, interest 2% / month.
# After 1 month -> from Rp. 1.000.000 to Rp. 1.020.000
# After 2 month -> from Rp. 1.020.000 to Rp. 1.040.400

month = int(input("How Many Months : "))

starting_money = 1000000

for i in range(0, month):
    interest = 0.02 * starting_money
    starting_money = starting_money + interest
    print("Rp.","{:0,.2f}".format(starting_money))