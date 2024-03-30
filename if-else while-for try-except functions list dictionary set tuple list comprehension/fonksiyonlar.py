
'''
def isim_Kisalt(isim):
    isimler = isim.split(' ')
    for i in isimler:
        print(i[0], end='.')


isim_Kisalt('ali akyol')
isim_Kisalt('veli şahin')
isim_Kisalt('ahmet şeker')

'''

'''
def en_büyük_ve_en_kücük_sayilari_topla(x, y, z):
    liste = []
    
    liste.append(x)
    liste.append(y)
    liste.append(z)

    minimum = min(liste)
    maksimum = max(liste)

    toplam = minimum + maksimum

    return toplam

print(en_büyük_ve_en_kücük_sayilari_topla(32, 23, 45))

'''

'''
def string_topla(x, y):
    return x + ' ' + y

print(string_topla('ali', 'veli'))

'''

'''
kelime1 = input('bir kelime yazınız : ')
kelime2 = input('bir kelime yazınız : ')

def kelimeleri_birleştir(x, y):
    return x + ' ' + y

print(kelimeleri_birleştir(kelime1, kelime2))

'''

'''
kelime = input('bir kelime giriniz : ')

def kelime_cogalt(x):
    return x * 10

print(kelime_cogalt(kelime))

'''

'''
sayi1 = int(input('lütfen bir sayı giriniz : '))
sayi2 = int(input('lütfen bir sayı giriniz : '))

def dört_islem(x, y):
    toplam = x + y
    carpma = x * y
    bölme = x / y
    cikarma = x - y
    return toplam, carpma, bölme, cikarma

print(dört_islem(sayi1, sayi2))

'''

'''
def üc_sayi_topla(x, y, z):
    global toplam
    toplam = x + y + z
    return toplam

print(üc_sayi_topla(12, 19, 23))

print(toplam)

'''
'''
sayi = int(input('bir sayı giriniz : '))

def küp_alani(x):
    alan = (x * x) * 6
    return alan

print(küp_alani(sayi))

'''

'''
kisa_kenar = int(input('kısa kenar giriniz : '))
uzun_kenar = int(input('uzun kenar giriniz : '))

def dikdörtgen_cevresi(x, y):
    cevre = (x + y) * 2
    return cevre

print(dikdörtgen_cevresi(kisa_kenar, uzun_kenar))

'''

'''

def toplamlar(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam

print(toplamlar(3,7,9,12,16))

'''
'''
def fonk(**parametreler):
    return parametreler

print(fonk(deger1 = 'hello', deger2 = 'world', deger3 = 'python', deger4 = 'html', deger5 = 'css'))

'''

'''
def carp(*sayilar):
    carpim = 1
    for i in sayilar:
        carpim *= i
    return carpim

print(carp(9, 13, 15, 18, 20, 23, 27))

'''
'''
def daire_alan(r=10):
    global pi
    pi = 3.14
    alan = pi * (r**2)
    return alan

print(daire_alan())
print(pi)

'''

'''
ogrenciler = {}

def ogrenci_ekle(isim):
    if isim not in ogrenciler.keys():
        ogrenciler[isim] = []
        return 'ekleme başarılı'
    else:
        return 'ekleme başarısız'

print(ogrenci_ekle('ahmet'))
print(ogrenciler)
print(ogrenci_ekle('hasan'))
print(ogrenciler)

def not_ekle(isim, notu):
    uzunluk = len(ogrenciler[isim])
    if isim in ogrenciler.keys() and uzunluk < 3:
        notlar = ogrenciler[isim]
        notlar.append(notu)
        return 'not eklendi'
    else:
        return 'not eklenemedi'

print(not_ekle('ahmet', 50))
print(ogrenciler)
print(not_ekle('ahmet', 60))
print(ogrenciler)
print(not_ekle('ahmet', 90))
print(ogrenciler)
print(not_ekle('hasan', 100))
print(ogrenciler)
print(not_ekle('hasan', 70))
print(ogrenciler)
print(not_ekle('hasan', 30))
print(ogrenciler)

'''

'''
sayi = int(input('bir sayı giriniz : '))

def kare_ve_karekök_hesapla(x):
    karesi = x**2
    karekökü = x**0.5
    return karesi, karekökü

print(kare_ve_karekök_hesapla(sayi))

'''

