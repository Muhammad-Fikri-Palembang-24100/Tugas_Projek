# Sistem Manajemen Inventaris Toko (Inventory Management System)

> **Tugas Besar Pemrograman Berorientasi Objek (PBO)** > Program aplikasi berbasis Python CLI (Command Line Interface) untuk mengelola stok barang toko secara efisien.

---

## Deskripsi Projek
Aplikasi ini dibangun untuk membantu pemilik toko mengelola inventaris barang secara digital. Dibangun dengan konsep **Object-Oriented Programming (OOP)**, aplikasi ini memungkinkan pengguna untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data barang.

Tujuan utama projek ini adalah mendemonstrasikan pemahaman mendalam mengenai konsep dasar Python dan PBO seperti *Class*, *Object*, dan *Method*

## Fitur Utama
1. **Menambah Produk Baru**: Memasukkan data barang (ID, Nama, Harga, Stok) ke dalam sistem.
2. **Melihat Daftar Produk**: Menampilkan tabel seluruh barang yang tersedia di gudang.
3. **Update Stok**: Mengubah jumlah stok barang tertentu (misal: saat barang masuk atau terjual).
4. **Hapus Produk**: Menghapus data barang yang sudah tidak dijual dari sistem.
5. **Pencarian ID**: Validasi otomatis untuk memastikan operasi dilakukan pada barang yang tepat.

---

##  Struktur Kode & Konsep PBO
Projek ini menerapkan konsep dasar PBO sebagai berikut:

- **Class `Produk`**: 
  Digunakan untuk setiap barang. Menyimpan atribut seperti `id_barang`, `nama`, `harga`, dan `stok`.
- **Class `Toko`**: 
  Class pengelola (Manager) yang bertanggung jawab menyimpan daftar produk dalam `list` dan berisi logika bisnis (tambah, hapus, update).

---
## Cara Penggunaan Kode (User Guide)

 **Langkah 1: Clone Repositori**
```bash
git clone https://github.com/Muhammad-Fikri-Palembang-24100/Tugas_Projek.git
```

**Langkah 2:  Masuk Folder Repositori**
```bash
cd Tugas_Projek
```

**Langkah 3: Jalankan Aplikasi**
```bash
python project.py
```
## Simulasi Penggunaan Kode
> ** Aplikasi ini belum ada sama sekali data (produk) yang disimpan, jadi kita perlu menambahkan produk baru **(pilih menu 1)**>

Setelah program dijalankan maka akan muncul tampilan utama seperti ini:
```plaintext
=== MENU SISTEM GUDANG ===
1. Tambah Produk Baru
2. Tampilkan Semua Produk
3. Update Stok Produk
4. Hapus Produk
5. Keluar
Pilih menu (1-5):
```
**A. Menambah Barang Baru**
Pada menu utama, ketik angka 1 lalu tekan Enter. Program akan meminta data. Kita coba masukkan contoh berikut:

>Masukkan ID Barang: 01
Masukkan Nama Barang: Keyboard Gaming
Masukkan Harga: 350000
Masukkan Stok Awal: 10
Output: "Sukses: Keyboard Gaming berhasil ditambahkan!"

**B. Melihat Daftar Barang**
Pada menu utama, ketik angka 2 lalu tekan Enter. Program akan menampilkan seluruh barang yang sudah diinput sebelumnya dalam format rapi seperti dibawah ini:
>--- Daftar Produk di Toko Elektronik Maju Jaya ---
[ID: 01] Keyboard Gaming - Rp350,000 (Stok: 10)


**C. Mengupdate Stok Barang**
Misalkan barang 01 terjual 2 unit, sisa stok menjadi 8.
Pada menu utama, ketik angka 3 lalu tekan Enter.

>Masukkan ID Barang yang mau diedit: 01.
Masukkan jumlah stok baru: 8.
Output: "Stok Keyboard Gaming berhasil diupdate menjadi 8."

**D. Menghapus Barang**
Pada menu utama, ketik angka 4 lalu tekan Enter.

>Masukkan ID Barang yang mau dihapus: 01.
Output: "Produk Keyboard Gaming berhasil dihapus."

**E. Keluar dari Program**
Ketik angka 5 untuk menghentikan program dan kembali ke terminal.

4. Pemecahan Masalah (Troubleshooting)
- Error: 'python' is not recognized... Pastikan Python sudah dimasukkan ke dalam PATH environment variable komputer Anda saat instalasi. Atau coba gunakan perintah py (Windows) atau python3 (Mac/Linux).

- Error: ValueError saat input angka Pastikan saat diminta input Harga atau Stok, Anda hanya memasukkan angka (contoh: 5000), bukan teks (contoh: lima ribu atau Rp 5000).
---
## Sekian dan Terima Kasih
| Data | Keterangan |
| :--- | :--- |
| **Nama Lengkap** | Muhammad Fikri Palembang |
| **NPM / NIM** | 121055520124100 |
| **Kelas** | Info4 |
| **Program Studi** | Teknik Informatika |
| **Mata Kuliah** | Pemrograman Berorientasi Objek |
| **Dosen Pengampu** | Muh Ikhwan Ilyas, S.Kom., M.Kom. |