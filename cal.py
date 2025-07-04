# Simple Calculator by Oppa 🧡

def tambah(x, y):
    return x + y

def tolak(x, y):
    return x - y

def darab(x, y):
    return x * y

def bahagi(x, y):
    if y == 0:
        return "Tak boleh bahagi dengan 0!"
    return x / y

print("🧮 Kalkulator Mudah")
print("1. Tambah")
print("2. Tolak")
print("3. Darab")
print("4. Bahagi")

while True:
    pilihan = input("Pilih operasi (1/2/3/4 atau 'q' untuk keluar): ")

    if pilihan == 'q':
        print("Keluar dari kalkulator. Bye! 🫶")
        break

    if pilihan in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan nombor pertama: "))
            num2 = float(input("Masukkan nombor kedua: "))

            if pilihan == '1':
                print("Hasil:", tambah(num1, num2))
            elif pilihan == '2':
                print("Hasil:", tolak(num1, num2))
            elif pilihan == '3':
                print("Hasil:", darab(num1, num2))
            elif pilihan == '4':
                print("Hasil:", bahagi(num1, num2))
        except ValueError:
            print("⚠️ Sila masukkan nombor yang sah!")
    else:
        print("⚠️ Pilihan tidak sah. Sila cuba lagi.")
        