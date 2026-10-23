# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
Struktur program ini terdiri dari enam file latihan dan satu file praktik. File latihan pertama digunakan untuk membuat list dan menghitung banyak data, file kedua untuk mempelajari indeks dan slicing, file ketiga untuk mengubah, menambah, menyisipkan, dan menghapus elemen dalam list, file keempat untuk menghitung total, rata-rata, nilai minimum, dan maksimum, file kelima untuk mencari nilai yang lulus berdasarkan batas nilai 60, dan file keenam untuk membuat fungsi yang menghitung rata-rata serta menangani list kosong agar tidak terjadi error. Sementara itu, file praktik analisis nilai mahasiswa menggabungkan materi yang sudah dipelajari untuk menghitung rata-rata, mencari nilai minimum dan maksimum, menghitung jumlah mahasiswa yang lulus, serta menguji program menggunakan beberapa data, termasuk data dengan batas kelulusan dan list kosong.

## Cara Menjalankan
python3 praktik/analisis_nilai_mahasiswa.py

## Test Case
Pada pengujian program, saya menggunakan beberapa data untuk memastikan codingan berjalan sesuai dengan hasil yang diharapkan. Pada data [60, 70, 80], hasil rata-rata yang diharapkan adalah 70.00 dan hasil aktualnya juga 70.00 dengan status berhasil. Untuk pengujian minimum dan maksimum menggunakan data yang sama, hasil yang diharapkan adalah 60 dan 80, dan hasil aktualnya juga sesuai. Pada pengujian jumlah lulus dengan data [60, 70, 80], hasil yang diharapkan adalah 3 orang dan hasil aktualnya juga 3 orang. Selanjutnya, pada data [59, 60, 61] dengan batas kelulusan 60, hasil yang diharapkan adalah 2 orang lulus dan hasil aktualnya juga 2 orang karena nilai 60 dan 61 memenuhi batas kelulusan. Terakhir, pada pengujian list kosong [], hasil yang diharapkan adalah program tidak mengalami error, dan hasil aktualnya adalah fungsi rata-rata mengembalikan nilai 0 sehingga program tetap berjalan. Berdasarkan seluruh pengujian tersebut, hasil aktual sudah sesuai dengan hasil yang diharapkan dan semua test case dinyatakan berhasil.

## Refleksi
Satu hal yang saya pahami tentang indeks dan list adalah list dapat digunakan untuk menyimpan banyak data dalam satu variabel, sehingga data lebih mudah diakses dan diolah. Indeks pada Python dimulai dari 0, sedangkan indeks -1 digunakan untuk mengambil elemen terakhir. Selain itu, saya juga memahami bahwa list dapat diubah, ditambah, dan dihapus elemennya sesuai kebutuhan.
Satu kesalahan yang berhasil saya perbaiki adalah risiko terjadinya ZeroDivisionError ketika menghitung rata-rata dari list kosong. Awalnya, jika rata-rata dihitung dengan membagi jumlah data dengan banyaknya elemen, program bisa mengalami error ketika jumlah elemennya 0. Untuk memperbaikinya, saya menambahkan kondisi if len(data) == 0: return 0 pada fungsi rata_rata(), sehingga program dapat menangani list kosong tanpa mengalami error.
