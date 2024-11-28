umur = int(input("Masukkan Umur: "))

# Meminta input status bekerja terlepas dari umur
status_bekerja = input("Masukkan Status Bekerja ya/tidak: ").lower()

if umur >= 100:
    print("Seriusan Umurnya di atas 100 Tahun? Bjir...")

if umur >= 18:
    if status_bekerja == "ya":
        pendapatan_perbulan = int(input("Masukkan Pendapatan Perbulan: Rp."))
        jumlah_tanggungan = int(input("Masukkan Jumlah Tanggungan jika tidak ada ketik 0: "))
        
        if jumlah_tanggungan == 0:
            biaya_hidup = pendapatan_perbulan
        else:
            biaya_hidup = pendapatan_perbulan / jumlah_tanggungan

        if biaya_hidup <= 300000:
            print("Anda Penduduk Miskin")
        else:
            print("Anda Bukan Penduduk Miskin")

    elif status_bekerja == "tidak":
        pass  # Di sini bisa ditambahkan logika tambahan jika perlu

    else:
        print("ANDA PENDUDUK MISKIN, di suruh milih ya/tidak malah jawab yang lain")

# Cek untuk status sekolah jika umur kurang dari 18 atau status bekerja "tidak"
if umur < 18 or (umur >= 18 and status_bekerja == "tidak"):
    status_sekolah = input("Masukkan Status Sekolah ya/tidak: ").lower()
    if status_sekolah == "ya":
        print("Anda Bukan Penduduk Miskin")
    elif status_sekolah == "tidak":
        print("\nAnda Penduduk Miskin")
    else:
        print("ANDA PENDUDUK MISKIN, di suruh milih ya/tidak malah jawab yang lain")

# Tambahkan logika untuk memproses kondisi ketika umur >= 100
if umur >= 100:
    status_sekolah = input("Masukkan Status Sekolah ya/tidak: ").lower()
    if status_sekolah == "ya":
        print("Anda Bukan Penduduk Miskin")
    elif status_sekolah == "tidak":
        print("\nAnda Penduduk Miskin")
    else:
        print("ANDA PENDUDUK MISKIN, di suruh milih ya/tidak malah jawab yang lain")
