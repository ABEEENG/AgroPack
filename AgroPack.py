import pandas as pd
import os
from tabulate import tabulate
import datetime

# ================== PENGECEKAN FILE =====================

try:
    pd.read_csv('Akun.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Username': ['Owner'], 'Password': ['Owner123'], 'Role' : ['Pemilik']})
    df['Username'].astype(str)
    df.to_csv('Akun.csv', index=False)
    
try:
    pd.read_csv('Produk.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Keterangan_Paket': [], 'Produk_Paket': [], 'Stok_Paket' : [], 'Harga' : []})
    df.to_csv('Produk.csv', index=False)

try:
    pd.read_csv('Pemesanan.csv')
except FileNotFoundError:
    df = pd.DataFrame({'username' : [], 'Waktu_Pemesanan' : [], 'Paket_Dipesan': [], 'Produk_Paket' : [], 'Jumlah' : [], 'Harga' : [], 'Status_Pemesanan' : [], 'Kontak_Pemesan' : []})
    df[['username', 'Kontak_Pemesan']].astype(str)
    df.to_csv('Pemesanan.csv', index=False)

try:
    pd.read_csv('Feedback.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Feedback': []})
    df.to_csv('Feedback.csv', index=False)


# ================== REGISTER / LOGIN ====================

def menu():
    os.system('cls')
    Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
    print(Header)

    print('''

                        1) LOGIN
                        2) REGISTER

    ''')

    while True:
        Pilih = input("Pilih Menu! (1 / 2) : ") 
        if Pilih == "1":
            login()
        elif Pilih == "2":
            register()
        else:
            print("     Pilihan tidak sesuai! Silahkan input kembali!")
            input("     Tekan ENTER untuk melanjutkan!")
            return menu()
        
def register():
    
    os.system('cls')
    Header = """
    ==================================================================
    
    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
    print(Header)

    try:
        username = input('    Masukkan Username : ')
        if username <= 
        password = input('    Masukkan Password : ')
    except ValueError:
        print('    Password atau Username tidak valid!')
        input('    Tekan ENTER untuk melanjutkan')
        return login()
    
    df = pd.read_csv('Akun.csv')
    
    if username in df['Username'].values:
        print('    Username sudah digunakan!')
        input('    Tekan ENTER untuk melanjutkan')
        return register()
    else:
        df = pd.concat([df, pd.DataFrame([{'Username' : username, 'Password' : password, 'Role' : 'Pelanggan'}])], ignore_index=True)
        df.to_csv('Akun.csv', index=False)
        print('    Akun Berhasil Ditambahkan!')
        input('    Tekan ENTER untuk melanjutkan')
        return menu()

def login():

    os.system('cls')
    Header = """
    ==================================================================
    
    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
    print(Header)

    
    try:
        username = input('    Masukkan Username : ')
        password = input('    Masukkan Password : ')
    except ValueError:
        print('     Password atau Username tidak valid!')
        input('     Tekan ENTER untuk melanjutkan')
        return login()
    
    df = pd.read_csv('Akun.csv')
    BarisData = df[(df['Username'] == username) & (df['Password'] == password)]

    if not BarisData.empty:
        role = BarisData['Role'].iloc[0]
        if role == "Pemilik":
            print('    Login berhasil! Selamat datang', BarisData['Username'].iloc[0])
            input('    Tekan ENTER untuk melanjutkan')
            pemilik(role, username)
        elif role == "Admin":
            print('    Login berhasil! Selamat datang', BarisData['Username'].iloc[0])
            input('    Tekan ENTER untuk melanjutkan')
            admin(role, username)
        elif role == "Pelanggan":
            print('    Login berhasil! Selamat datang', BarisData['Username'].iloc[0])
            input('    Tekan ENTER untuk melanjutkan')
            pelanggan(role, username)

    else:
        print('    Password atau Username salah! Silahkan Coba lagi.')
        input('    Tekan ENTER untuk melanjutkan')
        return login()

