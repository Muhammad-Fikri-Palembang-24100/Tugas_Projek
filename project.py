class Produk:
    def __init__(self, id_barang, nama, harga, stok):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok

    # UNtuk menampilkan barang
    def info(self):
        return f"[ID: {self.id_barang}] {self.nama} - Rp{self.harga:,} (Stok: {self.stok})"

class Toko:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = [] # List untuk menyimpan objek produk

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print(f"Sukses: {produk.nama} berhasil ditambahkan!")

    def tampilkan_semua_produk(self):
        print(f"\n--- Daftar Produk di {self.nama_toko} ---")
        if not self.daftar_produk:
            print("Belum ada produk.")
        else:
            for produk in self.daftar_produk:
                print(produk.info())

    def cari_produk(self, id_barang):
        for produk in self.daftar_produk:
            if produk.id_barang == id_barang:
                return produk
        return None

    def update_stok(self, id_barang, jumlah_baru):
        produk = self.cari_produk(id_barang)
        if produk:
            produk.stok = jumlah_baru
            print(f"Stok {produk.nama} berhasil diupdate menjadi {jumlah_baru}.")
        else:
            print("Produk tidak ditemukan!")

    def hapus_produk(self, id_barang):
        produk = self.cari_produk(id_barang)
        if produk:
            self.daftar_produk.remove(produk)
            print(f"Produk {produk.nama} berhasil dihapus.")
        else:
            print("Produk tidak ditemukan!")

# --- FUNGSI UTAMA ---
def main():
    # Inisialisasi Toko
    toko_saya = Toko("Toko Elektronik Maju Jaya")
    
    while True:
        print("\n=== MENU SISTEM PENYIMPANAN ===")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Update Stok Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            id_brg = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            try:
                harga = int(input("Masukkan Harga (angka): "))
                stok = int(input("Masukkan Stok Awal (angka): "))
                # Membuat Objek Produk baru
                produk_baru = Produk(id_brg, nama, harga, stok)
                toko_saya.tambah_produk(produk_baru)
            except ValueError:
                print("Error: Harga dan Stok harus berupa angka!")

        elif pilihan == '2':
            toko_saya.tampilkan_semua_produk()

        elif pilihan == '3':
            id_brg = input("Masukkan ID Barang yang akan diupdate: ")
            try:
                stok_baru = int(input("Masukkan jumlah stok baru: "))
                toko_saya.update_stok(id_brg, stok_baru)
            except ValueError:
                print("Error: Stok harus berupa angka!")

        elif pilihan == '4':
            id_brg = input("Masukkan ID Barang yang akan dihapus: ")
            toko_saya.hapus_produk(id_brg)

        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
    
    # LAnjutann