
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    jumlah = 0
    for nilai in data:
        if nilai >= batas:
            jumlah += 1
    return jumlah


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Data pengujian
data1 = [60, 70, 80]
data2 = [59, 60, 61]
data3 = []

# Pengujian 1: Rata-rata
print("Rata-rata:", f"{rata_rata(data1):.2f}")

# Pengujian 2: Minimum dan maksimum
print("Minimum / maksimum:", min(data1), "/", max(data1))

# Pengujian 3: Jumlah lulus
print("Jumlah lulus:", nilai_lulus(data1))

# Pengujian 4: Batas kelulusan
print("Batas kelulusan:", nilai_lulus(data2), "lulus")

# Pengujian 5: List kosong
print("Rata-rata list kosong:", rata_rata(data3))
