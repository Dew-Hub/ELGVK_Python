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

def girisKontrol():
    messagebox.showinfo("Test")

userLoad()
root = tk.Tk()

root.title("ATM")
root.geometry("300x400")
tcKimlikLabel = tk.Label(root ,text="Tc Kimlik").pack()
tcKimlik=tk.Entry(root).pack()

sifreLabel = tk.Label(root, text="Sifre").pack()
sifre=tk.Entry(root).pack()


tk.Button(root, text="Giriş Yap", command=girisKontrol).pack()


root.mainloop()