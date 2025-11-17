#Sayısal Loto APP

'''
import tkinter as tk

lotoSonucu=[]

pencere = tk.Tk()

pencere.title("SAYISAL LOTO")
pencere.geometry("400x300")

sonuc = tk.StringVar()
sonuc.set(str(lotoSonucu))

etiket = tk.Label(pencere,text="Sayısal Loto",font=("Arial",20))
etiket.pack(pady=50)

sonuc = tk.Label(pencere, font=("Arial",20))
sonuc.pack()

def lotoStart():
    lotoSonucu = random.sample(range(1,49), 6)
    sonuc.config(text=lotoSonucu)

lotoButton = tk.Button(pencere, text="Loto başlat", font=("Arial",20), command=lotoStart)
lotoButton.pack(pady=50)


pencere.mainloop()

'''

# ATM APP
# Kullanıcı bilgileri JSON sözlük tipinde olacak

# DB
# sifre, adsoyad, bakiye, 

# Menü
# Para çek, Para yatır, çıkış

import tkinter as tk
from tkinter import messagebox
import json

user={}
def userLoad():
    global user
    try:
        with open("user.json", "r", encoding="utf-8") as f:
            user=json.load(f)
    except:
        print("user.json dosyası bulunamadı!")



def paraYatirRootEkrani():
    paraYatirRoot = tk.Toplevel()
    paraYatirRoot.title("Para Yatir")
    paraYatirRoot.geometry("300x300")

    tk.Label(paraYatirRoot, text="Yatırmak istenen miktarı yazınız").pack()
    yatirilmakIstenenMiktar = tk.Entry(paraYatirRoot)
    yatirilmakIstenenMiktar.pack()

    def paraYatir():
        miktar = float(yatirilmakIstenenMiktar.get())
        mevcutMiktar = float(user[tcKimlik]["bakiye"])

        user[tcKimlik]["bakiye"] -= miktar
        try:
            with open("user.json","w", encoding="utf-8") as f:
                json.dump(user,f)
                guncelBakiyeLabel.configure(text=f"Bakiyeniz {user[tcKimlik]['bakiye']}TL", font=("Ariel", 20))
                print("yeni miktar kaydedildi") 
                paraYatirRoot.destroy()
        except:
            messagebox.showerror("hata","dosyaya yazarken hata oluştu")

    tk.Button(paraYatirRoot,text="Onayla",command=paraYatir).pack()

def paraCekRootEkrani():
    global paraCekRoot
    paraCekRoot = tk.Toplevel()
    paraCekRoot.title("Para Çekme")
    paraCekRoot.geometry("300x300")

    tk.Label(paraCekRoot, text="Çekmek istenen miktarı yazınız").pack()
    cekilmekIstenenMiktar = tk.Entry(paraCekRoot)
    cekilmekIstenenMiktar.pack()

    def paraCek():
        miktar = float(cekilmekIstenenMiktar.get())
        mevcutMiktar = float(user[tcKimlik]["bakiye"])

        if miktar > mevcutMiktar:
            messagebox.showerror("hata","hata")
            return
        user[tcKimlik]["bakiye"] -= miktar
        try:
            with open("user.json","w", encoding="utf-8") as f:
                json.dump(user,f)
                guncelBakiyeLabel.configure(text=f"Bakiyeniz {user[tcKimlik]['bakiye']}TL", font=("Ariel", 20))
                print("yeni miktar kaydedildi") 
                paraCekRoot.destroy()
        except:
            messagebox.showerror("hata","dosyaya yazarken hata oluştu")
    
    tk.Button(paraCekRoot,text="Onayla",command=paraCek).pack()

def cikis():
    cevap=messagebox.askyesno(title="Çıkış", message="Çıkış Yapılsın mı?")
    if cevap == True:
        userInfoRoot.destroy()
        root.deiconify()

def atmEkrani(userTcKimlikNo):
    global userInfoRoot
    global guncelBakiyeLabel
    userInfoRoot = tk.Toplevel()
    userInfoRoot.configure(bg="#ff781f")
    userInfoRoot.title("ATM İşlem Ekranı")
    userInfoRoot.geometry("800x600")

    tk.Label(userInfoRoot,text=f"Sayın {user[userTcKimlikNo]["adsoyad"]}\n Hoşgeldiniz.", font=("Ariel", 20)).pack()
    guncelBakiyeLabel = tk.Label(userInfoRoot,text=f"Bakiyeniz {user[userTcKimlikNo]["bakiye"]}TL", font=("Ariel", 20))
    guncelBakiyeLabel.pack(pady=20)
    paraCekButton = tk.Button(userInfoRoot,text="Para Çek", command=paraCekRootEkrani)
    paraCekButton.pack()
    paraYatirmaButton = tk.Button(userInfoRoot,text="Para Yatır", command=paraYatirRootEkrani)
    paraYatirmaButton.pack()
    tk.Button(userInfoRoot,text="Çıkış", command=cikis).pack()

def girisKontrol():
    global tcKimlik
    tcKimlik = tcKimlikEntry.get().strip()
    sifre = sifreEntry.get().strip()
    if not tcKimlik or not sifre:
        messagebox.showwarning("Hata!","Boş olamaz.")
        return
    elif not tcKimlik in user:
        messagebox.showerror("Bu TC kimlikte bir kişi bulunmuyır")
        return
    elif not sifre in user[tcKimlik]["sifre"]:
        messagebox.showerror("Şifre hatalı")
        return
    elif sifre in user[tcKimlik]["sifre"]:
        root.withdraw()
        atmEkrani(tcKimlik)

    #messagebox.showinfo("Test")

userLoad()
root = tk.Tk()

root.title("ATM")
root.geometry("400x150")
root.configure(bg="#2213c7")
tcKimlikLabel = tk.Label(root ,text="Tc Kimlik").pack()
tcKimlikEntry = tk.Entry(root)
tcKimlikEntry.pack()

sifreLabel = tk.Label(root, text="Sifre").pack()
sifreEntry = tk.Entry(root)
sifreEntry.pack()

tk.Button(root, text="Giriş Yap", command=girisKontrol).pack()

root.mainloop()