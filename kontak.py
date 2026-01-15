"""Berisi kelas kontak untuk menjalankan program kontak"""

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

    def melihat_kontak (self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Tidak ada kontak")
            return 1

    def menambah_kontak(self):
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan email yang baru: ")
        kontak_baru = f"{nama} {HP} {email}" + '\n'
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
            try:
                i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: ")) # i_hapus, i nya adalah index, jadi dihapus berdasarkan indeks
                del self.kontak[i_hapus - 1]
                print("Kontak sudah dihapus!")
            except:
                print("Input yang anda masukkan salah!")

    def keluar_kontak(self):
       dokumen.menyimpan_kontak(isi=self.kontak)
