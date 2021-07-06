###############################################################
# Bu program:
# - Customer tablosundan gelen json'u parse ederek listeler
# - Order tablosundan gelen json'u parse ederek listeler
# - Kullanıcıya "/customers" istegi için aramak istediği müşteri id'sorar.
# - Kullanıcıya "/orders" istegi için aramak istediği order id'sorar.
# - MapQuest API için kişisel Credential alır
# - GPS koordinatlarını MapQuest API'yı kullanarak "location" bilgisinden keşfeder.
# - MapQuest API'yı kullanarak kargo elemanına rota çizer.
# - Epoch time modülünü kullanarak ekrana zaman bilgisini formatlar.
# - Runtime'da hata vermemesi için Dictionary'de "key" olup olmadığını keşfederek kod yazar.
# - Dönen json'u konsepti "json beautifier" olan google araması ile daha okunaklı hale getirir
# - https://jsonformatter.curiousconcept.com/ sitesini referan alır



# Gerekli kütüphanelerin import edilmesi
import json
import requests
import time
import urllib
from googletrans import Translator

translator = Translator()

# Customers API için GET Request yapılması
urlCustomers = "https://northwind.netcore.io/query/customers.json" # json bağlantısı
rCustomers = requests.get(urlCustomers)

# Request Status Kontrolü

if rCustomers.status_code == 200:
    print(f"rCustomers : API Connection is Successful, Text = {rCustomers.text[:20]} ")
else:
    raise Exception(f"API Connection Error. Status Code =  {rCustomers.status_code}.\nText = {rCustomers.text}")

# Orders API için GET request yapılması
urlOrders = "https://northwind.netcore.io/query/orders.json"
rOrders = requests.get(urlOrders)

# Orders API için Request Status Kontrolü
if rOrders.status_code == 200:
    print(f"rOrders : API Connection is Successful, Text = {rOrders.text[:20]}")
else:
    raise Exception(f"API Connection Error. Status Code =  {rCustomers.status_code}.\nText = {rCustomers.text}")


# Response içeriklerinin json data formatına encode edilmesi
jsonCustomers = json.loads(rCustomers.text)
jsonOrders = json.loads(rOrders.text)
print(jsonCustomers['results'][0])
# MapQuest Ayarlamalarının yapılması

mapApiKey = "QHhwJZYUfGsSeX9ZjL05w5PJkaxNEF29"
mainMapApiUrl = "https://www.mapquestapi.com/directions/v2/route?"


# Uzun metinlerin manipulasyonu için gerekli fonksiyon
def metinKontrol(metin):
    if len(str(metin)) > 15:
        return f"{str(metin)[:15]}..."
    else:
        return f"{metin}"


# Müşterilerin tamamını listeleyecek fonksiyonun tanımlanması
def musteriListele():
    usefullKeys = ["id", "companyName", "contactName", "address", "country", "city"] # keys used to construct table

    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

    for singleCustomer in jsonCustomers["results"]:
        singleCustomerData = [metinKontrol(singleCustomer[key]) for key in usefullKeys]
        print("|{0:<8}|{1:<23}|{2:<23}|{3:<23}|{4:<23}|{5:<23}|".format(*singleCustomerData))

    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

# Tüm Siparişleri listeleyen fonksiyonun tanımlanması

def siparisListele():
    usefullKeys = ["id","customerId", "shipAddress", "shipCity", "shipCountry"]

    print("Sipariş Listesi")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId     |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")

    for singleOrder in jsonOrders["results"]:
        epochSaniye = int(singleOrder['orderDate'][6:15])
        gunumuzZamani = time.strftime("%a, %b %d %H:%M:%S %Y", time.gmtime(epochSaniye))
        singleOrderData = [metinKontrol(singleOrder[key]) for key in usefullKeys]
        singleOrderData.append(gunumuzZamani)
        #singleOrderData.append(singleOrder['id'])
        #print("|{5:<8}|{0:<23}|{4:<23}|{1:<23}|{2:<23}|{3:<23}|".format(*singleOrderData))
        print("|{0:<8}|{1:<15}|{5:<31}|{2:<23}|{3:<23}|{4:<23}|".format(*singleOrderData))

    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")


