bilangan = int(input("Masukkan bilangan : "))
if bilangan > 0 :
    print (f"{bilangan} ," adalah bilangan positif ")
    if bilangan %2 == 0 :
        print (f"{bilangan} ," adalah bilangan genap")
    else:
    print (f"{bilangan} ," adalah bilangan ganjil")
elif  bilangan < 0 :
    print( f"{bilangan} ," adalah bilangan negatif ")
    if bilangan %2 == 0 :
        print (f"{bilangan} ," adalah bilangan genap")
    else:
    print (f"{bilangan} ," adalah bilangan ganjil")
else:
    print(f"{bilangan} ," adalah bilangan netral")