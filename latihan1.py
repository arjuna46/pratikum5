# Membuat Dictionary
kontak = {}
kontak["Ari"] = "081267888"
kontak["Dina"] = "087677776"

print("Kontak Ari: ", kontak["Ari"])
kontak["Riko"] = "087654544"
kontak["Dina"] = "088999776"
print("\nSemua Nama: ")
for nama in kontak:
    print(nama)
print("\nSemua Nomor: ")
for nomor in kontak.values():
    print(nomor)
print("\nDaftar Nama dan Nomor: ")
for nama, nomor in kontak.items():
    print(nama, "|", nomor)
del kontak["Dina"]
print("\nDaftar Kontak Setelah Dihapus: ")
for nama, nomor in kontak.items():
    print(nama, "|", nomor)