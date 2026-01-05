"""Program Manajemen Kontak"""

kontak1 = {'nama': "Andi", 'HP':"081276766767", 'email': "Andi@python.com"}
kontak2 = {'nama': "Rafa", 'HP':"081321211212", 'email': "Rafa@python.com"}

kontak = [kontak1, kontak2]

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
        if kontak :
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item ["nama"]} ({item ["HP"]}, {item ["email"]})')
        else:
            print("Tidak ada kontak")

    elif pilihan == '2': # menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan email yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    elif pilihan == '3': # menghapus kontak
        print("\n")
        if kontak :
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item ["nama"]} ({item ["HP"]}, {item ["email"]})')
        else:
            print("Kontak kosong")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: ")) # i_hapus, i nya adalah index, jadi dihapus berdasarkan indeks
        del kontak[i_hapus - 1]
        print("Kontak sudah dihapus!")

    elif pilihan == '4': # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")
    print("-" * 50)