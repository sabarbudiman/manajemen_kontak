"""Program Manajemen Kontak"""
class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak (self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Tidak ada kontak")
            return 1

    def menambah_kontak(self):
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan email yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # print("\n")
        # if kontak:
        #     for num, item in enumerate(kontak, start=1):
        #         print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        # else:
        #     print("Kontak kosong")
        #     continue
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: ")) # i_hapus, i nya adalah index, jadi dihapus berdasarkan indeks
            del self.kontak[i_hapus - 1]
            print("Kontak sudah dihapus!")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")
    print()
    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")
    print("-" * 50)

    if pilihan == '1': # melihat semua kontak
       kontak_kantor.melihat_kontak()
    elif pilihan == '2': # menambahkan kontak
        kontak_kantor.menambah_kontak()
    elif pilihan == '3': # menghapus kontak
       kontak_kantor.menghapus_kontak()
    elif pilihan == '4': # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")
    print("-" * 50)