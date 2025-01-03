#STUDI KASUS
def validasi_form(nama, nomor_telepon, email):
    errors = []

    # validasi nama lengkap (hanya huruf)
    if not nama.replace(" ", "").isalpha():
        errors.append("nama lengkap harus hanya berisi huruf.")

    # validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        errors.append("nomor telepon harus hanya berisi angka.")

    # validasi email (harus mengandung '@' dan '.')
    if "@" not in email or "." not in email:
        errors.append("email harus mengandung karakter '@' dan '.'.")

    # output hasil validasi
    if errors:
        print("terdapat kesalahan pada data pendaftaran:")
        for error in errors:
            print(f"- {error}")
    else:
        print("data pendaftaran valid.")
        
# contoh penggunaan
nama = input("masukkan nama lengkap: ")
nomor_telepon = input("masukkan nomor telepon: ")
email = input ("masukkan email: ")

validasi_form(nama, nomor_telepon, email)
