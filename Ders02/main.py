'''
nameFlag = True
name = "NULL"
while(nameFlag):
    name = str(input("Kullanici adi giriniz: "))
    if(name):
        nameFlag = False
print(f"Adiniz: {name.upper()}")


isim = " Elginkan "
print(f"Eğitim kurumu {isim}")
print(f"Eğitim kurumu {isim.strip()}")
print(f"Eğitim kurumu {isim.upper()}")


kurum="ahmet elginkan"
print((kurum.split()[0][0].upper() + kurum.split()[0][1:]) + " " + (kurum.split()[1][0].upper() + kurum.split()[1][1:]))

kurumList = kurum.split()
print(type(kurumList))
print(kurumList[0][0:3] + " " + kurumList[1][2:4] + " " + str(kurumList[0:2]))


yapilacaklar = ["GMD Hazirla", "GMD'yi islemle", "Projeyi bitir"]
print("Liste oluşturuldu ve sifirinci elemani bu sekilde: ",yapilacaklar[0])
yapilacaklar.append("Sunum Hazirla")
print("Listeye append ile yeni bir eleman eklendi:",yapilacaklar)
yapilacaklar.pop(1)
print(f"Listenin tam hali: {yapilacaklar}\nListenin eleman sayisi: {len(yapilacaklar)}")



renkKirmizi = (255, 0, 0) 
renkYesil = (0, 255, 0)
renkMavi = (0, 0, 255)
#renkKirmizi[0] = 300  #tupper değişmez

myRGB = (renkKirmizi[0], renkYesil[1], renkMavi[2])
print(myRGB)


presoneller={
    "ad":"Burak",
    "soyad":"Onturk",
    "sicilno":"1055",
    "maas":85000,
    "deparman":"yazilim",
    "diller":["Python","C","C++","C#","SQL"]
}
print(presoneller["ad"])
#personelin maaşına yüzde 30 zam yapın
print(f"{presoneller['ad']} adli {presoneller['sicilno']} sicil nolu personelin maaşına %30 zam yapilmiştir güncel maas:",int(presoneller["maas"]*1.30))

ogrenciNotu = int(input("Notunuzu giriniz: "))

if 100 >= ogrenciNotu >= 90:
    print("Mukemmel not")
elif ogrenciNotu >= 50 and ogrenciNotu < 90:
    print("Gecer not")
elif 40<ogrenciNotu<50:
    print("Az daha calisman gerekiyor")
elif ogrenciNotu <= 40 and ogrenciNotu > 30:
    print("Biraz kötü")
elif ogrenciNotu <= 30 and ogrenciNotu >= 0:
    print("Kaldiniz")
else:
    print("Gecersiz girdi")


for i in range(5):
    print(i)


print("\nSepet listesi oluşturup içeriğini for döngüsüyle yazmak\n------------------------------------------------------------------------")
print("\nListeyi len ile alarak yaptiğimiz örnek\n------------------------------------------------------")

sepet = [100, 50, 500, 50.5,80.9]

toplam = 0
for i in range(len(sepet)):
    toplam = toplam + sepet[i]

print(f"sepetteki ürünlerin toplami {toplam} TL dir")
print("\nListeyi i değişkeni içerisine atarak yaptiğimiz örnek\n------------------------------------------------------")
toplam = 0
for i in sepet:
    toplam += i

print(f"sepetteki ürünlerin toplami {toplam} TL dir")


print("\nPersoneller tablosu for döngüsü\n------------------------------------")
print("\nKey'ler\n------------------")
for i in presoneller:
    print(i)

print("\nİçeriği\n------------------")
for i in presoneller:
    print(presoneller[i])


a = 1
while(a < 5):
    print(a)
    a+=1


import datetime
secim = ""
musteriler=[]
trashMusteriler=[]
while(secim != "q"):
    print("\n------- ANA MENÜ -------")
    print("1. Müşteri ekle")
    print("2. Müsteri sil")
    print("3. Tüm müşterileri listele")
    print("4. Tüm silinene müşterileri listele")
    print("Çikiş için 'q' tusuna basiniz")
    secim = input("\nYapmak istediğiniz işlemi yapiniz: ")
    if secim == "1":
        yeniMusteri = [input("Müsteri adini giriniz: "),datetime.datetime.now()]
        musteriler.append(yeniMusteri)
    elif secim == "2":
        musteriIndex = int(input("Silmek istediğiniz müşterinin ID numarini yazin: "))
        trashMusteriler.append(musteriler[musteriIndex])
        musteriler.pop(musteriIndex)
    elif secim == "3":
        for i in range(len(musteriler)):
            print(f"{i}. {musteriler[i]}")
    elif secim == "4":
        for i in range(len(trashMusteriler)):
            print(f"{i}. {trashMusteriler[i]}")




calisanlar={
    "1":{"ad":"Burak","dTarih":"06-07-2000","tel":"05325325641","memleket":"Bulgaria","eposta":"burakonturk@gmail.com", "maas":50000},
    "2":{"ad":"Mete","dTarih":"06-07-2001","tel":"0535345126","memleket":"Kocaeli","eposta":"meteulken@gmail.com", "maas":40000},
    "3":{"ad":"Ali","dTarih":"06-07-2005","tel":"0523412412","memleket":"Bursa","eposta":"alimehmet@gmail.com", "maas":30000}
}

calisanTcNoInput = input("Calisanın TC kimlik numarasını giriniz: ")

if(calisanTcNoInput in calisanlar):
    for i in calisanlar[calisanTcNoInput]:
        print(calisanlar[calisanTcNoInput][i])
else:
    print("Kullanıcı bulunamadı")

'''