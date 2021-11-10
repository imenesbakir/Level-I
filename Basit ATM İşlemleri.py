print("""
**************************************

X BANK HOŞGELDİNİZ
ATM YAPABİLECEĞİNİZ İŞLEMLER

1.BAKİYE SORGULAMA
2.PARA YATIRMA
3.PARA ÇEKME
4.ÇIKIŞ

**************************************""")

başlangıç_bakiyesi=100000

while True:
    Seçiniz=int(input("Yapacağınız İşlemi Seçiniz:"))

    if (Seçiniz==1):
        print("Güncel Bakiye: {}".format(başlangıç_bakiyesi))
    elif (Seçiniz==2):
        Miktar=int(input("Yatıracağınız Miktarı Giriniz:"))
        başlangıç_bakiyesi+=Miktar
        if Miktar > 0:
            print("Güncel Bakiye: {}".format(başlangıç_bakiyesi))
        else:
            print("Hatalı Giriş")
            continue
    elif (Seçiniz==3):
        Miktar = int(input("Çekilecek Miktarı Giriniz:"))
        if Miktar>başlangıç_bakiyesi and Miktar>0:
            print("Yetersiz Bakiye")
            continue
        elif Miktar<başlangıç_bakiyesi and Miktar>0 :
            başlangıç_bakiyesi-=Miktar
            print("Güncel Bakiye: {}".format(başlangıç_bakiyesi))
        else:
            print("Hatalı Giriş")
            continue
    elif (Seçiniz==4):
        print("İYİ GÜNLER DİLER YENİDEN BEKLERİZ")
        break
    else:
        print("Hatalı Giriş")
        continue