def pemilik(role, username):
    while True:
        os.system('cls')
        Header = """
    ==================================================================
    
    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Kelola Akun Admin\n'
            '    2) Kelola Produk\n'
            '    3) Melihat Laporan Penjualan\n'
            '    4) Melihat Feedback\n'
            '    5) Edit Akun\n'
            '    6) Logout\n'
        )
        Pilih = input('    Pilih Menu! ( 1 / 2 / 3 / 4 / 5 ) : ')
        if Pilih == '1':
            KelolaAkun()
        elif Pilih == '2':
            KelolaProduk(role, username)
        elif Pilih == '3':
            LaporanPenjualan()
        elif Pilih == '4':
            MelihatFeedback()
        elif Pilih == '5':
            EditAkun(role, username)
        elif Pilih == '6':
            logout()
        else:
            print('    Input tidak valid! Silahkan pilih lagi')
            print('    Tekan ENTER untuk melanjutkan')
            return pemilik(role, username)

def admin(role, username):
    while True:
        os.system('cls')
        Header = """
        ==================================================================

        ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
        ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
        ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
        ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
        ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                       SOLUSI PINTAR UNTUK PETANI TEMBAKAU

        ================================================================== """
        print(Header)

        print(
            '    1) Kelola Pesanan\n'
            '    2) Kelola Produk\n'
            '    3) Melihat Feedback\n'
            '    4) Edit Akun\n'
            '    5) Logout\n'
        )


        Pilih = input('    Pilih Menu! ( 1 / 2 / 3 / 4 ) : ')
        if Pilih == '1':
            KelolaPesanan()
        elif Pilih == '2':
            KelolaProduk(role, username)
        elif Pilih == '3':
            MelihatFeedback()
        elif Pilih == '4':
            EditAkun(role, username)
        elif Pilih == '5':
            logout()
        else:
            print('    Input tidak valid! Silahkan pilih lagi')
            input('    Tekan ENTER untuk melanjutkan')
            return admin()

def pelanggan(role, username):
    while True:
        os.system('cls')
        Header = """
    ==================================================================
    
    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Pesan Produk!\n'
            '    2) Edit Akun\n'
            '    3) Feedback\n'
            '    4) Logout\n'
        )


        Pilih = input('    Pilih Menu! ( 1 / 2 / 3 / 4 ) : ')
        if Pilih == '1':
            PesanProduk(username)
        elif Pilih == '2':
            EditAkun(role, username)
        elif Pilih == '3':
            Feedback()
        elif Pilih == '4':
            logout()
        else:
            print('    Input tidak valid! Silahkan pilih lagi')

        

def KelolaProduk(role, username):
    while True:
        os.system('cls')
        Header = """
        ==================================================================

        ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
        ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
        ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
        ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
        ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                       SOLUSI PINTAR UNTUK PETANI TEMBAKAU

        ================================================================== """
        print(Header)

        print(
            '    1) Tampilkan Produk\n'
            '    2) Tambah Produk\n'
            '    3) Edit Produk\n'
            '    4) Hapus Produk\n'
            '    5) Kembali\n'
        )
        Pilih = input("    Pilih Menu! ( 1 / 2 / 3 / 4 / 5 ) : ")
        if Pilih == '1':
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
                input('Tekan ENTER untuk kembali!')
                break
        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            KetPaket_baru = input("    Masukkan Keterangan Paket : ")
            if KetPaket_baru in df['Keterangan_Paket'].values:
                input('    Keterangan paket sudah ada! Tekan ENTER untuk kembali!')
            else:
                Produk_baru = input("    Masukkan Produk Paket : ")
                Harga_baru = input("    Masukkan Harga Paket : ")
                Stok = int(input('Masukkan Stok Paket : '))
                df = pd.concat([df, pd.DataFrame([{'Keterangan_Paket' : KetPaket_baru, 'Produk_Paket' : Produk_baru, 'Stok_Paket' : Stok, 'Harga' : Harga_baru}])], ignore_index=True)
                df.to_csv('Produk.csv', index=False)
                print('    Produk Berhasil Ditambahkan!')
                input('    Tekan ENTER untuk melanjutkan')
                break
        elif Pilih == '3':
            editproduk(role, username)
        elif Pilih == '4':
            while True:
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
                KetPaket = input('    Masukkan Keterangan Paket : ')
                if df['Keterangan_Paket'].empty:
                    input('    Paket produk tidak ada!\n    Tekan ENTER untuk kembali!')
                    break

                if KetPaket in df['Keterangan_Paket'].values:
                    df = df[df['Keterangan_Paket'] != KetPaket]
                    df.to_csv('Produk.csv', index=False)
                    print('    Data berhasil di hapus!')
                    input('    Tekan ENTER untuk kembali!')
                    break
                else:
                    input('    Paket tidak ada! Tekan ENTER untuk kembali!')
                    continue
        elif Pilih == '5':
            break
        else:
            input('Input tidak valid! tekan ENTER untuk melanjutkan')
            continue
                        

