def penjumlahan(tiga,satu):
    hasil = tiga + satu
    return hasil

def pengurangan(tiga,satu):
    hasil = tiga - satu 
    return hasil

def perkalian(tiga,satu):
    hasil = tiga * satu
    return hasil

def pembagian(tiga,satu):
    hasil = tiga / satu
    return hasil

print("======================")
print('1.jumlah     [+]')
print('2.kurang     [-]')
print('3.kali       [*]')
print('4.bagi       [/]')
print("======================")
operasi = input("pilih operasi (1/2/3/4): ")
print("======================")
tiga = eval(input("masukan bilangan pertama : "))
satu = eval(input("masukan bilangan kedua : "))
if operasi == '1':
    print(f"hasil operasi dari ",tiga,"+",satu,"=",penjumlahan(tiga,satu))

elif operasi == '2':
    print(f"hasil operasi dari",tiga,"-",satu,"=",pengurangan(tiga,satu))

elif operasi == '3':
    print(f"hasil operasi dari",tiga,"*",satu,"=",perkalian(tiga,satu))

elif operasi == '4':
    print(f"hasil operasi dari",tiga,"/",satu,"=",pembagian(tiga,satu))



class Node:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        self.left = None
        self.right = None

def penduduk(puncak, nama, usia):
    if puncak is None:
        return Node(nama, usia)
    else:
        if nama < puncak.nama:
            puncak.left = penduduk(puncak.left, nama, usia)
        else:
            puncak.right = penduduk(puncak.right, nama, usia)
    return puncak

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value, self)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value, self)
            else:
                self.right.insert(value)
        else:
            return False
def urutan_usia(root):
    if root:
        urutan_usia(root.left)
        print(root.nama, "-", root.usia, "tahun")
        urutan_usia(root.right)

def urutan_nama(root):
    if root:
        urutan_usia(root.left)
        print(root.nama, "-", root.usia, "tahun")
        urutan_usia(root.right)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None)
        else:
            self.root.insert(value)
        self.size += 1

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def print(self):
        self.inorder(self.root)
        print()

    def binarySearch(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self.binarySearch(node.left, value)
        else:
            return self.binarySearch(node.right, value)

    def search(self, value):
        return self.binarySearch(self.root, value) is not None

    def reverse(self):
        self.reverseInorder(self.root)
        print()
        

root = None

while True:
    print("\nPilih Menu:")
    print("1. Tambah Penduduk\n2. Tampilkan Urut Nama\n3. Tampilkan Urut Usia")
    
    try:
        pilihan = int(input("Pilihan Anda: "))
    except ValueError:
        print("Masukkan angka sebagai pilihan.")
        continue

    if pilihan == 1:
        nama = input("Masukkan Nama: ")
        try:
            usia = int(input("Masukkan Usia: "))
        except ValueError:
            print("Masukkan angka sebagai usia.")
            continue

        root = penduduk(root, nama, usia)
        print("Data berhasil ditambahkan!")

    elif pilihan == 2:
        print("Daftar Penduduk:")
        urutan_usia(root)

    elif pilihan == 3:
        print("Daftar Penduduk:")
        urutan_nama(root)

    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")







