import pandas as pd
import os
from tabulate import tabulate
import datetime
import textwrap

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
    df = pd.DataFrame({'Keterangan_Paket': [], 'Produk_Paket': [], 'Stok_Paket' : [], 'Deskripsi_Produk' : [], 'Harga' : []})
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
    df = pd.DataFrame({'Username' : [], 'Feedback': [], 'Balasan' : []})
    df.to_csv('Feedback.csv', index=False)


# ================== REGISTER / LOGIN ====================

def header():
    print('''
    ==================================================================

    ░█████╗░░██████╗░██████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
    ███████║██║░░██╗░██████╔╝██║░░██║██████╔╝███████║██║░░╚═╝█████═╝░
    ██╔══██║██║░░╚██╗██╔══██╗██║░░██║██╔═══╝░██╔══██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                   SOLUSI PINTAR UNTUK PETANI TEMBAKAU

    ================================================================== ''')

def menu():
    os.system('cls')
    header()

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
    while True:
        os.system('cls')
        header()
        print(
            '\n                            INFORMASI SINGKAT                         '
            '\n    =================================================================='
            '\n    Username harus lebih dari 8 karakter!'
            '\n    Gunakan kombinasi huruf besar, huruf kecil, karakter unik serta'
            '\n    angka agar passwordmu susah untuk ditembus hacker!' 
            '\n    =================================================================='
            )

        df = pd.read_csv('Akun.csv')

        try:
            username = input('\n    Masukkan Username : ')
            if len(username) < 8:
                input('    Username minimal memiliki 8 karakter! Tekan ENTER untuk melanjutkan!')
                continue
            if username in df['Username'].values:
                print('    Username sudah digunakan!')
                input('    Tekan ENTER untuk melanjutkan')
                return register()
            
            password = input('    Masukkan Password : ')
            if len(password) < 8:
                input('    Panjang password minimal 8! Tekan ENTER untuk melanjutkan!')
                continue

            Keamanan = CekPassword(password)

            if Keamanan == False:
                print('    Passwordmu masih cukup lemah! coba gunakan karakter unik seperti "!@#$%^&*()" dan angka!')
                input('    Tekan ENTER untuk melanjutkan')
            elif Keamanan == True:
                input('    Registrasi berhasil! tekan ENTER untuk melanjutkan!')
                df = pd.read_csv('Akun.csv')
                df = pd.concat([df, pd.DataFrame([{'Username' : username, 'Password' : password, 'Role' : 'Pelanggan'}])], ignore_index=True)
                df.to_csv('Akun.csv', index=False)
                input('    Akun Berhasil Ditambahkan! Tekan ENTER untuk melanjutkan')
                break

        except ValueError:
            print('    Password atau Username tidak valid!')
            input('    Tekan ENTER untuk melanjutkan')
            break

def CekPassword(password):
    PoinKeamanan = 0
    HurufBesar = False
    HurufKecil = False
    Angka = False
    Simbol = False
    for i in password:
        if i == i.upper() :
            HurufBesar = True
        if i == i.lower() :
            HurufKecil = True
        if i in "0123456789":
            Angka = True
        if i in "!@#$%^&*()":
            Simbol = True
    if HurufBesar == True:
        PoinKeamanan += 2
    if HurufKecil == True:
        PoinKeamanan += 3
    if Angka == True:
        PoinKeamanan += 1
    if Simbol == True:
        PoinKeamanan += 1
    
    if PoinKeamanan >= 2 and PoinKeamanan <= 4:
        Keamanan = False
    elif PoinKeamanan >= 6 and PoinKeamanan <= 7:
        Keamanan = True

    return Keamanan

    



def login():
    while True:

        os.system('cls')
        header()

        username = input('\n    Masukkan Username : ')
        password = input('    Masukkan Password : ')

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
            continue