def editproduk(role, username):
    while True: 
        os.system('cls')
        df = pd.read_csv('Produk.csv')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        print(
            '    1) Keterangan Paket\n'
            '    2) Produk Paket\n'
            '    3) Harga\n'
            '    4) Stok Paket\n'
            '    5) Kembali\n'
        )

        Pilih = input("    Pilih data yang ingin diubah! ( 1 / 2 / 3 / 4 ) : ")
        
        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            while True:
                KetPaket_lama = input('Masukkan Keterangan Paket Lama : ')
                if KetPaket_lama in df['Keterangan_Paket'].values:
                    KetPaket_baru = input('Masukkan Keterangan Paket Baru : ')
                    df.loc[df['Keterangan_Paket'] == KetPaket_lama, 'Keterangan_Paket'] = KetPaket_baru
                    df.to_csv('Produk.csv', index=False)   
                    input('    Paket Berhasil Dirubah! Tekan ENTER untuk kembali')
                    return editproduk(role)
                
        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            while True:
                KetPaket = input('Masukkan Keterangan Paket : ')
                if KetPaket in df['Keterangan_Paket'].values:
                    Produk_baru = input('Masukkan Produk Baru : ')
                    df.loc[df['Keterangan_Paket'] == KetPaket, 'Produk_Paket'] = Produk_baru
                    df.to_csv('Produk.csv', index=False)    
                    input('    Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                    return editproduk(role)

        elif Pilih == '3':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            while True:
                KetPaket = input('Masukkan Keterangan Paket : ')
                if KetPaket in df['Keterangan_Paket'].values:
                    Harga_baru = int(input('Masukkan Harga Baru : '))
                    df.loc[df['Keterangan_Paket'] == KetPaket, 'Harga'] = Harga_baru
                    df.to_csv('Produk.csv', index=False)  
                    input('    Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                    return editproduk(role)

        elif Pilih == '4':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            while True:
                KetPaket = input('Masukkan Keterangan Paket : ')
                if KetPaket in df['Keterangan_Paket'].values:
                    Stok_baru = int(input('Masukkan Stok Baru : '))
                    df.loc[df['Keterangan_Paket'] == KetPaket, 'Stok_Paket'] = Stok_baru
                    df.to_csv('Produk.csv', index=False)  
                    input('    Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                    return editproduk(role)
                
        elif Pilih == '5':
            break

        else:
            input('    Input salah! tekan ENTER untuk melanjutkan!')


def KelolaAkun():
    while True:
        os.system('cls')
        Header = """
        ==================================================================

        ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
        ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
        ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
        ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
        ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
        ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                       SOLUSI PINTAR UNTUK PETANI TEMBAKAU

        ================================================================== """
        print(Header)

        print(
            '    1) Tampilkan Akun\n'
            '    2) Ubah Role Akun\n'
            '    3) Kembali'
        )


        Pilih = input('    Pilih Menu ( 1 / 2 / 3) : ')
        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Akun.csv')
            df = df[['Username', 'Role']]
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break
        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Akun.csv')
            df_tampilan = df[['Username', 'Role']]
            print(tabulate(df_tampilan, headers='keys', tablefmt='fancy_grid'))
            username = input('    Masukkan username yang ingin diubah role : ')
            if username in df['Username'].values:
                while True: 
                    Role_baru = input('Masukkan Role Baru (Pemilik / Admin / Pelanggan) : ')
                    if Role_baru == 'Pemilik' or Role_baru == 'Admin' or Role_baru == 'Pelanggan':
                        df.loc[df['Username'] == username, 'Role'] = Role_baru
                        df.to_csv('Akun.csv', index=False)  
                        input('    Role berhasil diubah!')
                        return KelolaAkun()
                    else:
                        print('    Tidak ada role yang cocok dengan input!')
                        continue
        elif Pilih == '3':
            break
        else:
            input('Input tidak sesuai! Tekan ENTER untuk melanjutkan!')

def PesanProduk(username):
    while True:
        os.system('cls')
        Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Lihat Paket!\n'
            '    2) Pesan Paket!\n'
            '    3) Lihat Paket Dipesan!\n'
            '    4) Batalkan Pesanan\n'
            '    5) Kembali\n'
        )

        Pilih = input('Pilih Menu! : ')
        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break
        elif Pilih == '2':
            dfproduk = pd.read_csv('Produk.csv')
            dfpesan = pd.read_csv('Pemesanan.csv')
            if dfproduk['Keterangan_Paket'].empty:
                input('    Belum ada produk!\n    Tekan ENTER untuk kembali!')
                continue
            else:
                
                os.system('cls')
                print(tabulate(dfproduk, headers='keys', tablefmt='fancy_grid'))
                print('    1) Kembali')
                KetPaket = input('Pilih paket yang ingin dipesan : ')
                if KetPaket in dfproduk['Keterangan_Paket'].values:
                    try:
                        JumlahPaket = int(input('Masukkan jumlah paket yang ingin dipesan : '))
                        stok_lama = dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'].iloc[0]
                        stok_baru = stok_lama - JumlahPaket
                        if stok_baru < 0:
                            input('Stok tidak mencukupi! tekan ENTER untuk lanjut!')
                            break
                    except:
                        input("Input Salah! Silahkan coba lagi!")
                    os.system('cls')
                    Baris = dfproduk[dfproduk['Keterangan_Paket'] == KetPaket]
                    harga_satuan = Baris['Harga'].iloc[0]
                    produk_paket = Baris['Produk_Paket'].iloc[0]
                    nama_paket = Baris['Keterangan_Paket'].iloc[0]
                    harga_total = harga_satuan * JumlahPaket
                    print('====================DETAIL PEMESANAN ===========================')
                    print('Paket yang dipesan : ', nama_paket )
                    print('Produk paket dipesan : ', produk_paket)
                    print('Jumlah Dibeli : ', JumlahPaket)
                    print('Harga Total : ', harga_total)
                    print('================================================================')
                    print(
                        '         1) Lanjutkan Pesanan          \n'
                        '         2) Batalkan Pesanan           \n'
                    )
                    while True:
                        Pilih = input('Apakah anda ingin melanjutkan pesanan? ( 1 \ 2 )')
                        if Pilih == '1':
                            while True:
                                try:
                                    Kontak = input('Silahkan masukkan nomor aktif untuk dihubungi : ')
                                    dfpesan = pd.concat([dfpesan, pd.DataFrame([{
                                        'username' : username,
                                        'Waktu_Pemesanan' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        'Paket_Dipesan' : KetPaket, 
                                        'Produk_Paket' : produk_paket, 
                                        'Jumlah' : JumlahPaket, 
                                        'Harga' : harga_total,
                                        'Status_Pemesanan' : "Pending",
                                        'Kontak_Pemesan' : "'" + Kontak
                                        }])], ignore_index=True)
                                    dfpesan.to_csv('Pemesanan.csv', index=False)
                                    dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'] = stok_baru
                                    dfproduk.to_csv('Produk.csv', index=False)
                                    print('Pesanan Berhasil Ditambahkan! Silahkan menunggu pesanan diproses!')
                                    print('======================== TERIMA KASIH ==========================')
                                    input('Tekan ENTER untuk melanjutkan!')
                                    return PesanProduk(username)
                                
                                except ValueError:
                                    print('Input tidak valid! Masukkan Angka!')
                        elif Pilih == '2':
                            return PesanProduk(username)
                        else:
                            print('Input tidak valid!')
                elif  KetPaket == "1":
                    break
                else:
                    print('Input tidak valid!')
        elif Pilih == "3":
            os.system('cls')
            df = pd.read_csv('Pemesanan.csv')
            df_tampilan = df.loc[
                df['username'] == username, 
                ['Waktu_Pemesanan', 'Paket_Dipesan', 'Produk_Paket', 'Jumlah', 'Harga', 'Status_Pemesanan']
                ]
            print(tabulate(df_tampilan, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break
        elif Pilih == '4':
            os.system('cls')
            df = pd.read_csv('Pemesanan.csv')
            df_tampilan = df.loc[
                df['username'] == username, 
                ['Waktu_Pemesanan', 'Paket_Dipesan', 'Produk_Paket', 'Jumlah', 'Harga', 'Status_Pemesanan']
                ]
            print(tabulate(df_tampilan, headers='keys', tablefmt='fancy_grid', showindex=True))
            try:
                indexpaket = int(input('    Masukkan Index yang ingin dihapus : '))
                if indexpaket in df.index:
                    dfproduk = pd.read_csv('Produk.csv')
                    Baris = df.loc[indexpaket]
                    KetPaket = Baris['Paket_Dipesan']
                    JumlahPaket = Baris['Jumlah']
                    stok_lama = dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'].iloc[0]
                    stok_baru = stok_lama + JumlahPaket
                    dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'] = stok_baru
                    dfproduk.to_csv('Produk.csv', index=False)
                    df = df.drop(indexpaket)
                    df.to_csv('Pemesanan.csv', index=False)
                    print('    Data berhasil di hapus!')
                    input('    Tekan ENTER untuk kembali!')
                    break
                else:
                    input('Index tidak ditemukan! tekan ENTER untuk lanjut!')
                    break
            except:
                input('Input salah! Masukkan Angka!')
        elif Pilih == '5':
            break
        else:
            input('Input tidak valid! tekan ENTER untuk lanjut!')

def EditAkun(role, username):
    while True:
        os.system('cls')
        Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Ganti Username\n'
            '    2) Ganti Password\n'
            '    3) Kembali'
        )

        Pilih = input('Pilih Menu : ')

    
        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Akun.csv')
            print('    Username Anda : ', username)
            print('    1) Kembali')
            username_baru = input('    Masukkan Username Baru : ')
            if username_baru == '1':
                break
            elif username_baru in df['Username'].values:
                print('    Username sudah digunakan!')
                input('    Tekan ENTER untuk melanjutkan')
                continue
            else:
                df.loc[df['Username'] == username, 'Username'] = username_baru
                df.to_csv('Akun.csv', index=False)  
                input('    Username berhasil diubah! Tekan ENTER untuk melanjutkan')
                username = username_baru
                if role == 'Pemilik':
                    return pemilik(role, username)
                elif role == 'Admin':
                    return admin(role, username)
                elif role == 'Pelanggan':
                    return pelanggan(role, username)
                
            
        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Akun.csv')
            print('    1) Kembali')
            password_lama = input('    Masukkan password lama :')
            if password_lama == '1':
                break
            elif password_lama == df.loc[df['Username'] == username, 'Password'].iloc[0]:
                password_baru = input('    Masukkan password baru : ')
                df.loc[df['Username'] == username, 'Password'] = password_baru
                df.to_csv('Akun.csv', index=False)  
                input('    Password berhasil diubah!')
                return EditAkun(role, username)
        elif Pilih == '3':
            break
        else:
            input('Input tidak Valid! Tekan ENTER untuk melanjutkan!')


def LaporanPenjualan():
    while True:
        os.system('cls')
        df = pd.read_csv('Pemesanan.csv')
        df_tampilan = df.loc[
            df['Status_Pemesanan'] == 'Selesai', 
            ['username', 'Waktu_Pemesanan', 'Paket_Dipesan', 'Produk_Paket', 'Jumlah', 'Harga']
            ]
        print(tabulate(df_tampilan, headers='keys', tablefmt='fancy_grid'))

        print(
            '    1) Pilih berdasarkan tanggal!\n'
            '    2) Kembali\n'
        )
         

def Feedback():
    while True:
        os.system('cls')
        Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Berikan Feedback!\n'
            '    2) Kembali'
        )

        Pilih = input('Pilih Menu ( 1 / 2 ): ')

        if Pilih == '1':
            
            df = pd.read_csv('Feedback.csv')
            Feedback = input("    Kirim Feedback mu sekarang! ( Akun akan disembunyikan ) : ")
            df = pd.concat([df, pd.DataFrame([{'Feedback' : Feedback}])], ignore_index=True)
            df.to_csv('Feedback.csv', index=False)
            print('    Terima kasih feedbacknya!!!!')
            input('    Tekan ENTER untuk melanjutkan')
            break

        elif Pilih == '2':
            break
        else:
            input('Input tidak valid! Tekan ENTER untuk melanjutkan!')
    
def MelihatFeedback():
    while True:
        os.system('cls')
        Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Lihat Feedback\n'
            '    2) Kembali'
        )

        Pilih = input('Pilih Menu ( 1 / 2 )')

        if Pilih == '1':
            
            os.system('cls')
            df = pd.read_csv('Feedback.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break

        elif Pilih == '2':
            break

def KelolaPesanan():
    while True:
        os.system('cls')
        Header = """
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== """
        print(Header)

        print(
            '    1) Lihat Pesanan\n'
            '    2) Ubah Status Pesanan\n'
            '    3) Kembali\n'
        )

        Pilih = input('Pilih Menu ( 1 / 2 / 3 ) : ')

        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Pemesanan.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break

        elif Pilih == '2':
            df = pd.read_csv('Pemesanan.csv')
            if df['Paket_Dipesan'].empty:
                os.system('cls')
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
                input('Tidak ada pesanan, tekan ENTER untuk melanjutkan!')
            else:
                os.system('cls')
                df = pd.read_csv('Pemesanan.csv')
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

                try:
                    nomorpesanan = int(input('Masukkan indeks pesanan yang ingin diubah : '))
                    if nomorpesanan in df.index:
                        print (
                            '    1) Selesai\n'
                            '    2) Diproses\n'
                            '    3) Pending\n'
                        )
                        statusUbah = input('Masukkan status pesanan baru : ')

                        if statusUbah == '1':
                            df.loc[nomorpesanan, 'Status_Pemesanan'] = 'Selesai'
                            df.to_csv('Pemesanan.csv', index=False)  
                            input('    Status berhasil diubah! tekan ENTER untuk melanjutkan')
                            break
                        if statusUbah == '2':
                            df.loc[nomorpesanan, 'Status_Pemesanan'] = 'Diproses'
                            df.to_csv('Pemesanan.csv', index=False) 
                            input('    Status berhasil diubah! tekan ENTER untuk melanjutkan')
                            break
                        if statusUbah == '3':
                            df.loc[nomorpesanan, 'Status_Pemesanan'] = 'Pending'
                            df.to_csv('Pemesanan.csv', index=False)
                            input('    Status berhasil diubah! tekan ENTER untuk melanjutkan')
                            break
                except ValueError:
                    input('Input salah! Masukkan Angka Indeks!')
                

        elif Pilih == '3':
            break
        else:
            input('Input tidak valid! tekan ENTER untuk melanjutkan!')

def logout():
    input ("============= Berhasil Logout! Tekan ENTER untuk benar benar logout! ==============")
    os.system('cls')
    exit()

menu()
    
