from datetime import timedelta, datetime
from time import sleep

class Antrian:
    def __init__(self):
        self.items=[]
    def data(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def rear(self):
        return self.items[0]
    def front(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
def menu():
    print ("\n=============================== APLIKASI ANTRIAN PEMBUATAN SIM ==========================================\n")
    print ("DIMOHON UNTUK PENGANTRI SEGERA MELAKUKAN PENGISIAN DATA DIRI TERLEBIH DAHULU SEBELUM MENGANTRI LOKET PEMBUATAN SIM")
    print ("                DIMOHON KEPADA SAUDARA UNTUK BISA MENUNGGU ANTRIAN DENGAN TERTIB                    \n")

menu()
    
def antrian():
    endtime = datetime.now() + timedelta(seconds = 2)
    tanda='n'
    m = Antrian()
    cad = Antrian()
    inputan = int(input('\n\nMasukan Pengantri Yang Malakukan Pendaftaran = '))
    for i in range(inputan):
        nama = input('Masukan Nama Pengantri %i =  '%(i+1))
        m.enqueue(nama)
        cad.enqueue(nama)

    print("Estimasi Jam Pelayanan\n")
    while not m.data():
        if not m.data():
            if tanda=='n':
                print(m.dequeue(),'Akan Dilayani Pada :',datetime.now())
                tanda=''
            else:
                print(m.dequeue(),'Akan Dilayani Pada :',datetime.now())
                endtime = endtime + timedelta(seconds = 8)

    tanda='n'
    print("\n=========================== ANTRIAN =====================================")
    while not cad.data():
        if not cad.data():
            if tanda==0:
                print(cad.dequeue(),'Sedang Dilayani')
                tanda=1
            else:
                sleep(2)
                print(cad.dequeue(),'Sedang Dilayani')
                
        if cad.data():
            print('============= MAAF KAMI TIDAK MELAYANI ANTRIAN ====================\n\n')
            
data=[]
pilih = "Y"
while pilih == "Y":
    print("\nMasukkan Data")
    npm = input("ID = ")
    nama = input("Nama = ")
    alamat = input("Alamat = ")
    a = data.append([npm,nama,alamat])
    pilih = input("Masukkan Data Lagi ? (Y/N) =")


antrian()

a = data
b = input("cari ID = ")

found=0
for x in range(len(a)):
    for y in range(len(a)):
        if a[x][y]==b:
            print(a[x])
            found=found+1
if found == 0 :
    print("tidak ditemukan")


        


            
