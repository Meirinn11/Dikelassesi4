bil1 = int(input("Masukan bilangan 1 :"))
bil2 = int(input("Masukan bilanagan 2 :"))
bil3 = int(input("Masukan bilangan 3 :"))

if bil1 > bil2 and bil3 > bil2:
    print(bil1," dan ", bil3, " Lebih besar dari ",bil2)
elif bil2 > bil1 and bil3 > bil1:
    print(bil2, " dan ", bil3, " lebih besar dari ", bil1)
elif bil2 > bil3 and bil1 > bil3:
    print(bil1 , " dan ", bil2 , " lebih besar dari ", bil3)
elif bil1 == bil2 and bil1 > bil3:
    print(bil1, " dan ",bil2, " lebih besar dari ", bil3)
elif bil1 == bil3 and bil1 > bil2:
    print(bil1, " dan ",bil3, " lebih besar dari ", bil2)
elif bil2 == bil3 and bil2 > bil1:
    print(bil2, " dan ",bil3, " lebih besar dari ", bil1)
elif bil1 == bil2 and bil1 < bil3:
    print(bil1, " dan ",bil2, " lebih kecil dari ", bil3)
elif bil1 == bil3 and bil1 < bil2:
    print(bil1, " dan ",bil3, " lebih kecil dari ", bil2)
elif bil2 == bil3 and bil2 < bil1:
    print(bil2, " dan ",bil3, " lebih kecil dari ", bil1)
else:
    print(bil1, bil2, bil3, "sama besar")