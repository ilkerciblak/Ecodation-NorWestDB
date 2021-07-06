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
#
# Öğrenci:
# 1. API request", "URL parse", "epoch time conversion" için kütüphaneleri import edecek.
# 2. Customers API için gerekli URL'leri girecek
# 3. Customers API için GET request kullanacak
# 4. if  case, bu kısımda her hangi bir kod değişikliği yapmayacak, request status kontrol ediliyor
# 5. Response içeriği  referans amaçlı print edilecek
# 6. Response icerigi json data formatına encode edilecek
# 7. Orders API için gerekli URL'leri girecek
# 8. Orders API için GET request kullanacak
# 9. if  case, bu kısımda her hangi bir kod değişikliği yapmayacak, request status kontrol ediliyor
# 10. Response içeriği  referans amaçlı print edilecek
# 11. Response icerigi json data formatına encode edilecek
# 12. Mapquest API için gerekli URL'leri girecek
# 13. Mapquest Credential için; token, key... hazırlıkları yapılacak
# 14. UI manipulasyonu. Output anında 15 karakterden uzun metinler için manipulasyon yapılacak
# 15. Müşterileri listeleyecek
# 16. Müşterileri Id'ye göre arama yapılacak
# 17. Siparişleri listeleyecek
# 18. Sipariş Id'ye göre arama yapılacak
# 19. Menü hazırlıkları yapılacak
###############################################################


# 1 → Kütüphaneleri import edelim
# API request",
# "URL parse",
# "epoch time conversion"
from time import gmtime
from urllib.parse import urlparse
import requests



# 2 → Customers API için gerekli URL girelim
urlCustomers = "https://northwind.netcore.io/query/customers.json" # json bağlantısı

# 3 → Customers API için GET request
rCustomers = request.get(urlCustomers)

# 4 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
if not rCustomers.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rCustomers.status_code, rCustomers.text))

# 5 → Response içeriği print et referans amaçlı
#print(rCustomers.text)

# 6 → Response icerigi json data formatına encode et
jsonCustomers = #<Gerekli Json Encode Kodu İle Değiştir>

# 7 → Orders API için gerekli URL'leri girelim
urlOrders = "<Gerekli URL İle Değiştir>"

# 8 → Orders API için GET request
rOrders = #<Request>

# 9 → if  case, bu kısımda her hangi bir kod değişikliği yapmayın lütfen
if not rOrders.status_code == 200:
    raise Exception("API Bağlantı Sorunu. Status code: {}. Text: {}".format(
        rOrders.status_code, rOrders.text))

# 10 → Response içeriği print et referans amaçlı
#print(rOrders.text)

# 11 → response icerigi json data formatına encode et
jsonOrders = #<Gerekli Json Encode Kodu İle Değiştir>

# 12 → Mapquest API için gerekli URL'leri girelim
mainMapApiUrl="<Gerekli URL İle Değiştir>"

# 13 → Mapquest Credential için; token, key... hazırlıkları yapalım
mapApiKey="Kisisel_Key"


# 14 → UI manipulasyonu. Output anında 15 karakterden uzun metinler için manipulasyon yapalım
def metinKontrol(metin):
    if len(metin)>15:
        return f"<Gerekli Kod İle Değiştir>"
    else:
        return f"<Gerekli Kod İle Değiştir>"

# 15 → Müşterileri listeleyelim
def musteriListele():
    print("Müşteri Listesi")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CompanyName            |ContactName            |Address                |Country                |City                   |")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

    for i in jsonCustomers["<Gerekli Key İle Değiştir>"]:
        print(f"Gerekli Output İçin Formatla")

    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

# 16 → Müşterileri Id'ye göre arama yapalım
def musteriAra(musteriId):
    for i in jsonCustomers["<Gerekli Key İle Değiştir>"]:
        if i['id']==musteriId:
            print(f"{musteriId} ID'li müşteri bulundu. Detay Listesi")
            print("==========================")
            print(f"Gerekli Outputlar İçin Değiştir")
            break
    else:
        print(f"{musteriId} ID'li müşteri bulunamadı")

# 17 → Siparişleri listeleyelim
def siparisListele():
    print("Sipariş Listesi")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    print("|ID      |CustomerId     |OrderDate                      |ShipAddress            |ShipCity               |ShipCountry            |")
    print("+--------+---------------+-------------------------------+-----------------------+-----------------------+-----------------------+")
    for i in jsonOrders["<Gerekli Key İle Değiştir>"]:
        epochSaniye = #<Gerekli Key İle Değiştir>
        gunumuzZamani = #<Time Kütüphanesi Gerekli Fonksiyon İle Değiştir>
        print(f"Gerekli Output İçin Formatla")
    print("+--------+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+")

# 18 → Sipariş Id'ye göre arama yapalım
def siparisAra(siparisId):
    for i in jsonOrders["<Gerekli Key İle Değiştir>"]:
        if i['order']['id']==siparisId:
            epochSaniye = #<Gerekli Key İle Değiştir>
            gunumuzZamani = #<Time Kütüphanesi Gerekli Fonksiyon İle Değiştir>
            print(f"{siparisId} ID'li sipariş bulundu. Detay Listesi")
            print("==========================")
            print(f"Gerekli Outputlar İçin Değiştir")
            nereye = #<Gerekli Key İle Değiştir>
            cevap = input(f"Kargo Rotasını {nereye.upper()} Şehri İçin Görmek İster misiniz? [e/E] :")
            if cevap.lower()=="e":
                while True:
                    print(f"Varış Noktası {nereye} için Rota Hesaplanacak")
                    nereden = input("Nereden Çıkacak: ")
                    #<MapQuest API'yı Kullanarak Rota Belirlenecek>
                    break
            break
    else:
        print(f"{siparisId} ID'li sipariş bulunamadı")
# endregion

# 19 → menu
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
        pass
    elif secim==2:
        pass
    elif secim==3:
        pass
    elif secim==4:
        pass
    elif secim==5:
        pass
    else:
        pass
