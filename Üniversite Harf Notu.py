print("""
Harf Notu Hesaplama""")

Vize1=float(input("1.Vize Sonucunu Giriniz:" ))
Vize2=float(input("2.Vİze Sonucunu Giriniz:"))
Final=float(input("Final Sonucunu Giriniz:"))

a=float(Vize1*0.3)
b=float(Vize2*0.3)
c=float(Final*0.4)

Not=float(a+b+c)
print("Not: {}".format(Not))

if Not >=85 and Final>50:
    print("A")
elif Not >=70 and Not<85 and Final>50:
    print("B")
elif Not >=50 and Not<70 and Final>50:
    print("C")
else:
    print("F")