# Müşteri ismi ve Sipariş Id'ye göre Arama yapan fonksiyonların tanımlanması

def musteriAra(musteriId):
    usefullKeys = ["id", "companyName", "contactName", "contactTitle",
                   "address", "city", "postalCode", "country", "phone", "fax"]
    printHeads = ["ID", "Firma Adı", "Müşteri Adı", "İş Disiplini", "Adres",
                       "Şehir", "Posta Kodu", "Ülke", "Telefon", "Fax Nu"]

    for singleCustomer in jsonCustomers["results"]:
        if singleCustomer['id'].lower()==musteriId.lower():
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            for key, head in zip(usefullKeys, printHeads):
                try:
                    print(f"{head : <23}: {singleCustomer[key]}")
                except:
                    print(f"{head : <23}: N/A")
            break
    else:
        print(f"{musteriId} ID'li müşteri bulunamadı")

def siparisAra(siparisId):

    printHeads = ["Sipariş Id", "Müşteri Id", "Firma Adı", "Müşteri Adı",
                  "Sipariş Tarihi","Adres", "Şehir", "Ülke"]
    usefullKeys = ["id", "customerId", "shipName", "contactName","orderDate","shipAddress", "shipCity", "shipCountry"]



    for singleOrder in jsonOrders["results"]:
        if singleOrder['id']==siparisId:

            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")

            for key, head in zip(usefullKeys, printHeads):

                if key == "contactName":
                    for singleCustomer in jsonCustomers["results"]:
                        if singleCustomer["id"] == singleOrder['customerId']:
                            print(f"{head : <23} : {singleCustomer[key]}")
                            break

                elif key == "orderDate":
                    epochSaniye = int(singleOrder['orderDate'][6:15])
                    gunumuzZamani = time.strftime("%a, %b %d %H:%M:%S %Y", time.gmtime(epochSaniye))
                    print(f"{head : <23} : {gunumuzZamani}")

                else:
                    print(f"{head : <23} : {singleOrder[key]}")
            print("==========================")

            nereye = singleOrder['shipCity']
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower() == "e":
                while True:

                    print(f"\nVarış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak:  ")
                    mapurl = mainMapApiUrl + urllib.parse.urlencode({"key" : mapApiKey, "from" : nereden, "to": nereye})
                    jsonRouter = requests.get(mapurl).json()
                    break
                print("=========================="*2)
                print(f"Kargo Rotası → Kaynak : {nereden} Varış : {nereye} ")
                print(f"Toplam Süre : {jsonRouter['route']['formattedTime']}")
                print(f"Uzaklık, kilometre : {jsonRouter['route']['distance']*1.61:.2f}")
                print("=========================="*2)

                for dir in jsonRouter["route"]["legs"][0]["maneuvers"]:
                    print(f"{translator.translate(dir['narrative'], dest='tr').text} ({dir['distance']*1.61 : .2f} km)")
                    

                print("=============================================\n")
            break

    else:
        print(f"{siparisId} ID'li sipariş bulunamadı")


if __name__ == "__main__":
    while True:
        for i in range(5):
            print()
        secim = int(input("""
        Seçiminiz:
        [1]     → MÜŞTERİ LİSTELE
        [2]     → MÜŞTERİ ARA <MÜŞTERİ ID'E GÖRE>
        [3]     → SİPARİŞ LİSTELE
        [4]     → SİPARİŞ ARA <SİPARİŞ ID'E GÖRE>
        [5]     → ÇIK
        """))
        if secim==1:
            musteriListele()
        elif secim==2:
            musteriAra(input("Lütfen Müşteri Adı Giriniz, büyük/ küçük harf duyarlılığı yoktur   : "))
        elif secim==3:
            siparisListele()
        elif secim==4:
            siparisAra(int(input("Aranan Sipariş ID giriniz          :")))
        elif secim==5:
            break
        else:
            print("Hatalı Bir Seçim Yaptınız! Tekrar Deneyin. ")