'''
sayi = int(input('bir sayı giriniz : '))

def faktöriyel(x):
    fakt = 1
    if x >= 0:
        for i in range(1, x + 1):
            fakt *= i
        return fakt
    else:
        return 'döndürülemedi'

print(faktöriyel(sayi))

'''

'''
sayi = int(input('bir sayı giriniz : '))

def asal_sayi_kontrol(x):
    sayac = 0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                sayac += 1
                break
        if sayac == 0:
            print('sayı asaldır.')
    
        else:
            print('sayı asal değildir.')
            
asal_sayi_kontrol(sayi)

'''

'''
def küp_al(*sayilar):
    küpler_listesi = []
    for i in sayilar:
        küpler_listesi.append(i ** 3)
    return küpler_listesi

print(küp_al(3, 5, 7, 8, 11, 14))

'''

'''
def kare_al(*sayilar):
    kareler_listesi = []
    for i in sayilar:
        kareler_listesi.append(i ** 2)
    return kareler_listesi

print(kare_al(3,5,8,9,11,12,15,16,18,20,22))

'''

'''
def sözlük(**x):
    return x

print(sözlük(ali='yazılımcı', ahmet='öğretmen', orhan='avukat', ayhan='doktor'))

'''

'''
def maas(**x):
    return x

print(maas(maaş1=32000, maaş2=38000, maaş3=45000, maaş4=56000, maaş5=67000))

'''

'''
import time

def yaz():
    print('hi')

sayac = 0
while sayac < 10:
    yaz()
    time.sleep(1)
    sayac += 1

'''

'''
def yaz(x='merhaba'):
    global kelime
    kelime = 'python'
    return x + ' ' + kelime

print(yaz('selam'))
print(kelime)

'''

'''
def ortalama_hesapla(liste):
    toplam = sum(liste)
    liste_uzunlugu = len(liste)
    ortalama = toplam / liste_uzunlugu
    return ortalama

print(ortalama_hesapla([4,6,10,5,8,9]))

'''

'''
def ilk_harfini_büyük_yaz(metin):
    metin = metin.capitalize()
    return metin

print(ilk_harfini_büyük_yaz('selamlar'))

'''

'''
def bütün_harfleri_büyült(metin):
    metin = metin.upper()
    return metin

print(bütün_harfleri_büyült('hello'))

'''

'''
def bütün_harfleri_kücült(metin):
    metin = metin.lower()
    return metin

print(bütün_harfleri_kücült('PYTHON'))

'''

'''
def not_ortalama(vize= 40, final=100):
    if 0 <= vize <= 100 and 0 <= final <= 100:
        ortalama = vize * 0.40 + final * 0.60
    return ortalama

print(not_ortalama())

'''

'''
cümle = input('bir cümle yazınız : ')

def böl(x):
    x = x.split('-')
    return x

print(böl(cümle))

'''

'''
kelime = input('bir kelime yazınız : ')

def hangi_harfle_basliyo(x):
    if x.lower().startswith('m'):
        return 'kelime m harfi ile başlıyo'
    else:
        return 'kelime m harfi ile başlamıyo'

print(hangi_harfle_basliyo(kelime))

'''

'''
kelime = input('bir kelime yazınız : ')

def hangi_harfle_bitiyo(x):
    if x.lower().endswith('s'):
        return 'kelime s harfi ile bitiyo'
    else:
        return 'kelime s harfi ile bitmiyo'

print(hangi_harfle_bitiyo(kelime))

'''

'''
kelime = input('bir kelime yazınız : ')

def bosluklarını_al(x):
    x = x.strip()
    return x

print(bosluklarını_al(kelime))

'''

'''
kelime = input('bir kelime yazınız : ')

def yenisiyle_degistir(x):
    x = x.replace('.', '')
    return x

print(yenisiyle_degistir(kelime))

'''

'''
sayi1 = int(input('sayı giriniz : '))
sayi2 = int(input('sayı giriniz : '))

def büyük_kücük_sayi_kontrol(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 'iki sayı eşit'

print(büyük_kücük_sayi_kontrol(sayi1, sayi2))

'''

