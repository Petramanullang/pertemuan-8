# Kecepatan(v) = 2m / detik
# Waktu(t) = 100 detik

# Jarak(s) = kecepatan(v) x waktu(t)

import os
os.system("clear")

print("1. Jarak")
print("2. Kecepatan")
print("3. Waktu")
print()
pilih = int(input("Pilih Menu : "))

def jarak():
    os.system("clear")
    print("Jarak")
    print()
    kecepatan = int(input("Kecepatan (m/d) : "))
    waktu = int(input("Waktu (d) : "))
    print("Jarak = ",kecepatan * waktu, "m")

def kecepatan():
    os.system("clear")
    print("Kecepatan")
    print()
    jarak = int(input("jarak (m) : "))
    waktu = int(input("Waktu (d) : "))
    print("Kecepatan = ",jarak // waktu, "m/d")

def waktu():
    os.system("clear")
    print("Waktu")
    print()
    jarak = int(input("Jarak (m) : "))
    kecepatan = int(input("Kecepatan (m/d) : "))
    print("Waktu = ",jarak // kecepatan, "detik")

def menu_invalid():
    os.system("clear")
    print("Menu tidak ada")

def pilih_menu(option):
    switch_case = {
        1 : jarak,
        2 : kecepatan,
        3 : waktu
    }
    switch_case.get(option, menu_invalid)()

pilih_menu(pilih)

