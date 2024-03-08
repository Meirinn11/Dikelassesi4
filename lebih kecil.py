Bill_1= int(input("Masukkan Angka ke 1:"))
Bill_2=int(input("Masukkan Angka ke 2:"))
Bill_3=int(input("Masukkan Angka ke 3:"))
if Bill_1 > Bill_2 > Bill_3:
    print("bilangan yang lebih kecil adalah",Bill_3)
elif Bill_1<Bill_2<Bill_3:
    print("bilangan yang lebih kecil adalah",Bill_1)
elif Bill_1 > Bill_2 < Bill_3:
    print("bilangan yang lebih kecil adalah",Bill_2)