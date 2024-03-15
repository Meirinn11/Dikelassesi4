bil1 = int(input("masukan bilangan pertama: "))
bil2 = int(input("masukan bilangan kedua: "))
bil3 = int(input("masukan bilangan ketiga: "))

if bil1 < bil2 and bil1 < bil3 :
    print (f"{bil1} lebih kecil dari pada {bil2} dan {bil3}")
else:
    print (f"{bil1} lebih besar dari pada {bil2} dan {bil3}")