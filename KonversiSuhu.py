print ("Apa yang ingin anda coba konversi ? celcius / fahrenheit")
derajat = int(input("Angka suhu: "))
suhu = str(input("Dari jenis suhu : "))
suhu2 = str(input("Ke jenis suhu : "))

if suhu == "celcius":
    hasil= derajat *1.8+32
else:
    hasil = ((derajat-32)*5)/9


print(derajat, suhu, " di konversikan menjadi ",hasil, suhu2)