'''
def carp(x, y):
    return x * y

print(carp(12, 55))


def metin_yaz():
    carpim = carp(6, 8)
    metin = f'iki sayının carpimi = {carpim}'
    return metin

print(metin_yaz())

'''

'''
def topla(x, y):
    return x + y


def cikar(x, y):
    return x - y


def carp(x, y):
    return x * y


def böl(x, y):
    return x / y


def tüm_islemleri_hesapla():
    toplama = topla(12, 15)
    cikarma = cikar(30, 18)
    carpma = carp(6, 9)
    bölme = böl(55, 11)
    return toplama, cikarma, carpma, bölme

print(tüm_islemleri_hesapla())

'''

'''
tam_isim = input('lütfen tam isim giriniz : ')


def isim_soyisim_ayirma(x):
    isim = tam_isim.split()[0]
    soyisim = tam_isim.split()[1]
    return isim, soyisim

print(isim_soyisim_ayirma(tam_isim))
print()

a, b = isim_soyisim_ayirma(tam_isim)
print(a)
print(b)

'''

'''
def isim_soyisim_birlestir(*tüm_isimler):
    return '-'.join(tüm_isimler)

print(isim_soyisim_birlestir('metin', 'yağız', 'ali', 'vedat'))

'''

'''
def argümanlar_carp(*sayilar):
    carpim = 1
    for i in sayilar:
        carpim *= i
    return carpim

print(argümanlar_carp(3,5,6,7,8))

'''

'''
def harf_kontrol(**parametreler):
    for i in parametreler:
        print(i.isalpha())
    
harf_kontrol(al4i= 1, veli= 2, can= 3, c22ihan= 4, kem40al= 5)

'''

'''
def isim_maas(**parametreler):
    return f"okanın maaşı = {parametreler['okan']}\nkorayın maaşı = {parametreler['koray']}\nsavaşın maaşı = {parametreler['savaş']}"


print(isim_maas(okan= 22000, burak= 26000, murat= 28000, kazım= 32000, koray= 35000, alper= 38000, savaş= 43000))

'''

'''
isim = input('isim giriniz : ')
soyisim = input('soyisim giriniz : ')

def e_mail_yaz(x, y):
    return x + '.' + y + '@gmail.com'

print(e_mail_yaz(isim, soyisim))

'''

'''
import time
from pprint import pprint
import uuid


personeller = {}

def menu():
    
    print('1 - personel ekle\n'
          '2 - personel listele\n'
          '3 - personel güncelle\n'
          '4 - personel sil\n'
          '5 - çıkış\n')






def ekle():
    kimlik = str(uuid.uuid4())
    isim = input('personelin ismini giriniz : ')
    soyisim = input('personelin soyismini giriniz : ')
    maas = input('personelin maaşını giriniz : ')
    yas = input('personelin yaşını giriniz : ')
    meslek = input('personelin mesleğini giriniz : ')
    
    personeller.update({
        kimlik : {
                'personelin adı' : isim,
                'personelin soyadı' : soyisim,
                'personelin maaşı' : maas,
                'personelin yaşı' : yas,
                'personelin mesleği' : meslek
                }
            })


def listele():
    pprint(personeller)

def güncelle():
    kimlik_no = input('güncellenecek personelin kimlik numarasını giriniz : ')

    if kimlik_no in personeller:
        ad_güncelle = input('yeni isim giriniz : ')
        personeller[kimlik_no]['personelin adı'] = ad_güncelle

        soyad_güncelle = input('yeni soyisim giriniz : ')
        personeller[kimlik_no]['personelin soyadı'] = soyad_güncelle

        maas_güncelle = input('yeni maaş giriniz : ')
        personeller[kimlik_no]['personelin maaşı'] = maas_güncelle

        yas_güncelle = input('yeni yaş giriniz : ')
        personeller[kimlik_no]['personelin yaşı'] = yas_güncelle

        meslek_güncelle = input('yeni meslek giriniz : ')
        personeller[kimlik_no]['personelin mesleği'] = meslek_güncelle
    else:
        print('kimlik no bulunamadı..!')

def sil():
    kimlik_no = input('silinecek personelin kimlik numarasını giriniz : ')

    if kimlik_no in personeller:
        del personeller[kimlik_no]
    else:
        print('kimlik no bulunamadı..!')



while True:
    print()
    menu()
    islem = input('bir işlem türü seçiniz : ')
    print()
    
    if islem == '1':
        ekle()
    
    elif islem == '2':
        listele()
    
    elif islem == '3':
        güncelle()
    
    elif islem == '4':
        sil()
    
    elif islem == '5':
        print('döngüden çıkılıyo....')
        time.sleep(3)
        break
        
'''


