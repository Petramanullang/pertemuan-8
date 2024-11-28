import os
os.system("clear")

# Kemeja < Rp.100k Disc 10% + 20%
# Kemeja > Rp.100k Disc 20% + 30%
# Celana < Rp.200k Disc 10% + 30%
# Celana > Rp.200k Disc 20% + 40%

diskon_rules = {
    1: (0.1, 0.2),  # Kemeja < Rp.100k
    2: (0.2, 0.3),  # Kemeja > Rp.100k
    3: (0.1, 0.3),  # Celana < Rp.200k
    4: (0.2, 0.4),  # Celana > Rp.200k
}

print("Jenis Pakaian")
print("=============")
print("1. Kemeja")
print("2. Celana")
jenis_pakaian = int(input("Jenis Pakaian : "))
harga_awal = int(input("Harga Awal Pakaian: Rp. "))

if jenis_pakaian == 1:
    kode_diskon = 1 if harga_awal < 100000 else 2
elif jenis_pakaian == 2:
    kode_diskon = 3 if harga_awal < 200000 else 4

diskon_berjenjang = diskon_rules[kode_diskon]

harga_sementara = harga_awal

print(f"Anda Mendapatkan Diskon {' + '.join(f'{int(d * 100)}%' for d in diskon_berjenjang)}")
for diskon in diskon_berjenjang:
    potongan = diskon * harga_sementara
    harga_sementara -= potongan
    print(f"Diskon {int(diskon * 100)}% = Rp. {potongan:.0f}")
    print(f"Harga setelah diskon {int(diskon * 100)}% = Rp. {harga_sementara:.0f}")

print(f"Harga Akhir = Rp. {harga_sementara:.0f}")
