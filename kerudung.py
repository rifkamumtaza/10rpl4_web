import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    menu = 0
    jawaban_user = 0
    total_harga = 0
    jumlah_barang = 0
    uang = 0
    
    # Inisialisasi root window
    root = tk.Tk()
    root.withdraw()  # Sembunyikan window utama karena kita hanya membutuhkan dialog

    # Teks yang menampilkan daftar produk
    daftar_barang = """=======HIJAB BY REGITA=======

TERSEDIA:
1. Segiempat Paris Jadul\t\tRp.20.000
2. Segiempat Paris Premium\tRp.25.000
3. Segiempat Bella Square\t\tRp.15.000
4. Segiempat Plain Square\t\tRp.19.000
5. Pashmina Silk\t\t\tRp.45.000
6. Pashmina Ceruty\t\tRp.22.000
7. Pashmina Kaos\t\t\tRp.29.000
8. Pashmina Plisket\t\tRp.25.000
9. Pashmina Shimmer\t\tRp.35.000
10. Pashmina Shawl\t\tRp.50.000
11. Bergo Hamidah\t\tRp.21.000
0. Selesai

Silahkan Pilih Menu Diatas (Inputkan Nomer)"""

    while True:
        menu = simpledialog.askinteger("MENU", daftar_barang, minvalue=0, maxvalue=11)
        
        if menu == 0:
            if total_harga > 0:
                jawaban_user = messagebox.askyesno("SELESAI !!!", f"MENU SELESAI !!!\n\nBelanjaan Anda:\nRp.{total_harga}\n\nKembali Belanja?")
                if not jawaban_user:
                    break
            else:
                jawaban_user = messagebox.askyesno("SELESAI !!!", "MENU SELESAI !!!\n\nAnda Belum Membeli Apapun !!!\n\nKembali Belanja?")
                if not jawaban_user:
                    break

        elif menu == 1:
            jumlah = simpledialog.askinteger("SEGIEMPAT PARIS JADUL", "Segiempat Paris Jadul = Rp.20.000\n\nMau beli Segiempat Paris Jadul Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 20000

        elif menu == 2:
            jumlah = simpledialog.askinteger("SEGIEMPAT PARIS PREMIUM", "Segiempat Paris Premium = Rp.25.000\n\nMau Beli Segiempat Paris Premium Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 25000

        elif menu == 3:
            jumlah = simpledialog.askinteger("SEGIEMPAT BELLA SQUARE", "Segiempat Bella Square = Rp.15.000\n\nMau Beli Segiempat Bella Square Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 15000

        elif menu == 4:
            jumlah = simpledialog.askinteger("SEGIEMPAT PLAIN SQUARE", "Segiempat Plain Square = Rp.19.000\n\nMau Beli Segiempat Plain Square Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 19000

        elif menu == 5:
            jumlah = simpledialog.askinteger("PASHMINA SILK", "Pashmina Silk = Rp.45.000\n\nMau Beli Pashmina Silk Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 45000

        elif menu == 6:
            jumlah = simpledialog.askinteger("PASHMINA CERUTY", "Pashmina Ceruty = Rp.22.000\n\nMau Beli Pashmina Ceruty Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 22000

        elif menu == 7:
            jumlah = simpledialog.askinteger("PASHMINA KAOS", "Pashmina Kaos = Rp.29.000\n\nMau Beli Pashmina Kaos Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 29000

        elif menu == 8:
            jumlah = simpledialog.askinteger("PASHMINA PLISKET", "Pashmina Plisket = Rp.25.000\n\nMau Beli Pashmina Plisket Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 25000

        elif menu == 9:
            jumlah = simpledialog.askinteger("PASHMINA SHIMMER", "Pashmina Shimmer = Rp.35.000\n\nMau Beli Pashmina Shimmer Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 35000

        elif menu == 10:
            jumlah = simpledialog.askinteger("PASHMINA SHAWL", "Pashmina Shawl = Rp.50.000\n\nMau Beli Pashmina Shawl Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 50000

        elif menu == 11:
            jumlah = simpledialog.askinteger("BERGO HAMIDAH", "Bergo Hamidah = Rp.21.000\n\nMau Beli Bergo Hamidah Berapa?", minvalue=1)
            jumlah_barang += jumlah
            total_harga += jumlah * 21000

        if total_harga > 0:
            jawaban_user = messagebox.askyesno("PILIHAN", f"Belanjaan Anda:\nRp.{total_harga}\n\nIngin Belanja Lagi?")

        if jawaban_user == 0:
            break

    if total_harga == 0:
        messagebox.showinfo("TIDAK BERBELANJA", "Anda Tidak Berbelanja Apapun :(")
    else:
        while True:
            uang = simpledialog.askinteger("UANG", f"Total Belanjaan Anda \nRp.{total_harga}\n\nMasukkan Nominal Uang", minvalue=total_harga)
            if uang >= total_harga:
                break
            else:
                messagebox.showwarning("UANG KURANG", "Uang Anda kurang silahkan bayar dengan uang pas atau lebih")
        
        kembalian = uang - total_harga
        messagebox.showinfo("KEMBALIAN", f"Kembalian Anda \nRp.{kembalian}")
        
        messagebox.showinfo("NOTA", f"""=====HIJAB BY REGITA=====
        
Detail Belanjaan Anda ===>
Banyak Barang   : {jumlah_barang}
Harga Total     : Rp.{total_harga}

Total Bayar     : Rp.{uang}
Uang Kembalian  : Rp.{kembalian}

Terimakasih sudah berbelanja
Silahkan datang kembali

Keluhan Hubungi : 0882009057369

=====HIJAB BY REGITA=====""")
        
if __name__ == "__main__":
    main()
