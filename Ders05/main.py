import requests
from pymongo import MongoClient
import certifi

mongourl = "mongodb+srv://burakonturkELG:hnAF2OFUUJGdrEHB@cluster0.j5vgdyh.mongodb.net/?appName=Cluster0"

dbName = "atmDB"

user = [{"tc" : "123456" ,"adsoyad": "Ali Tuna", "sifre": "123", "bakiye": 3147.0}, {"tc" : "55555", "adsoyad": "Burak \u00d6nt\u00fcrk", "sifre": "6462", "bakiye": 10000}]

try:
    mongoCln = MongoClient(mongourl)
    mongoCln.admin.command('ping')
    db = mongoCln[dbName]
    userColl = db["user"]
    userColl.insert_many(user)

except:
    print("Hata oluştu")