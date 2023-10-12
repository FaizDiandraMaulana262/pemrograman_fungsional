expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1 Buatlah Fungsi add_expense disini


def add_expense(date, description, amount):
    jumlah_pengeluaran = {'tanggal': date,
                          'deskripsi': description, 'jumlah': amount}
    return jumlah_pengeluaran

# TODO 2 Buatlah fungsi calculate_total_expenses disini


def calculate_total_expenses(x): 
    total = 0
    for i in x :
        total = total + i['jumlah']
    return print(
    f"\nTotal Pengeluaran Harian: Rp {total}")

# TODO 3 Buatlah fungsi get_expenses_by_date disini

def get_expenses_by_date(ex, date):
    list = [i for i in ex if i['tanggal'] == date]
    return list

# TODO 4 Buatlah fungsi generate_expenses_report disini


def generate_expenses_report(expenses):
    for i in expenses:
        yield str(i)

# TODO 5 pastikan semua fungsi yang ada sudah berupa pure function;

def add_expense_interactively():
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(expense)


def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command): return int(input(command))


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            test = add_expense_interactively()
            expenses.append(test)
        elif choice == 2:
            calculate_total_expenses(expenses)
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        elif choice == 6:
            print(expenses)
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
