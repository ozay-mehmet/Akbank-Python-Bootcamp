import pyfiglet as pf   # pyfiglet kütüphanesi ascii art sanatı kullanılmak için import edildi
import tkinter as tk    # tkinter kütüphanesi import edildi

#  Kullanici adi tanimlandi
class User:
    def __init__(self,username):
        self.username = username

# Kütüphane sinifi tanimlandi
class Library:
    def __init__(self,name,author,year,page,bookType,publication):
        self.name = name
        self.author = author
        self.year = year
        self.page = page
        self.bookType = bookType
        self.publication = publication
        self.file = open("kitaplar.txt","a+")
     
    def kategori(self,bookType):
        for books in self.book_data:
            book_info = books.strip().split(", ")
            if bookType in book_info[4]:
                print(f'{book_info[0]}, {book_info[1]}')
            else:
                print(f"{bookType} turunde bir kitap degil.")
       
    #  Kitap listeleme fonksiyonu başladi                   
    def listele(self): 
        print("1 - Hepsi\t2 - Romanlar\t3 - Hikayeler\t4 - Masallar")
        sec = input("Listelemek istediğiniz kitabi/kitaplari girin: ")
        with open("kitaplar.txt", 'r') as file:
            self.book_data = file.readlines()
        self.file.seek(0)
        book_data = self.file.read().splitlines()               
        if sec == '1':
            for books in book_data:
                book_info = books.strip().split(",")
                print(f'{book_info[0]}, {book_info[1]}')
        elif sec == '2':
            self.kategori("roman")
        elif sec == '3':
            self.kategori("hikaye")
        elif sec == '4':
            self.kategori("masal")
        else:
            print("1-4 arasinda bir sayi girin")
        
    # Kitap ekleme fonksiyonu başladi  
    def ekle(self):
        self.name = input("Kitabin ismi nedir: ")
        self.author = input("Kitabin yazari kimdir: ")
        self.year = int(input("Kitap kac yilinda basilmistir: "))
        self.page = int(input("Kitap kac sayfadan olusmaktadir: "))
        self.bookType = input("Kitabinizin turu nedir: ")
        self.publication = input("Kitabinizin yayini nedir: ")
        self.file.write(f"{self.name}, {self.author}, {self.year}, {self.page}, {self.bookType}, {self.publication}\n")
        print(f"\n{self.author} tarafindan yazilan {self.name} isimli kitap listeye eklenmistir...\n")
        
    # Kitap silme fonksiyonu başladi 
    def sil(self):
        self.name = input("Silmek istediğiniz kitabin ismini yazin: ")
        with open("kitaplar.txt", "r") as file:
            satirlar = file.readlines()
        silinemeyecekler = [satir for satir in satirlar if self.name not in satir]
        with open("kitaplar.txt", "w") as file: 
            file.writelines(silinemeyecekler)
        if self.name in satirlar:
            print(f"\n{self.name} isimli kitap basariyla silinmistir...\n")
        else:   
           print(f"{self.name}, eklediginiz kitaplar listesinde bulunamadi :(\n")
           
    # Kitap siralama fonksiyonu cagrildi       
    def sirala(self):
        print("1 - Yayina Gore\t2 - Yazara Gore\t3 - Ture Gore")
        sira = input("Siralamak istediginiz turu secin: ")
        with open("kitaplar.txt", 'r') as file:
            book_data = [line.strip().split(',') for line in file]
        if(sira == '1'):        # kitap yayinini alfabetik bir sıraya göre sıralar      
            book_data.sort(key=lambda kitap: kitap[5])  # lambda fonksiyonu sort ile kullanilir ve herhangi bir islem tanimlamada kullanilir
            for book in book_data:
                print(f"{book[0]}")
        elif(sira == '2'):      # kitap yazarlarini alfabetik bir sıraya göre sıralar
            book_data.sort(key=lambda kitap: kitap[1])
            for book in book_data:
                print(f"{book[0]}")
        elif(sira == '3'):      # kitap turlerini alfabetik bir sıraya göre sıralar
            book_data.sort(key=lambda kitap: kitap[4])
            for book in book_data:
                print(f"{book[0]}")
        else:
            print("1-3 arasinda sayi girin")
            return
                   
    # Dosya Kapandi 
    def __del__(self):
        self.file.close()     
  
username = input("İsminiz nedir: ")
user = User(username)

# ASCII yazisi 
ascii_art = pf.figlet_format(f"{user.username} kütüphanemize hoşgeldin...\n")

# Tkinter kütüphanesi cagrildi
window = tk.Tk()
window.title("Akbank Python Bootcamp")

# ASCII yazisini pencerede gösterir
ascii_yazisi = tk.Label(window, text=ascii_art, font=("Courier", 12),fg="white",bg="black")
ascii_yazisi.pack()

window.mainloop()
                 
lib = Library("","",0,0,"","")    # Library classi cagrildi

while True: 
    print("\t====> MENU <====\t")
    print(" 1) Kitap Listele")
    print(" 2) Kitap Ekle")
    print(" 3) Kitap Sil")
    print(" 4) Kitaplari Sirala")
    print(" q) Cikis Yap")
    sec = input("Cikis yapmak için q harfine basin diger aktiviteleri yapmak için 1-3 arasinda bir sayi girin: ")
    if(sec == '1'):
        lib.listele()
    elif(sec == '2'):
        lib.ekle()
    elif(sec == '3'):
        lib.sil()
    elif(sec == '4'):
        lib.sirala()
    elif(sec == 'q'):
        print("Cikisiniz yapiliyor...")
        print("Yine bekleriz")
        break
    else:
        print("Hatali giris")        
