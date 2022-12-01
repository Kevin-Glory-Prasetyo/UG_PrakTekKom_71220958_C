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





