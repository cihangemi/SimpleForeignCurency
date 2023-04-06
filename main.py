import requests

url = "https://api.apilayer.com/fixer/latest?base="
payload = {}
headers= {
  "apikey": "YOUR APİ KEY"
}

first=input("Birinci Döviz:")
second=input("Çevrilecek Döviz:")
miktar= float(input("Miktar:"))
r =requests.request("GET",url+first,headers=headers,data=payload )

json_data=r.json()
print(float(json_data["rates"][second])*miktar)