def pemilik(role, username):
    while True:
        os.system('cls')
        header()

        print(
            '    1) Kelola Akun Admin\n'
            '    2) Kelola Produk\n'
            '    3) Melihat Laporan Penjualan\n'
            '    4) Feedback\n'
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
            MelihatFeedback(username)
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
        header()

        print(
            '    1) Pesan Produk Untuk Pelanggan \n'
            '    2) Kelola Pesanan\n'
            '    3) Kelola Produk\n'
            '    4) Feedback\n'
            '    5) Edit Akun\n'
            '    6) Logout\n'
        )


        Pilih = input('    Pilih Menu! ( 1 / 2 / 3 / 4 ) : ')
        if Pilih == '1':
            PesanProduk(role, username)
        if Pilih == '2':
            KelolaPesanan()
        elif Pilih == '3':
            KelolaProduk(role, username)
        elif Pilih == '4':
            MelihatFeedback(username)
        elif Pilih == '5':
            EditAkun(role, username)
        elif Pilih == '6':
            logout()
        else:
            print('    Input tidak valid! Silahkan pilih lagi')
            input('    Tekan ENTER untuk melanjutkan')
            continue

def pelanggan(role, username):
    while True:
        os.system('cls')
        header()

        print(
            '    1) Pesan Produk!\n'
            '    2) Edit Akun\n'
            '    3) Feedback\n'
            '    4) Logout\n'
        )


        Pilih = input('    Pilih Menu! ( 1 / 2 / 3 / 4 ) : ')
        if Pilih == '1':
            PesanProduk(role, username)
        elif Pilih == '2':
            EditAkun(role, username)
        elif Pilih == '3':
            Feedback(username)
        elif Pilih == '4':
            logout()
        else:
            print('    Input tidak valid! Silahkan pilih lagi')

        

def KelolaProduk(role, username):
    while True:
        os.system('cls')
        header()

        print(
            '    1) Tampilkan Paket\n'
            '    2) Tambah Paket\n'
            '    3) Edit Paket\n'
            '    4) Hapus Paket\n'
            '    5) Kembali\n'
        )
        Pilih = input("    Pilih Menu! ( 1 / 2 / 3 / 4 / 5 ) : ")
        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            df.index += 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
            input('Tekan ENTER untuk kembali!')
            break
        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Produk.csv')
            df.index += 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
            KetPaket_baru = textwrap.fill(input('Masukkan Keterangan Paket : '), 50)
            if KetPaket_baru in df['Keterangan_Paket'].values:
                input('Keterangan paket sudah ada! Tekan ENTER untuk kembali!')
            else:
                Produk_baru = textwrap.fill(input('Masukkan Produk : '), 50) 
                Deskripsi = textwrap.fill(input('Masukkan Deskripsi Produk : '), 100) 

                while True:
                    try:
                        Stok = int(input('Masukkan Stok Paket : '))
                        if Stok < 1:
                            input('Stok tidak bisa kurang dari 1! Tekan ENTER untuk melanjutkan!')
                        else:
                            while True:
                                try:
                                    Harga_baru = int(input("Masukkan Harga Paket : "))   
                                    if Harga_baru < 0:
                                        input('Harga tidak bisa kurang dari 0! Tekan ENTER untuk melanjutkan!')
                                    else:
                                        df = pd.concat([df, pd.DataFrame([{'Keterangan_Paket' : KetPaket_baru, 'Produk_Paket' : Produk_baru, 'Deskripsi_Produk' : Deskripsi, 'Stok_Paket' : Stok, 'Harga' : Harga_baru}])], ignore_index=True)
                                        df.to_csv('Produk.csv', index=False)
                                        print('Produk Berhasil Ditambahkan!')
                                        input('Tekan ENTER untuk melanjutkan')
                                        return KelolaProduk(role, username)
                                except ValueError:
                                    input('Input tidak valid! Masukkan Angka!')
                    except ValueError:
                        input('Stok tidak valid! Masukkan Angka!')
                        continue

        elif Pilih == '3':
            editproduk(role, username)
        elif Pilih == '4':
            while True:
                df = pd.read_csv('Produk.csv')
                if df['Keterangan_Paket'].empty:
                    input('Paket produk tidak ada! Tekan ENTER untuk kembali!')
                    break
                else: 
                    os.system('cls')
                    df = pd.read_csv('Produk.csv')
                    df.index += 1
                    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
                    KetPaket = input('Masukkan paket yang ingin dihapus! : ')
                    

                    if KetPaket in df['Keterangan_Paket'].values:
                        df = df[df['Keterangan_Paket'] != KetPaket]
                        df.to_csv('Produk.csv', index=False)
                        print('Data berhasil di hapus!')
                        input('Tekan ENTER untuk kembali!')
                        break
                    else:
                        input('Paket tidak ada! Tekan ENTER untuk kembali!')
                    
        elif Pilih == '5':
            break
        else:
            input('Input tidak valid! tekan ENTER untuk melanjutkan')

                        

def editproduk(role, username):
    while True:
        df = pd.read_csv('Produk.csv')
        if df.empty:
            os.system('cls')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tidak ada produk yang bisa di edit! Tekan ENTER untuk kembali!')
            break
        else:
            os.system('cls')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            print(
                '1) Keterangan Paket\n'
                '2) Produk Paket\n'
                '3) Harga\n'
                '4) Stok Paket\n'
                '5) Deskripsi Paket\n'
                '6) Kembali\n'
            )

            Pilih = input("Pilih data yang ingin diubah! ( 1 / 2 / 3 / 4 ) : ")
            
            if Pilih == '1':
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                df.index += 1
                print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
                while True:
                    KetPaket_lama = textwrap.fill(input('Masukkan keterangan paket yang ingin diubah : '), 50)
                    if KetPaket_lama in df['Keterangan_Paket'].values:
                        KetPaket_baru = textwrap.fill(input('Masukkan keterangan paket yang baru! : '), 50)
                        df.loc[df['Keterangan_Paket'] == KetPaket_lama, 'Keterangan_Paket'] = KetPaket_baru
                        df.to_csv('Produk.csv', index=False)   
                        input('Paket Berhasil Dirubah! Tekan ENTER untuk kembali')
                        break
                    else: 
                        input('Keterangan paket tidak ditemukan! Tekan ENTER untuk melanjutkan! ')
                        break
                    
            elif Pilih == '2':
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                df.index += 1
                print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
                while True:
                    KetPaket = textwrap.fill(input('Masukkan keterangan paket yang ingin diubah produknya! : '), 50)
                    if KetPaket in df['Keterangan_Paket'].values:
                        Produk_baru = textwrap.fill(input('Masukkan produk yang baru! : '), 50)
                        df.loc[df['Keterangan_Paket'] == KetPaket, 'Produk_Paket'] = Produk_baru
                        df.to_csv('Produk.csv', index=False)    
                        input('Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                        break
                    else:
                        input('Keterangan paket tidak ditemukan! tekan ENTER untuk melanjutkan!')
                        break

            elif Pilih == '3':
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                df.index += 1
                print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
                while True:
                    KetPaket = textwrap.fill(input('Masukkan keterangan paket yang ingin diubah harganya! : '), 50)
                    if KetPaket in df['Keterangan_Paket'].values:
                        try:
                            Harga_baru = int(input('Masukkan Harga Baru : '))
                            if Harga_baru < 0:
                                input('Harga tidak boleh kurang dari 0! Tekan ENTER untuk melanjutkan!')
                                break 
                            else:
                                df.loc[df['Keterangan_Paket'] == KetPaket, 'Harga'] = Harga_baru
                                df.to_csv('Produk.csv', index=False)  
                                input('Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                                break
                        except ValueError:
                            input('Input tidak valid! Masukkan Angka!')
                            break
                    else:
                        input('Keterangan paket tidak ditemukan! tekan ENTER untuk melanjutkan!')

            elif Pilih == '4':
                os.system('cls')
                df = pd.read_csv('Produk.csv')
                df.index += 1
                print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
                while True:
                    KetPaket = textwrap.fill(input('Masukkan keterangan paket yang ingin diubah stoknya! : '), 50)
                    if KetPaket in df['Keterangan_Paket'].values:
                        try:
                            Stok_baru = int(input('Masukkan Stok Baru : '))
                            if Stok_baru < 1:
                                input('Stok tidak boleh kurang dari 1! Tekan ENTER untuk melanjutkan!')
                                continue
                            else:
                                df.loc[df['Keterangan_Paket'] == KetPaket, 'Stok_Paket'] = Stok_baru
                                df.to_csv('Produk.csv', index=False)  
                                input('Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                                break
                        except ValueError:
                            input('Input tidak valid! Masukkang angka!')   
                    else:
                        input('Keterangan paket tidak ditemukan! tekan ENTER untuk melanjutkan!') 

            elif Pilih == '5':
                while True:
                    KetPaket = textwrap.fill(input('Masukkan keterangan paket yang ingin diubah deskripsinya! : '), 50)
                    if KetPaket in df['Keterangan_Paket'].values:
                        Deskripsi = textwrap.fill(input('Masukkan deskripsi produk yang baru! : '), 100)
                        df.loc[df['Keterangan_Paket'] == KetPaket, 'Deskripsi_Produk'] = Deskripsi
                        df.to_csv('Produk.csv', index=False)   
                        input('Deskripsi Produk Berhasil Dirubah! Tekan ENTER untuk kembali')
                        break
                    else:
                        input('Keterangan paket tidak ditemukan! tekan ENTER untuk melanjutkan!')
            
            elif Pilih == '6':
                break

            else:
                input('Input salah! tekan ENTER untuk melanjutkan!')

def KelolaAkun():
    while True:
        os.system('cls')
        header()

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
            df.index += 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
            input('Tekan ENTER untuk kembali!')
            break
        elif Pilih == '2':
            while True:
                os.system('cls')
                df = pd.read_csv('Akun.csv')
                df_tampilan = df[['Username', 'Role']]
                df_tampilan.index += 1
                print(tabulate(df_tampilan, headers='keys', tablefmt='fancy_grid', showindex=True))
                username = input('Masukkan username yang ingin diubah role : ')
                if username in df['Username'].values:
                    while True: 
                        Role_baru = input('Masukkan Role Baru (Pemilik / Admin / Pelanggan) : ')
                        if Role_baru == 'Pemilik' or Role_baru == 'Admin' or Role_baru == 'Pelanggan':
                            df.loc[df['Username'] == username, 'Role'] = Role_baru
                            df.to_csv('Akun.csv', index=False)  
                            input('Role berhasil diubah!')
                            return 
                        else:
                            print('Tidak ada role yang cocok dengan input!')
                else:
                    input('Username tidak ditemukan! Tekan ENTER untuk melanjutkan!')

        elif Pilih == '3':
            break
        else:
            input('Input tidak sesuai! Tekan ENTER untuk melanjutkan!')

def PesanProduk(role, username):
    while True:
        os.system('cls')
        header()

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
            df.index += 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
            input('    Tekan ENTER untuk kembali!')
            continue
        elif Pilih == '2':
            dfproduk = pd.read_csv('Produk.csv')
            dfproduk.index += 1
            dfpesan = pd.read_csv('Pemesanan.csv')
            dfpesan.index += 1
            if dfproduk['Keterangan_Paket'].empty:
                input('Belum ada produk! Tekan ENTER untuk kembali!')
            else:
                while True:
                    os.system('cls')
                    df_tampilanProduk = dfproduk.loc[
                        dfproduk['Stok_Paket'] > 0, 
                        ['Keterangan_Paket', 'Produk_Paket','Stok_Paket','Harga']
                        ]
                    print(tabulate(df_tampilanProduk, headers='keys', tablefmt='fancy_grid', showindex=True))
                    print('1) Kembali')
                    KetPaket = input('Ketik paket yang ingin dipesan ( Ketika "1" untuk kembali! ): ')

                    if KetPaket in dfproduk['Keterangan_Paket'].values:
                        while True:
                            os.system('cls')
                            Baris = dfproduk[dfproduk['Keterangan_Paket'] == KetPaket]
                            harga_satuan = Baris['Harga'].iloc[0]
                            produk_paket = Baris['Produk_Paket'].iloc[0]
                            stok_paket = Baris['Stok_Paket'].iloc[0]
                            deskripsi_produk = textwrap.fill(Baris['Deskripsi_Produk'].iloc[0], 100, subsequent_indent=' ' * len('Deksripsi produk : '))
                            nama_paket = Baris['Keterangan_Paket'].iloc[0]
                            print('==================== DETAIL PAKET ===========================')
                            print('Paket yang dipesan : ', nama_paket )
                            print('Produk paket dipesan : ', produk_paket)
                            print('Deskripsi produk :', deskripsi_produk)
                            print('Stok Paket : ', stok_paket)
                            print('Harga per paket : ', harga_satuan)
                            print('================================================================')
                            print(
                                '         1) Lanjutkan Pesanan          \n'
                                '         2) Batalkan Pesanan           \n'
                            )
                            Pilih = input('Apakah anda ingin melanjutkan pesanan? ( 1 \ 2 )')
                            if Pilih == '1':
                                while True:
                                    try:
                                        JumlahPaket = int(input('Masukkan jumlah paket yang ingin dipesan : '))
                                        stok_lama = dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'].iloc[0]
                                        stok_baru = stok_lama - JumlahPaket
                                        if JumlahPaket < 1:
                                            input('Jumlah paket yang dibeli tidak boleh kurang dari 1! Tekan ENTER untuk melanjutkan!')
                                        elif JumlahPaket > stok_lama:
                                            input('Stok tidak mencukupi! tekan ENTER untuk lanjut!')
                                        else:
                                            harga_total = harga_satuan * JumlahPaket
                                            Kontak = input('Silahkan masukkan nomor aktif untuk dihubungi : ')
                                            if role == 'Admin':
                                                status_pemesanan = 'Diproses'
                                            elif role == 'Pelanggan':
                                                status_pemesanan = 'Pending'
                                            dfpesan = pd.concat([dfpesan, pd.DataFrame([{
                                                'username' : username,
                                                'Waktu_Pemesanan' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                'Paket_Dipesan' : KetPaket, 
                                                'Produk_Paket' : produk_paket, 
                                                'Jumlah' : JumlahPaket, 
                                                'Harga' : harga_total,
                                                'Status_Pemesanan' : status_pemesanan,
                                                'Kontak_Pemesan' : "'" + Kontak
                                                }])], ignore_index=True)
                                            dfpesan.to_csv('Pemesanan.csv', index=False)
                                            dfproduk.loc[dfproduk['Keterangan_Paket'] == KetPaket, 'Stok_Paket'] = stok_baru
                                            dfproduk.to_csv('Produk.csv', index=False)
                                            print('Pesanan Berhasil Ditambahkan! Silahkan menunggu pesanan diproses!')
                                            print('======================== TERIMA KASIH ==========================')
                                            input('Tekan ENTER untuk melanjutkan!')
                                            return PesanProduk(role, username)
                                        
                                    except ValueError:
                                        print('Input tidak valid! Masukkan Angka!')
                            elif Pilih == '2':
                                return PesanProduk(role, username)
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
            df.index += 1
            df_tampilan = df.loc[
                (df['username'] == username) & (df['Status_Pemesanan'] == 'Pending'), 
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
        header()

        print(
            '1) Ganti Username\n'
            '2) Ganti Password\n'
            '3) Kembali'
        )

        Pilih = input('Pilih Menu : ')

    
        if Pilih == '1':
            while True:
                os.system('cls')
                df = pd.read_csv('Akun.csv')
                print('Username Anda : ', username)
                print('1) Kembali')
                username_baru = input('Masukkan Username Baru ( "1" Untuk Kembali! ): ')
                if username_baru == '1':
                    break
                elif username_baru in df['Username'].values:
                    print('Username sudah digunakan!')
                    input('Tekan ENTER untuk melanjutkan')
                else:
                    df.loc[df['Username'] == username, 'Username'] = username_baru
                    df.to_csv('Akun.csv', index=False)  
                    input('Username berhasil diubah! Tekan ENTER untuk melanjutkan')
                    username = username_baru
                    if role == 'Pemilik':
                        return pemilik(role, username)
                    elif role == 'Admin':
                        return admin(role, username)
                    elif role == 'Pelanggan':
                        return pelanggan(role, username)
                    
            
        elif Pilih == '2':
            while True:
                os.system('cls')
                df = pd.read_csv('Akun.csv')
                print('1) Kembali')
                password_lama = input('Masukkan password lama ( "1" Untuk Kembali ):')
                if password_lama == '1':
                    break
                elif password_lama == df.loc[df['Username'] == username, 'Password'].iloc[0]:
                    password_baru = input('Masukkan password baru : ')    
                    Keamanan = CekPassword(password_baru)
                    if Keamanan == False:
                        print('Passwordmu masih cukup lemah! coba gunakan karakter unik seperti "!@#$%^&*()" dan angka!')
                        input('Tekan ENTER untuk melanjutkan')
                    elif Keamanan == True:
                        df = pd.read_csv('Akun.csv')
                        df.loc[df['Username'] == username, 'Password'] = password_baru
                        df.to_csv('Akun.csv', index=False)  
                        input('Password berhasil diubah! Tekan ENTER untuk melanjutkan')
                        break
                else:
                    input('Password lama salah! Silahkan coba lagi!')
        elif Pilih == '3':
            break
        else:
            input('Input tidak Valid! Tekan ENTER untuk melanjutkan!')


def LaporanPenjualan():
    while True:
        os.system('cls')
        header()

        print(
            '    1) Laporan per produk!\n'
            '    2) Laporan per periode!\n'
            '    3) Laporan Keseluruhan!\n'
            '    4) Kembali'
        )

        Pilih = input('Pilih Menu ( 1 / 2 / 3 / 4 ) : ')

        if Pilih == '1':
            os.system('cls')
            df = pd.read_csv('Pemesanan.csv')
            df_laporan = df.groupby('Produk_Paket').agg({
                'Jumlah' : 'sum',
                'Harga' : 'sum'
            }).reset_index()
            df_laporan.index += 1
            print(tabulate(df_laporan, headers='keys', tablefmt='fancy_grid', showindex=True))
            input('Tekan ENTER untuk kembali!')

        elif Pilih == '2':
            while True:
                os.system('cls')
                header()
                df = pd.read_csv('Pemesanan.csv')
                df['Waktu_Pemesanan'] = pd.to_datetime(df['Waktu_Pemesanan'], format='%Y-%m-%d %H:%M:%S')

                try:
                    print("    Masukkan tanggal dengan format (DD-MM-YYYY)!")
                    tanggalawal = input("    Masukkan tanggal awal: ").strip()
                    tanggalakhir = input("    Masukkan tanggal akhir: ").strip()
                    
                    tanggalawal = pd.to_datetime(tanggalawal, format='%d-%m-%Y')
                    tanggalakhir = pd.to_datetime(tanggalakhir, format='%d-%m-%Y')
                    
                    if tanggalawal > tanggalakhir:
                        input("    Tanggal awal tidak boleh lebih besar dari tanggal akhir! Tekan ENTER untuk melanjutkan!")
                        continue

                    tanggalakhir_filter = tanggalakhir + pd.Timedelta(days=1)
                    break
                except (ValueError, AttributeError):
                    input("    Format tanggal salah! Gunakan format DD-MM-YYYY! Tekan ENTER untuk melanjutkan!")
            while True:  
                rentangwaktu = df[
                    (df['Waktu_Pemesanan'] >= tanggalawal) & 
                    (df['Waktu_Pemesanan'] < tanggalakhir_filter)
                ]

                laporan = rentangwaktu.groupby(rentangwaktu['Waktu_Pemesanan'].dt.date).agg({
                    'Jumlah' : 'sum',
                    'Harga': 'sum'
                    }).reset_index()
                laporan.index += 1

                print(f"\nLaporan Keuntungan {tanggalawal} s/d {tanggalakhir}:\n")

                if len(laporan) > 0:
                    os.system('cls')
                    print(tabulate(laporan, headers='keys', tablefmt='fancy_grid'))
                    print(f"\nTotal Keuntungan: Rp {laporan['Harga'].sum():,.0f}")
                    input('Tekan ENTER untuk melanjutkan!')
                    break
                else:
                    os.system('cls')
                    header()
                    input("\n    Tidak ada transaksi pada periode tersebut! tekan ENTER untuk melanjutkan!")
                    break
        elif Pilih == '3':
            os.system('cls')
            df = pd.read_csv('Pemesanan.csv')
            laporan = df['Harga'].sum()
            print("\nLaporan Keseluruhan : ")
            print(f"Total Keuntungan: Rp {laporan:,.0f}")
            input('\n\n Tekan ENTER untuk melanjutkan!')

        elif Pilih == '4':
            break

        else:
            input('Input tidak valid! Tekan ENTER untuk melanjutkan!')


def Feedback(username):
    while True:
        os.system('cls')
        header()
        
        print(
            '    1) Berikan Feedback!\n'
            '    2) Lihat Feedbackmu!\n'
            '    3) Kembali'
        )

        Pilih = input('Pilih Menu ( 1 / 2 ): ')

        if Pilih == '1':
            os.system('cls')
            header()
            df = pd.read_csv('Feedback.csv')
            Feedback = textwrap.fill(input("    Kirim Feedback mu sekarang! ( Akun akan disembunyikan ) : "), 60)
            df = pd.concat([df, pd.DataFrame([{'Username' : username,'Feedback' : Feedback, 'Balasan' : 'Pesan Belom Dibalas'}])], ignore_index=True)
            df.to_csv('Feedback.csv', index=False)
            print('    Terima kasih feedbacknya!!!!')
            input('    Tekan ENTER untuk melanjutkan')
            break
        
        elif Pilih == '2':            
            os.system('cls')
            df = pd.read_csv('Feedback.csv')
            df = df.loc[
                df['Username'] == username, 
                ['Feedback', 'Balasan']
                ]
            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
            input('Tekan ENTER untuk kembali!')
            break


        elif Pilih == '3':
            break
        else:
            input('Input tidak valid! Tekan ENTER untuk melanjutkan!')
    
def MelihatFeedback(username):
    while True:
        os.system('cls')
        header()

        print(
            '    1) Lihat Feedback\n'
            '    2) Balas Feedback\n'
            '    3) Kembali'
        )

        Pilih = input('Pilih Menu ( 1 / 2 / 3 )')

        if Pilih == '1':
            
            os.system('cls')
            df = pd.read_csv('Feedback.csv')
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            input('Tekan ENTER untuk kembali!')
            break

        elif Pilih == '2':
            os.system('cls')
            df = pd.read_csv('Feedback.csv')
            df.index += 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            try:
                indexfeedback = int(input('    Masukkan Index dibalas : '))
                if indexfeedback in df.index:
                    Balasan = textwrap.fill(input("Kirimkan balasan! : "), 60)
                    df.loc[indexfeedback, 'Balasan'] = Balasan
                    df.to_csv('Feedback.csv', index=False)
                    input('Balasan berhasil di kirimkan! Tekan ENTER untuk melanjutkan')
                else:
                    input('Index tidak ditemukan! tekan ENTER untuk lanjut!')
            except ValueError:
                input('Input tidak valid! Masukkan Angka!')

        elif Pilih == '3':
            break

def KelolaPesanan():
    while True:
        os.system('cls')
        header()

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
    os.system('cls')
    header()
    input ("\n============= Berhasil Logout! Tekan ENTER untuk benar benar logout! ==============")
    os.system('cls')
    exit()


menu()
    
