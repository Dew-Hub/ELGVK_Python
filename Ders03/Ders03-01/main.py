import random

'''
def karsilamaMesaji():
    print("---------- Hoşgeldiniz ----------")
    print(" Size nasıl yardımcı olabilirim?")
print("\n")

karsilamaMesaji()

print("\n")

karsilamaMesaji()

print("\n")
'''
'''
def toplamaDf(sayi1, sayi2):
    return(sayi1 + sayi2)
def cikarmaDf(sayi1, sayi2):
    return(sayi1 - sayi2)
def bolmeDf(sayi1, sayi2):
    return(sayi1 / sayi2)
def carpmaDf(sayi1, sayi2):
    return(sayi1 * sayi2)


def hesaplama(ilkSayi, ikinciSayi, islemPrefix):
    if(islemPrefix == "+"):
        if((toplamaDf(ilkSayi, ikinciSayi)%1) != 0):
            print(f"{ilkSayi} ve {ikinciSayi} Toplama işlemi sonucu:" , toplamaDf(ilkSayi, ikinciSayi))
        else:
            print(f"{int(ilkSayi)} ve {int(ikinciSayi)} Toplama işlemi sonucu:" , int(toplamaDf(ilkSayi, ikinciSayi)))


    elif(islemPrefix == "-"):
        if((toplamaDf(ilkSayi, ikinciSayi)%1) != 0):
            print(f"{ilkSayi} ve {ikinciSayi} Çıkarma işlemi sonucu:" , cikarmaDf(ilkSayi, ikinciSayi))
        else:
            print(f"{int(ilkSayi)} ve {int(ikinciSayi)} Çıkarma işlemi sonucu:" , int(cikarmaDf(ilkSayi, ikinciSayi)))

    elif(islemPrefix == "/"):
        print(f"{str(ilkSayi)} ve {str(ikinciSayi)} Bölüme işlemi sonucu:" , bolmeDf(ilkSayi, ikinciSayi))

    elif(islemPrefix == "*"):
        print(f"{str(ilkSayi)} ve {str(ikinciSayi)} Çarpma işlemi sonucu:" , carpmaDf(ilkSayi, ikinciSayi))

    else:
        print("Yanlış işlem isteği.\n")
    
    print("\n")

sayi1 = float(input("İşlem için ilk sayıyı giriniz: "))
sayi2 = float(input("İşlem için ikinci sayıyı giriniz: "))
secim = input("Hangi işlemi yapmak isterseniz (+ | - | / | *): ")

hesaplama(sayi1, sayi2, secim)

'''
'''

print(random.randint(5,50))

loto=[]
sayi = 1
while sayi <= 6:
    lotoNumarasi = random.randint(1,49)
    if lotoNumarasi in loto:
        continue
    loto.append(lotoNumarasi)
    sayi += 1

loto2 = random.sample(range(1,49), 6)

print(loto)
print(loto2)

'''
'''
ogrenciler=["Ali","Ayşe","Mehmet"]
print(random.choice(ogrenciler))

'''