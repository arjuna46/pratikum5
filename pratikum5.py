from prettytable import PrettyTable

def tambah_data(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ")
    try:
        tugas = float(input("Masukkan nilai tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
    except ValueError:
        print("Input nilai harus berupa angka.")
        return

    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas

    data_mahasiswa[nim] = {
        'NO': len(data_mahasiswa) + 1,
        'NIM': nim,
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    }
    print("Data mahasiswa berhasil ditambahkan.\n")

def tampilkan_data(data_mahasiswa):
    if not data_mahasiswa:
        print("Data mahasiswa kosong.\n")
        return

    table = PrettyTable()
    table.field_names = ["NO", "NIM", "Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"]

    for nim, data in data_mahasiswa.items():
        table.add_row([data['NO'], nim, data['Nama'], data['Tugas'], data['UTS'], data['UAS'], data['Nilai Akhir']])

    print(table)
    print()

def ubah_data(data_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ")
    if nim in data_mahasiswa:
        print("Data sebelum diubah:", data_mahasiswa[nim])
        try:
            tugas = float(input("Masukkan nilai tugas baru: "))
            uts = float(input("Masukkan nilai UTS baru: "))
            uas = float(input("Masukkan nilai UAS baru: "))
        except ValueError:
            print("Input nilai harus berupa angka.")
            return

        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas

        data_mahasiswa[nim] = {
            'NO': data_mahasiswa[nim]['NO'],
            'NIM': nim,
            'Nama': data_mahasiswa[nim]['Nama'],
            'Tugas': tugas,
            'UTS': uts,
            'UAS': uas,
            'Nilai Akhir': nilai_akhir
        }
        print("Data mahasiswa berhasil diubah.\n")
    else:
        print("Data mahasiswa tidak ditemukan.\n")

if __name__ == "_main_":
    data_mahasiswa = {}
    while True:
        print("Menu Pilihan:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            tambah_data(data_mahasiswa)
        elif pilihan == '2':
            ubah_data(data_mahasiswa)
        # Add other options here if needed
        elif pilihan == '4':
            tampilkan_data(data_mahasiswa)
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-6.\n")