'''
def menu():
    print('1 - topla\n'
          '2 - çıkar\n'
          '3 - çarp\n'
          '4 - böl\n'
          '5 - çık\n'
          '6 - karesini hesapla\n'
          '7 - küpünü hesapla\n'
          '8 - karekökünü hesapla\n')


def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def böl(x, y):
    return x / y

def karesini_hesapla(x, y):
    if y == 2:
        return x ** y
    else:
        print('ikinci sayı ikiye eşit olmalı')

def küpünü_hesapla(x, y):
    if y == 3:
        return x ** y
    else:
        print('ikinci sayı üçe eşit olmalı')

def karekökünü_al(x, y):
    if y == 0.5:
        return x ** y
    else:
        print('ikinci sayı 0.5 e eşit olmalı')



while True:
    print()
    menu()
    
    islem = input('bir işlem türü seçiniz : ')
    print()

    if islem == '5':
        print('döngüden çıkıldı!!')
        break

    sayi1 = float(input('ilk sayıyı giriniz : '))
    print()
    sayi2 = float(input('ikinci sayıyı giriniz : '))
    print()

    if islem == '1':
        print('toplama işlemi seçildi')
        print()
        print(f"toplama işleminin sonucu = {topla(sayi1, sayi2)}")
    
    elif islem == '2':
        print('çıkarma işlemi seçildi')
        print()
        print(f"çıkarma işleminin sonucu = {cikar(sayi1, sayi2)}")
    
    elif islem == '3':
        print('çarpma işlemi seçildi')
        print()
        print(f"çarpma işleminin sonucu = {carp(sayi1, sayi2)}")
    
    elif islem == '4':
        print('bölme işlemi seçildi')
        print()
        print(f"bölme işleminin sonucu = {böl(sayi1, sayi2)}")
    
    elif islem == '6':
        print('karesini hesaplama işlemi seçildi')
        print()
        print(f"karesini hesaplama işleminin sonucu = {karesini_hesapla(sayi1, sayi2)}")
    
    elif islem == '7':
        print('küpünü hesaplama işlemi seçildi')
        print()
        print(f"küpünü hesaplama işleminin sonucu = {küpünü_hesapla(sayi1, sayi2)}")
    
    elif islem == '8':
        print('karekökünü alma işlemi seçildi')
        print()
        print(f"karekökünü alma işleminin sonucu = {karekökünü_al(sayi1, sayi2)}")

'''



'''
while True:
    sayi = int(input('bir sayı giriniz : '))

    def cift_mi_tek_mi(x):
        if x % 2 == 0:
            print('girilen sayı çifttir.')
        elif x % 2 == 1:
            print('girilen sayı tektir.')
       

    cift_mi_tek_mi(sayi)

'''

'''
liste = [2, 5, 6, 10, 13, 17, 21, 22, 28, 33]

ciftler_listesi = []

tekler_listesi = []


def cift_sayilari_bul():
    for i in liste:
        if i % 2 == 0:
            ciftler_listesi.append(i)
    return ciftler_listesi


def tek_sayilari_bul():
    for i in liste:
        if i % 2 == 1:
            tekler_listesi.append(i)
    return tekler_listesi

def main():
    print(cift_sayilari_bul())
    print(tek_sayilari_bul())

main()

'''

