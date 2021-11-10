print("""
BEDEN KİTLE ENDEKSİ""")

Boy=float(input("Boyunuzu Giriniz:"))
Kilo=float(input("Kilonuzu Giriniz:"))

Beden_Kitle_Endeksi=Kilo/Boy**2
print("Beden Kitle Endeksi: {}".format(Beden_Kitle_Endeksi))

if Beden_Kitle_Endeksi < 18.5 :
    print("Zayıf")
elif Beden_Kitle_Endeksi >= 18.5 and Beden_Kitle_Endeksi <25:
    print("Normal")
elif Beden_Kitle_Endeksi >= 25 and Beden_Kitle_Endeksi<30:
    print("Fazla Kilolu")
elif Beden_Kitle_Endeksi >= 30:
    print("Obez")
