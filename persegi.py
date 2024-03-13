print('##  Program Python Menghitung Luas Persegi  ##')
print('==============================================')
print()
 
def hitungLuasPersegi(sisi_persegi):
  return round(sisi_persegi * sisi_persegi,2)
 
sisi_persegi = float(input('Input panjang sisi persegi: '))
print('Luas persegi = ',hitungLuasPersegi(sisi_persegi))


#Hitung Luas Segitiga

def luas_segitiga():
    a = int(input("Masukkan alas segitiga : "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)


luas_segitiga()
