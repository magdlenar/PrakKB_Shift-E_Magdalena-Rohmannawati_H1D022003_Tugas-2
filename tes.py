import json  #Library

shopping_list = []  # List untuk menyimpan item belanja

def add_item(item, quantity): #Menambahkan item ke daftar belanja
    shopping_list.append({"Item": item, "Quantity": quantity})
    print(f"{item} telah ditambahkan ke daftar")

def remove_item(item):#Menghapus Item
    global shopping_list
    shopping_list = [i for i in shopping_list if i["Item"] != item]
    print(f"{item} telah dihapus dari daftar")

def show_list(): #Menampilkan daftar belanja
    if shopping_list:
        print("\n Daftar Belanja ")
        for index, data in enumerate(shopping_list, start=1):
            print(f"{index}. {data['Item']} - {data['Quantity']}")
    else:
        print("Daftar belanja kosong")

def save_list(filename="shopping_list.json"): #Library
    """Menyimpan ke dalam file JSON"""
    with open(filename, "w") as file:
        json.dump(shopping_list, file, indent=4)
    


while True:   #Struktur Kontrol
    print("\n MENU AKTIVITAS ")
    print("1. Tambah Item")
    print("2. Hapus Item")
    print("3. Tampilkan Daftar Belanja")
    print("4. Simpan dan Keluar")

    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        item = input("Masukkan nama item: ")
        quantity = input("Masukkan jumlah: ")
        add_item(item, quantity)

    elif choice == "2":
        item = input("Masukkan nama item yang ingin dihapus: ")
        remove_item(item)

    elif choice == "3":
        show_list()

    elif choice == "4":
        save_list()
        print("=== Copyright (c) 2025, Magdalena ===")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
