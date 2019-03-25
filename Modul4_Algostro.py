class mhsTIF():
    def __init__(self, nama, asal, saku):
        self.nama = nama
        self.asal = asal
        self.saku = saku

c0 = mhsTIF('Ika','Sukoharjo',240000)
c1 = mhsTIF('Budi','Klaten', 260000)
c2 = mhsTIF('Ahmad','Salatiga',280000)
c3 = mhsTIF('Chandra','Klaten',220000)
c4 = mhsTIF('Eka','Surakarta',275000)
c5 = mhsTIF('Fandi','Salatiga',290000)
c6 = mhsTIF('Deni','Sukoharjo',252000)
c7 = mhsTIF('Galuh','Sukoharjo',245000)
c8 = mhsTIF('Janto','Sukoharjo',230000)
c9 = mhsTIF('Hasan','Sukoharjo',235000)
c10 = mhsTIF('Khalid','Sukoharjo',250000)

daftar = [c0,c1,c2,c3,c4,c5,c6]

#1
def cari(n):
    baru = []
    for i in range(len(n)):
        if(n[i].asal.lower() == 'klaten'):
            baru.append(i)
    return baru


#2
def sakuKcl(n):
    baru = n[0].saku
    for i in range(len(n)):
        if(n[i].saku<baru):
            baru = n[i].saku
    return baru

#3
def sakuKcl2(n):
    baru = n[0].saku
    list = []
    for i in range(len(n)):
        if(n[i].saku==baru):
            list.append(n[i].nama)
        elif(n[i].saku<baru):
            baru = n[i].saku
            list = []
            list.append(n[i].nama)
    return list

#4
def sakuKrg(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].saku < batas):
            list.append(n[i].nama)
    return list
print(cari(daftar))
print(sakuKcl(daftar))
print(sakuKcl2(daftar))

#5
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        return self.head
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
llist = LinkedList() 
llist.pushAw(21)
llist.pushAw(22)
llist.pushAw(12)
llist.pushAw(14)
llist.pushAw(2)
llist.pushAw(19)

print(llist.search(21))
print(llist.search(29))
print(sakuKrg(daftar))

#6
def binSe(list, target):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            return "target di index "+str(mid)
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid +1
    return "Target tidak ditemukan di index berapapun"

list = [2,4,6,9,12,27,39,46,59,77]
target = 12
print(binSe(list,target))
list = [2,4,6,9,12,27,39,46,59,77]
target = 133
print(binSe(list,target))

#7
def binSe(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2,3,4,5,8,8,9,12]
target = 8
print(binSe(kumpulan,target))

#8
#Untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
#yaitu dengan menggunakan Logaritma basis 2 (log2(n))
#misalkan :
#    apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
#    itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
#    dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128
#    apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
#    itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
    dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
