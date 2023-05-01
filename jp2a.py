import os,time,jp2a,sys

from time import sleep

def banner():
	print("""\033[33m
     ██╗██████╗ ██████╗  █████╗
     ██║██╔══██╗╚════██╗██╔══██╗
     ██║██████╔╝ █████╔╝███████║
██   ██║██╔═══╝ ██╔═══╝ ██╔══██║
╚█████╔╝██║     ███████╗██║  ██║
 ╚════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝\033[0m
\033[41m Pengubah Gambar menjadi ASCII \033[0m\n""")

def clear():
	os.system("clear")

def default():
	clear()
	banner()
	os.system("jp2a "+dir)

def border():
	clear()
	banner()
	os.system("jp2a --border "+dir)

def color():
	clear()
	banner()
	os.system("jp2a --colors "+dir)

def depth_color():
	clear()
	banner()
	warna = input("Pilih kode warna[mis, 4/8/24] ")
	join = "jp2a --color-depth="+warna+" "
	os.system(join+dir)

def balik_gambar():
	clear()
	banner()
	os.system("jp2a -i "+dir)

def output():
	clear()
	banner()
	file = input("Kasih nama : ")
	give = "jp2a --output="+file+" "
	os.system(give+dir)

def uk_panj_leb():
	clear()
	banner()
	uk = input("Ukuran [mis, 50x25] ")
	size = "jp2a --size="+uk+" "
	os.system(size+dir)

def info_lengkap():
	clear()
	banner()
	os.system("jp2a -v "+dir)

def ukuran():
	clear()
	banner()
	y = input("Ukuran [mis, 50] ")
	asu = "jp2a --width="+y+" "
	os.system(asu+dir)

pilihan = input("""
\033[0m+-------------------------------+
| \033[31mNo \033[0m| \033[32mPilihan                  \033[0m|
+-------------------------------+
| \033[31m1. \033[0m| \033[32mDefault                  \033[0m|
| \033[31m2. \033[0m| \033[32mBergaris tepi            \033[0m|
| \033[31m3. \033[0m| \033[32mWarna default            \033[0m|
| \033[31m4. \033[0m| \033[32mWarna pilihan            \033[0m|
| \033[31m5. \033[0m| \033[32mGambar dibalik           \033[0m|
| \033[31m6. \033[0m| \033[32mSimpan sbg file          \033[0m|
| \033[31m7. \033[0m| \033[32mPanjang × Lebar          \033[0m|
| \033[31m8. \033[0m| \033[32mInfo lengkap             \033[0m|
| \033[31m9. \033[0m| \033[32mUkuran                   \033[0m|
+-------------------------------+
\033[33mPilih angkanya saja! \033[0m""")

dir = input("\033[33mDirektori file : \033[32m")
if os.path.exists(dir):
	sleep(1)
	print("\033[32mFile ada!")
	sleep(1)
else:
	sleep(1)
	print("\033[31mFile tidak ada")
	sleep(1)

if pilihan == "1":
	default()
	sys.exit()

elif pilihan == "2":
	border()
	sys.exit()

elif pilihan == "3":
	color()
	sys.exit()

elif pilihan == "4":
	depth_color()
	print("\n")
	sys.exit()

elif pilihan == "5":
	balik_gambar()
	sys.exit()

elif pilihan == "6":
	output()
	sys.exit()

elif pilihan == "7":
	uk_panj_leb()
	sys.exit()

elif pilihan == "8":
	info_lengkap()
	sys.exit()

elif pilihan == "9":
	ukuran()
	sys.exit()
else:
	print("\033[31mPilihan tidak ada!")
	sys.exit()
