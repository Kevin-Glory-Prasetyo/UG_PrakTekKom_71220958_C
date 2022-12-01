print("periksa kelipatan")
mlebu = int(input("masukan angka : "))
def kelipatan_sembilan():
    answer = (mlebu%9)
    return answer


if kelipatan_sembilan()==0:
    print("BENAR")

else :
    print("SALAH")



