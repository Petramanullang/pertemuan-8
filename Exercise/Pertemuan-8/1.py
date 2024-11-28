# Kemeja < Rp.100k Disc 10% + 20%
# Kemeja > Rp.100k Disc 20% + 30%
# Celana < Rp.200k Disc 10% + 30%
# Celana > Rp.200k Disc 20% + 40%

import os

os.system("clear")

print("Jenis Pakaian")
print("=============")
print("1. Kemeja")
print("2. Celana")
jenis_pakaian = int(input("Jenis Pakaian : "))
harga_awal = int(input("Harga Awal Pakaian: Rp. "))

if jenis_pakaian == 1:
    if harga_awal < 100000:
        print("Anda Mendapatkan Diskon 10% + 20%")
        disc_1 = 0.1 * harga_awal
        print(f"Diskon 20% = Rp. {disc_1} (10% x {harga_awal})")
        print(f"Harga setelah Diskon 10% = Rp. {harga_awal - disc_1} ({harga_awal} - {disc_1})")
        disc_2 = 0.2 * harga_awal
        print(f"Diskon 20% = Rp. {disc_2} (20% x {disc_1})")
        print(f"Harga setelah Diskon 20% = Rp. {harga_awal - disc_2} ({harga_awal} - {disc_2})")
    elif harga_awal > 100000:
        print("Anda Mendapatkan Diskon 20% + 30%")
        disc_3 = 0.2 * harga_awal
        print(f"Diskon 20% = Rp. {disc_3} (20% x {harga_awal})")
        print(f"Harga setelah Diskon 20% = Rp. {harga_awal - disc_3} ({harga_awal} - {disc_3})")
        disc_4 = 0.3 * harga_awal
        print(f"Diskon 20% = Rp. {disc_4} (30% x {disc_3})")
        print(f"Harga setelah Diskon 30% = Rp. {harga_awal - disc_4} ({harga_awal} - {disc_4})")
    else:
        print("Tidak ada diskon")
elif jenis_pakaian == 2:
    if harga_awal < 200000:
        print("Anda Mendapatkan Diskon 10% + 20%")
        disc_7 = 0.1 * harga_awal
        print(f"Diskon 10% = Rp. {disc_7} (10% x {harga_awal})")
        print(f"Harga setelah Diskon 10% = Rp. {harga_awal - disc_7} ({harga_awal} - {disc_7})")
        disc_8 = 0.4 * harga_awal
        print(f"Diskon 40% = Rp. {disc_8} (40% x {disc_7})")
        print(f"Harga setelah Diskon 40% = Rp. {harga_awal - disc_8} ({harga_awal} - {disc_8})")
    elif harga_awal > 200000:
        print("Anda Mendapatkan Diskon 20% + 40%")
        disc_5 = 0.2 * harga_awal
        print(f"Diskon 20% = Rp. {disc_5} (20% x {harga_awal})")
        print(f"Harga setelah Diskon 20% = Rp. {harga_awal - disc_5} ({harga_awal} - {disc_5})")
        disc_6 = 0.4 * harga_awal
        print(f"Diskon 40% = Rp. {disc_6} (40% x {disc_5})")
        print(f"Harga setelah Diskon 40% = Rp. {harga_awal - disc_6} ({harga_awal} - {disc_6})")
    else:
        print("Tidak ada diskon")