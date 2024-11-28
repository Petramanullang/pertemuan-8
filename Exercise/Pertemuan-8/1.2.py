# Kemeja < Rp.100k Disc 10% + 20%
# Kemeja > Rp.100k Disc 20% + 30%
# Celana < Rp.200k Disc 10% + 30%
# Celana > Rp.200k Disc 20% + 40%

print("Jenis Pakaian")
print("=============")
print("1. Kemeja")
print("2. Celana")
jenis_pakaian = int(input("Jenis Pakaian : "))
harga_awal = int(input("Harga Awal Pakaian: Rp. "))

if jenis_pakaian == 1 :
    disc_1 = 0.1 if harga_awal <= 100000 else 0.2
    disc_2 = 0.2 if harga_awal <= 100000 else 0.3
elif jenis_pakaian == 2:
    disc_2 = 0.1 if harga_awal <= 200000 else 0.2
    disc_2 = 0.3 if harga_awal <= 200000 else 0.4
else:
    print("Pilihan Salah !!")

harga_discount_1 = harga_awal -(harga_awal * disc_1)
harga_discount_2 = harga_discount_1 - (harga_discount_1 * disc_2)
print(f"Harga Yang Harus di Bayar = Rp.{harga_discount_2:.0f}")