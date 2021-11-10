print("""
******************
Kullanıcı Girişi
******************""")
x="Enes Bakır"
y="123"
giriş_hakkı=3

while True:
    kullanıcı_adı=input("kullanıcı adı:")
    kullanıcı_parolası=input("parola")

    if(kullanıcı_adı==x and kullanıcı_parolası==y):
        print("Sisteme Giriş Başarıyla Sağlandı.")
        break
    else:
        print("Sisteme Başarısız Giriş Yapıldı")
        giriş_hakkı -=1
    if giriş_hakkı==0 :
        print("Giriş Hakkınız Bitmiştir")
        break
