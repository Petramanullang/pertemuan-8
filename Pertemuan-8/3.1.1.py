# Meminjam Rp.1.000.000 dengan bunga 2%
# Bulan Pertama -> Rp.1.000.000 + (Rp.1.000.000 * 2%) = Rp.1.000.000 + Rp.20.000 = Rp.1.020.000
# Rp.1.020.000 - (Rp.1.020.000 * 10%) = Rp.1.020.000 - Rp.102.000 = Rp.918.000
# Pada bulan kedua -> Rp.918.000 + (Rp.918.000 * 2%) = Rp.918.000 + Rp.18.360 = Rp.936.360
# Rp.936.360 - (Rp.936.360 * 10%) = Rp.936.360 - Rp.93.636 = Rp.842.724

import os

os.system('clear')

month = int(input("Berapa Bulan: "))

utang_awal = 1000000

print("===============================================================================================")
print(f"{("Bulan").ljust(8)} | {("Utang Bunga Awal").ljust(15)} | {("Bunga Utang 2%").ljust(15)} | {("Utang").ljust(15)} | {("Cicilan").ljust(15)} | {("Sisa Utang").ljust(15)}")

for i in range(0, month):
    # Bulan
    print("{:>3}".format(i + 1), end="")
    print("{:17,.0f}".format(utang_awal), end= " ")
    utang_bunga = 0.02 * utang_awal # 20k
    utang_bulanan = utang_awal + utang_bunga # 1.020.000
    cicilan = 0.1 * utang_bulanan # 102.000
    utang_awal = utang_bulanan - cicilan 
    print("{:15,.0f}".format(utang_bunga), end=" ")
    print("{:20,.0f}".format(utang_bulanan), end=" ")
    print("{:15,.0f}".format(cicilan), end=" ")
    print("{:17,.0f}".format(utang_awal))

print("===============================================================================================")
print()
print("Final Amount Of Savings = Rp. {:10,.2f}".format(utang_awal))
print()