'''
import time

ogrenciler = {
    'isim' : 'yiğit',
    'soyisim' : 'kartal',
    'not ortalaması' : 45,
    'yaş' : 12
}

print(ogrenciler)
print()


def keys_values():
    for k, v in ogrenciler.items():
        time.sleep(3)
        print(f"anahtar = {k}, değer = {v}")

keys_values()

'''
'''
def dıs_fonk():
    print('dış fonksiyon çalışıyor.')
    def ic_fonk():
        print('iç fonksiyon çalışıyor.')
    print('dış fonksiyon sonlanıyor.')
    ic_fonk()

dıs_fonk()

'''
'''
def hesapla(x):
    def karesini_hesapla(a):
        return a ** 2
    def küpünü_hesapla(a):
        return a ** 3
    def karekökünü_hesapla(a):
        return a ** 0.5
    def faktöriyelini_hesapla(a):
        carpim = 1
        for i in range(1, a + 1):
            carpim *= i
        return carpim
    kare = karesini_hesapla(x)
    küp = küpünü_hesapla(x)
    karekök = karekökünü_hesapla(x)
    faktöriyel = faktöriyelini_hesapla(x)
    return f"karesi : {kare} küpü : {küp} karekökü : {karekök} faktöriyeli : {faktöriyel}"

print(hesapla(8))

'''

'''
def toplama_carpma(*parametreler):
    def toplama(sayilar):
        return sum(sayilar)
    def carpma(sayilar):
        carpim = 1
        for i in sayilar:
            carpim *= i
        return carpim
    return f"toplamları : {toplama(parametreler)} çarpımları : {carpma(parametreler)}"

print(toplama_carpma(3, 5, 6, 8, 9, 12, 14))

'''

'''
def faktöriyel(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * faktöriyel(x - 1)

print(faktöriyel(5))

'''

'''
def toplam(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + toplam(liste[1:])

sayilar_listesi = [10,12,14,15,16]

print(toplam(sayilar_listesi))

'''

# Verilen bir listenin en uzun ve en kısa karakter sayısını bulan fonksiyon yazın


# karakterler değişkeninin tipi tuple.

#karakterler = ('bora','eren','erdem','yunus','gul','başaramadıklarımızdan','harikasın') 


# karakterler değişkenini listeye çevirdik.

# karakterler_listesi = list(karakterler) 


# karakterler listesi içindeki her bir karakterin uzunluğunu depolamak için karakterlerin uzunlukları diye boş bir liste oluşturduk.

# karakterlerin_uzunlukları = [] 


# karakterler listesi içindeki herbir karakterin uzunluğunu karakterlerin uzunlukları listesine ekledik.

#for i in karakterler_listesi: 
    #karakterlerin_uzunlukları.append(len(i))   
#print(karakterlerin_uzunlukları)


# karakterlerin uzunlukları listesini sort ederek herbir karakterin uzunluğunu küçükten büyüğe doğru olacak şekilde sıraladık.
'''
karakterlerin_uzunlukları.sort() 

print(karakterlerin_uzunlukları)

'''

# sort ettikten sonra en kısa kelime sıfırıncı indexte olduğu için sıfırıncı indexteki elemanı alıp en kısa kelime değişkenine atadık.

'''
en_kısa_kelime = karakterlerin_uzunlukları[0]

print(en_kısa_kelime)

'''


# karakterler listesi içinde döngü yapıp tüm kelimelerin uzunluklarını kontrol ettik 
# eğer kelimenin uzunluğu en kısa kelimeye eşit yada küçükse i değişkenini print ettik.

'''
for i in karakterler_listesi: 
    if len(i) <= en_kısa_kelime: 
        print(i)
'''


'''
# Verilen bir listenin en uzun ve en kısa karakter sayısını bulan fonksiyon yazın.

karakterler = ('bora','eren','erdem','yunus','gul','başaramadıklarımızdan','harikasın')

karakterler_listesi = list(karakterler)

karakterlerin_uzunlukları = []

def en_kısa_karakter_sayısı(liste):
    for i in liste: 
        karakterlerin_uzunlukları.append(len(i))
        karakterlerin_uzunlukları.sort()
        en_kısa_kelime = karakterlerin_uzunlukları[0]
    
    for i in liste:
        if len(i) <= en_kısa_kelime:
            print(i)
    

en_kısa_karakter_sayısı(karakterler_listesi)

print('__' * 50)

def en_uzun_karakter_sayısı(liste):
    for i in liste: 
        karakterlerin_uzunlukları.append(len(i))
        karakterlerin_uzunlukları.sort()
        en_uzun_kelime = karakterlerin_uzunlukları[-1]
    
    for i in liste:
        if len(i) >= en_uzun_kelime:
            print(i)
    

en_uzun_karakter_sayısı(karakterler_listesi)

'''






    


 







    
        






    



















































































































    

























