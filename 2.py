# Diketahui Ribuan Ayam memberi makan dengan 30kg/hari => menghasilkan 200 Butir/hari.
# Berasal dari 3 Jenis Kandang. Kandang A, B, C
# Kandang A : 10kg => 60 butir
# Kandang B : 10kg => 100 butir
# Kandang C : 10kg => 40 butir

print("A : Kandang A")
print("B : Kandang B")
print("C : Kandang C")
jenis_kandang = input("Masukkan Jenis Kandang : ").upper()
banyak_makanan = int(input("Masukkan Banyak Makanan (kg): "))

# Dictionary dari jenis kandang
perkalian = {"A": 6, "B": 10, "C": 4}

if jenis_kandang in perkalian:
    print("Jumlah Telur yang dihasilkan =", banyak_makanan * perkalian[jenis_kandang], "Butir Telur")
else:
    print("Output Salah")
