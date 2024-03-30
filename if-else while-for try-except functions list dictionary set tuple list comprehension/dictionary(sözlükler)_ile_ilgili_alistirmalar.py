
import pprint


'''
kisi = {
    'isim' : 'ahmet',
    'yas'  : 35,
    'cinsiyet' : 'male',
    'hobiler' : ['Spor', 'Seyahat', 'Kitap Okuma']
}

print(kisi)
print('__' * 30)
print(kisi['isim'])
print()
print(kisi['yas'])
print()
print(kisi['cinsiyet'])
print()
print(kisi['hobiler'])
print('__' * 30)
print(kisi.get('isim'))
print()
print(kisi.get('yas'))
print()
print(kisi.get('cinsiyet'))
print()
print(kisi.get('hobiler'))
print()
print(kisi.get('kilosu', 'böyle bir key yok'))
print()
print('__' * 100)

kisi['isim'] = 'metin'
print(kisi)
print('___' * 100)

kisi.update({'yas' : 48, 'hobiler' : ['bilardo', 'dans', 'atletizm', 'yüzme']})
print(kisi)
print('___' * 100)

kisi['memleket'] = 'adana'
print(kisi)
print('___' * 100)

kisi['id'] = 67954233
print(kisi)
print('___' * 100)

del kisi['id']
print(kisi)
print('___' * 100)

for i in kisi:
    print(i)
print('___' * 100)

for i in kisi:
    print(kisi[i])
print('___' * 100)

print(kisi.keys())
print()
print(kisi.values())
print()
print(kisi.items())
print('___' * 100)

for i in kisi.keys():
    print(i)
print('___' * 100)

for i in kisi.values():
    print(i)
print('___' * 100)

for i, j in kisi.items():
    print(i, j)
print('___' * 100)

'''

'''
while True:
    
    renkler = {
        'mavi' : 'blue',
        'sarı' : 'yellow',
        'beyaz' : 'white',
        'yeşil' : 'green',
        'kırmızı' : 'red',
        'siyah' : 'black'
    }

    renk = input('bir renk adı giriniz : ')

    print(f"girilen rengin çevirisi = {renkler.get(renk, 'böyle bir renk sözlükte yok!!')}")

'''
'''
personeller = {
    'ali' : 30,
    'veli' : 34,
    'ekrem' : 45,
    'osman' : 56,
    'ümit' : 26
}

isim = input('bir isim giriniz : ')

print(f"girmiş olduğunuz personelin yaşı : {personeller.get(isim, 'isim yok')}")

'''

'''
personeller = {
    'jack' : {'yas' : 45, 'maas' : 50000, 'boy' : 186, 'kilo' : 82},
    'joe' : {'yas' : 42, 'maas' : 42000, 'boy' : 175, 'kilo' : 70},
    'taylor' : {'yas' : 36, 'maas' : 38500, 'boy' : 182, 'kilo' : 78},
    'michael' : {'yas' : 52, 'maas' : 53500, 'boy' : 180, 'kilo' : 74},
    'sebastian' : {'yas' : 28, 'maas' : 62000, 'boy' : 168, 'kilo' : 60},
    'mary' : {'yas' : 26, 'maas' : 47500, 'boy' : 156, 'kilo' : 53},
    'natalia' : {'yas' : 30, 'maas' : 60000, 'boy' : 160, 'kilo' : 55}
}

while True:
    try:
        personel = input('bir personel adı giriniz : ')

        print(f"{personel} adlı personelin bilgileri: {personeller[personel]}")
    
    except Exception:
        print('böyle bir personel bulunamadı...')
        break
        
'''
'''
while True:

    try:
        dersler = {
            'alican' : ['türkçe', 'ingilizce', 'matematik'],
            'kerem'  : ['fen', 'kimya', 'biyoloji'],
            'ümit'   : ['bilişim', 'tarih', 'coğrafya']
        }

        ögrenci_adı = input('bir öğrenci adı giriniz : ')
        print(f"{ögrenci_adı} adlı öğrencinin aldığı dersler:")

        for i in dersler[ögrenci_adı][0]:
            print(f"ders = {i}")
    except:
        print('böyle bir öğrenci yok!!!')
        break
        
'''
'''
person = dict(isim= 'saffet', soyisim='şahin', yas=55, boy=194, kilo=85)
print(person)

for i,j in person.items():
    print(i,j)

'''
'''
person = {
    'isim' : 'cihan',
    'soyisim' : 'bulut',
    'yas' : 42
}

print(person)
print()

person['memleket'] = 'bursa'
print(person)
print()

person.update({'isim' : 'erdem', 'soyisim' : 'güneş', 'yas' : 30, 'meslek' : 'garson', 'maaş' : 25000})
print(person)
print()

while True:
    anahtar_kelime = input('bir anahtar kelime giriniz : ')

    if anahtar_kelime in person:
        print(person[anahtar_kelime])

    else:
        print('sözlük içinde böyle bir anahtar kelime bulunamadı...')
        break

print('__' * 50)

print(person.get('saat', 'böyle bir anahtar kelime yok!'))
print()
print(person.get('meslek'))
print()
print(person['memleket'])
print('__' * 50)

for i in person.keys():
    print(f"anahtar = {i}")

print("__" * 50)

for i in person.values():
    print(f"değer = {i}")

print("__" * 50)

for i, j in person.items():
    print(f"anahtar = {i} : değer = {j}")

'''

'''
car = {
    'marka' : 'audi',
    'model' : 'a4',
    'yıl' : 2015

}

print(car)
print('------------------')

car['renk'] = 'beyaz'
print(car)
print('------------------')

car['model'] = 'a5'
print(car)
print('------------------')

car.update({'marka' : 'peugeot', 'model' : 308, 'yıl' : 2018, 'renk' : 'siyah', 'fiyat' : '850000'})
print(car)
print('------------------')

car.pop('renk')
print(car)
print('------------------')

car.popitem()
print(car)
print('------------------')

del car['yıl']
print(car)
print('------------------')

car.clear()
print(car)
print('------------------')

'''

'''
dersler = {

    'kaan' : ['matematik', 'coğrafya', 'türkçe'],
    'ogün' : ['tarih', 'kimya', 'ingilizce'],
    'murat' : ['biyoloji', 'fizik', 'edebiyat'],
    'burak' : ['geometri', 'felsefe', 'fransızca']

}


while True:
    ögrenci = input('bir öğrenci adı giriniz : ')
    

    if ögrenci not in dersler:
        print('böyle bir öğrenci yok...')
        break

    else:
        dersler[ögrenci][-1] = 'yazılım'
        dersler[ögrenci][0] = 'beden dersi'
        dersler[ögrenci].pop(1)
        dersler[ögrenci].append('bilgisayar')
        dersler[ögrenci].extend(['php','java','html'])
        
    print(f"girmiş olduğunuz {ögrenci} adlı öğrencinin dersleri: {dersler.get(ögrenci, 'dersler bulunamadı.')}")

'''

# Kullanıcı bir ingilizce cümle yazsın.
# cümle renk isimlerinden oluşsun.
# cümle içindeki renklerin anlamı türkçeye çevrilsin.

'''
renkler = {
    'black' : 'siyah',
    'red' : 'kırmızı',
    'blue' : 'mavi',
    'green' : 'yeşil',
    'yellow' : 'sarı',
    'white' : 'beyaz',
    'brown' : 'kahverengi',

}


while True:
    
    cümle = input("bir cümle giriniz (çıkmak için q tuşuna basınız...) : ")

    if cümle == 'q':
        print('q tuşuna bastınız...')
        break

    isaret_karakterleri = '.,;:?!=-'

    for i in isaret_karakterleri:
        cümle = cümle.replace(i, '')

    kelimeler = set(cümle.lower().split())
    

    for i in kelimeler:
        kelime_anlami = renkler.get(i, 'böyle bir renk sözlükte bulunmuyor...')

        print(f"{i} : {kelime_anlami}")

'''

'''
users = {
    'james' : 'xxx999yyy',
    'brentley' : '15555000',
    'thompson' : 'abc2332',
    'taylor' : '1a1b1c1d1e'
}

print(len(users))
print('__' * 40)

print(dir(users))
print('__' * 40)

print(users.get('taylor', 'böyle bir kullanıcı sözlükte yok'))
print('__' * 40)

print(users['james'])
print('__' * 40)

users['alphonso'] = 'qw12qw'

print(users)
print('__' * 40)

users.pop('james')
print(users)
print('__' * 40)

users.popitem()
print(users)
print('__' * 40)


kullanicilar = users.copy()
print(kullanicilar)
print('__' * 40)

kullanicilar['terminator'] = 'king1'
print(kullanicilar)
print('__' * 40)

print(users)
print('__' * 40)

ögrenciler = ['kadir', 'emel', 'selen','ismail','okan']

students = dict()

print(students.fromkeys(ögrenciler, 'arslan'))
print('__' * 40)

users.clear()
print(users)
print('__' * 40)

users.setdefault('spiderman', 'örümcekadam12345')
print(users)
print('__' * 40)

users['batman'] = 'yarasaadam987654321'
print(users)
print('__' * 40)

users.update({'spiderman' : 12345, 'batman' : 54321, 'ironman' : 101010})
print(users)
print('__' * 200)

personeller = [{
    'ad' : 'hasan',
    'soyad' : 'doğan',
    'maas' : 35000,
    'meslek' : 'grafiker',
    'hobiler' : ['yemek yapma', 'spor', 'yürüyüş']

},
 {
     'ad' : 'orhan',
    'soyad' : 'kartal',
    'maas' : 43000,
    'meslek' : 'yazılımcı',
    'hobiler' : ['müzik', 'dans', 'basketbol']
 },
 {
     'ad' : 'kenan',
    'soyad' : 'şahin',
    'maas' : 30000,
    'meslek' : 'öğretmen',
    'hobiler' : ['kitap okuma', 'satranç', 'seyahat']
 }

]

for i in personeller:
    print(i)
    print()
    print(i.get('ad'))
    print()
    print(i.pop('maas'))
    print()
    print(i)
    print()
    i.update({'hobiler' : ['dağcılık', 'yüzme', 'atletizm']})
    print(i)
    print()
    print(i.get('hobiler')[-1])
    print()
    i['hobiler'][-1] = 'satranç'
    print(i)
    print()
    i['memleket'] = ['ankara', 'mersin', 'izmir']
    print(i)
    print()
    i['memleket'][-1] = ''
    print(i)
    print()
    i.update({'memleket' : ['erzurum', 'ankara', 'mersin']})
    print(i)

'''

'''
personel = {
    'isim' : 'murat',
    'soyisim' : 'yalın',
    'yas' : 45,
    'lokasyon' : {
        'doğum yeri' : 'antalya',
        'yaşadığı şehir' : 'adana'

    }
}

print(personel['lokasyon']['doğum yeri'])
print(personel['lokasyon']['yaşadığı şehir'])
print('__'*40)

print(personel.keys())
print()
print(personel.values())
print()
print(personel.items())

'''

'''
personeller = {
    'canberk yılmaz' : {'şehir' : 'istanbul',
                        'meslek' : 'doktor',
                        'yaş' : 58},
    
    'metin aytekin' :  {'şehir' : 'konya',
                        'meslek' : 'öğretmen',
                        'yaş' : 45,
                        'hobiler' : {'spor' : ['yüzme', 'dağcılık', 'vücut geliştirme'], 
                                     'aktivite' : 'konser'}},

}

print(personeller['canberk yılmaz']['yaş'])
print()
print(personeller['metin aytekin']['meslek'])
print()
print(personeller['metin aytekin']['hobiler']['aktivite'])
print()
print(personeller['metin aytekin']['hobiler']['spor'][-1])
print()
personeller['metin aytekin']['hobiler']['spor'][0] = 'basketbol'
print(personeller)
print()
personeller['metin aytekin']['hobiler']['spor'][1] = ''
print(personeller)
print()
personeller['canberk yılmaz'].update({'hobiler' : {'spor' : ['tenis', 'voleybol', 'hentbol']}})
print(personeller)
print()
personeller['canberk yılmaz'].update({'aktivite' : ['sinema', 'tiyatro', 'konser']})
print(personeller)
print()
personeller['metin aytekin'].pop('şehir')
print(personeller)
print()
del personeller['metin aytekin']['hobiler']['aktivite']
print(personeller)
print()
del personeller['metin aytekin']['hobiler']['spor'][1]
print(personeller)

'''
'''
while True:

    ögrenci = input('bir öğrenci adı giriniz : ')
    
    students = {
        'yusuf' : {'yaş' : 14, 'en sevdiği ders' : 'matematik', 'memleket' : 'bolu'},
        'can' : {'yaş' : 13, 'en sevdiği ders' : 'coğrafya', 'memleket' : 'hatay'},
        'ekrem' : {'yaş' : 15, 'en sevdiği ders' : 'tarih', 'memleket' : 'kocaeli'},
        'serkan' : {'yaş' : 12, 'en sevdiği ders' : 'fizik', 'memleket' : 'muğla'},
        'soner' : {'yaş' : 16, 'en sevdiği ders' : 'felsefe', 'memleket' : 'istanbul'},
        'altan' : {'yaş' : 17, 'en sevdiği ders' : 'geometri', 'memleket' : 'ankara'},
        'necdet' : {'yaş' : 11, 'en sevdiği ders' : 'ingilizce', 'memleket' : 'izmir'}
    }

    isaretleme_karakterleri = '.,?:;!'

    for i in isaretleme_karakterleri:

        ögrenci = ögrenci.lower().replace(i, '')
    
    if ögrenci not in students:
        print(f"{ögrenci} adlı öğrenci bulunamadı!")
        break

    else:
        print(f"girmiş olduğunuz {ögrenci} adlı öğrencinin bilgileri = {students[ögrenci]}")

'''

'''
rakamlar = {'0' : 'sıfır', '1' : 'bir', '2' : 'iki', '3' : 'üç', '4' : 'dört', 
            '5' : 'beş', '6' : 'altı', '7' : 'yedi', '8' : 'sekiz', '9' : 'dokuz'}

while True:
    numara = input('bir numara giriniz : ')

    string_rakam = ''
    for i in numara:
        if i.isdigit():
           string_rakam += rakamlar[i] + ' '
        else:
          print(f"lütfen rakam giriniz..")
    
    print(string_rakam)

'''
'''
personeller = {
    'hasan' : 20000,
    'recep' : 22000,
    'suat' : 26500,
    'erkan' : 32500
}

personel_isimleri = input('personel giriniz : ')
personel_isimleri = personel_isimleri.lower().split()

maas_toplam = 0

for i in personel_isimleri:
    if i in personeller:
       maas_toplam += personeller[i]

print(maas_toplam)

'''

'''
import pprint


ogrenciler = {}

sayac = 0

while sayac < 3:
    numara = input('bir numara giriniz : ')
    name = input('öğrencinin ismini giriniz : ')
    surname = input('öğrencinin soyismini giriniz : ')
    phone = input('öğrencinin telefon numarasını giriniz : ')
    print()

    ogrenciler.update({
            numara : {
                'ad' : name,
                'soyad' : surname,
                'telefon' : phone
            }
        })
    
    sayac += 1

    pprint.pp(ogrenciler)
    print()
    
    
ogrenci_no = input('hangi öğrencinin bilgisini öğrenmek istiyorsanız öğrenci numarasını giriniz : ')

if ogrenci_no in ogrenciler:
    print('öğrenci bulundu...')
    print(f"öğrencinin numarası : {ogrenci_no}\nismi : {ogrenciler[ogrenci_no]['ad']}\nsoyismi : {ogrenciler[ogrenci_no]['soyad']}\ntelefonu : {ogrenciler[ogrenci_no]['telefon']}")
    print()
else:
    print(f'girilen {ogrenci_no} öğrenci numarası sözlükte mevcut değil!!')
    

ogrenci_no = input('hangi öğrenciyi silmek istiyorsanız öğrenci numarasını giriniz : ')

if ogrenci_no in ogrenciler:
    print('öğrenci bulundu...')
    print(f"{ogrenciler[ogrenci_no]['ad']} {ogrenciler[ogrenci_no]['soyad']} isimli öğrenci silindi....")
    del ogrenciler[ogrenci_no]
    
else:
    print(f'girilen {ogrenci_no} öğrenci numarası sözlükte mevcut olmadığından öğrenci silme işlemi gerçekleştirilemedi!!')
pprint.pp(ogrenciler)
print()


ogrenci_no = input('hangi öğrencinin telefon numarasını güncellemek istiyorsanız öğrenci numarasını giriniz : ')

if ogrenci_no in ogrenciler:
   print('öğrenci bulundu...')
   print(f"{ogrenciler[ogrenci_no]['ad']} {ogrenciler[ogrenci_no]['soyad']} isimli öğrencinin yeni telefon numarasını güncelleyin...")
   updated_phone = input('öğrencinin yeni telefon numarasını giriniz : ')
   ogrenciler[ogrenci_no]['telefon'] = updated_phone
else:
    print(f'girilen {ogrenci_no} öğrenci numarası sözlükte mevcut olmadığından telefon numarası güncelleme işlemi gerçekleştirilemedi!!')
pprint.pp(ogrenciler)

'''

'''
import pprint

personeller = {}

sayac = 0

while sayac < 3:

    identity = input('personelin kimlik numarasını giriniz : ')
    name = input('personelin ismini giriniz : ')
    surname = input('personelin soyismini giriniz : ')
    age = input('personelin yaşını giriniz : ')
    phone = input('personelin telefon numarasını giriniz : ')
    occupation = input('personelin mesleğini giriniz : ')

    personeller.update({
        identity : {
            'isim' : name,
            'soyisim' : surname,
            'yaş' : age,
            'telefon no' : phone,
            'meslek' : occupation

        }
    })

    sayac += 1

pprint.pp(personeller)

kimlik_no = input('bilgilerini öğrenmek istediğiniz personelin kimlik numarasını giriniz : ')

if kimlik_no in personeller:
    print('personel bulundu...')
    print(f"personelin kimlik no : {kimlik_no}\nismi : {personeller[kimlik_no]['isim']}\nsoyismi : {personeller[kimlik_no]['soyisim']}\nyaşı : {personeller[kimlik_no]['yaş']}\ntelefon no : {personeller[kimlik_no]['telefon no']}\nmesleği : {personeller[kimlik_no]['meslek']}")
else:
    print(f"{kimlik_no} kimlik numarası bulunamadığından personel bilgileri gösterilemedi!!!")


kimlik_no = input('silmek istediğiniz personelin kimlik numarasını giriniz : ')

if kimlik_no in personeller:
    print('personel bulundu...')
    print(f"{personeller[kimlik_no]['isim']} {personeller[kimlik_no]['soyisim']} adlı personel silinmiştir...")
    del personeller[kimlik_no]
else:
    print(f"{kimlik_no} kimlik numarası bulunamadığından personel silme işlemi gerçekleştirilemedi!!!")

pprint.pp(personeller)

kimlik_no = input('bilgilerini güncellemek istediğiniz personelin kimlik numarasını giriniz : ')

if kimlik_no in personeller:
    print('personel bulundu...')
    print('personel bilgilerini güncelleyebilirsiniz...')
    updated_age = input('lütfen personelin yeni yaşını giriniz : ')
    updated_phone = input('lütfen personelin telefon numarasını giriniz : ')
    updated_occupation = input('lütfen personelin yeni mesleğini giriniz : ')
    personeller[kimlik_no]['yaş'] = updated_age
    personeller[kimlik_no]['telefon no'] = updated_phone
    personeller[kimlik_no]['meslek'] = updated_occupation

else:
    print(f"girilen {kimlik_no} kimlik numarası sözlükte mevcut olmadığından personel bilgileri güncellenemedi!!!")

pprint.pp(personeller)

kimlik_no = input('herhangi bir personele memleket bilgisi eklemek istiyorsanız lütfen personelin kimlik numarasını giriniz : ')

if kimlik_no in personeller:
    print('personel bulundu...')
    print('bulunan personele memleket bilgisi ekleyebilirsiniz...')
    hometown = input('lütfen personelin memleket bilgisini giriniz : ')
    personeller[kimlik_no]['memleket'] = hometown

else:
    print(f"girilen {kimlik_no} kimlik numarası sözlükte mevcut olmadığından dolayı personele memleket özelliği ekleme işlemi gerçekleştirilemedi!!")

pprint.pp(personeller)

tüm_personelleri_sil = input('tüm personelleri silmek istediğinizden eminmisiniz (E / H) : ')

if tüm_personelleri_sil.upper() == 'E':
    print('sözlük içindeki tüm personeller başarıyla silindi...')
    personeller.clear()

elif tüm_personelleri_sil.upper() == 'H':
    print(f"tüm personelleri silme işlemini onaylamadınız!!!")

else:
    print(f"(E / H) dışında başka bir tuşa bastınız!!")

pprint.pp(personeller)

'''




'''
ürünler = {
    'sebzeler' : ['turp', 'havuç', 'limon', 'fasulye'],
    'meyveler' : ['kavun', 'karpuz', 'incir', 'şeftali'],
    'bakliyatlar' : ['kırmızı mercimek', 'yeşil mercimek', 'pirinç', 'bulgur']
}

while True:
    islem = (input('1-ürün sil\n2-ürün ekle\n3-ürünleri listele\n4-ürün adı güncelle\n5-çıkış yap\n6-ürünü istenilen indekse ekle\n7-ürün sayısını bul\nyapmak istediğiniz işlemi seçiniz : '))

    if islem.isdigit():
    
        if islem == '1':
            
            kategori = input('kategori seçiniz (sebzeler, meyveler, bakliyatlar) : ')
            
            if kategori == 'sebzeler':
                print(ürünler['sebzeler'])
                ürün_adı = input('silmek istediğiniz ürünün adını giriniz : ')
                ürünler['sebzeler'].remove(ürün_adı)
            
            if kategori == 'meyveler':
                print(ürünler['meyveler'])
                ürün_adı = input('silmek istediğiniz ürünün adını giriniz : ')
                ürünler['meyveler'].remove(ürün_adı)
            
            if kategori == 'bakliyatlar':
                print(ürünler['bakliyatlar'])
                ürün_adı = input('silmek istediğiniz ürünün adını giriniz : ')
                ürünler['bakliyatlar'].remove(ürün_adı)
        
       
    
        
        if islem == '2':
            
            kategori = input('kategori seçiniz (sebzeler, meyveler, bakliyatlar) : ')
            
            
            if kategori == 'sebzeler':
                print(ürünler['sebzeler'])
                ürün_adı = input('eklemek istediğiniz ürünün adını giriniz : ')
                
                ürünler['sebzeler'].append(ürün_adı)
                
            
            if kategori == 'meyveler':
                print(ürünler['meyveler'])
                ürün_adı = input('eklemek istediğiniz ürünün adını giriniz : ')
                
                ürünler['meyveler'].append(ürün_adı)
            
            
            if kategori == 'bakliyatlar':
                print(ürünler['bakliyatlar'])
                ürün_adı = input('eklemek istediğiniz ürünün adını giriniz : ')
                
                ürünler['bakliyatlar'].append(ürün_adı)
            
       
    
        
        if islem == '3':
            print(ürünler)
        

        
        if islem == '4':

            kategori = input('kategori seçiniz (sebzeler, meyveler, bakliyatlar) : ')

            
            if kategori == 'sebzeler':
                print(ürünler['sebzeler'])
                güncellenecek_ürün_adı = input('güncellemek istediğiniz ürün adını giriniz : ')
                ürünün_yeni_adı = input('güncellenen ürünün yeni adını giriniz : ')
                if güncellenecek_ürün_adı in ürünler['sebzeler']:
                    i = ürünler['sebzeler'].index(güncellenecek_ürün_adı)
                    ürünler['sebzeler'][i] = ürünün_yeni_adı
            
            
            if kategori == 'meyveler':
                print(ürünler['meyveler'])
                güncellenecek_ürün_adı = input('güncellemek istediğiniz ürün adını giriniz : ')
                ürünün_yeni_adı = input('güncellenen ürünün yeni adını giriniz : ')
                if güncellenecek_ürün_adı in ürünler['meyveler']:
                    i = ürünler['meyveler'].index(güncellenecek_ürün_adı)
                    ürünler['meyveler'][i] = ürünün_yeni_adı
            

            if kategori == 'bakliyatlar':
                print(ürünler['bakliyatlar'])
                güncellenecek_ürün_adı = input('güncellemek istediğiniz ürün adını giriniz : ')
                ürünün_yeni_adı = input('güncellenen ürünün yeni adını giriniz : ')
                if güncellenecek_ürün_adı in ürünler['bakliyatlar']:
                    i = ürünler['bakliyatlar'].index(güncellenecek_ürün_adı)
                    ürünler['bakliyatlar'][i] = ürünün_yeni_adı
                    
            
            
         
        if islem == '5':
            print('çıkış yapıldı...')
            break


        
        if islem == '6':

            kategori = input('kategori seçiniz (sebzeler, meyveler, bakliyatlar) : ')

            if kategori == 'sebzeler':
                print(ürünler['sebzeler'])
                indeks_numarasına_göre_eklenecek_ürün = input('indeks numarasına göre eklemek istediğiniz ürünü giriniz : ')
                eklenecek_ürünün_indeksi = int(input('eklenecek ürünün indeks numarasını giriniz : '))
                if indeks_numarasına_göre_eklenecek_ürün not in ürünler['sebzeler']:
                    ürünler['sebzeler'].insert(eklenecek_ürünün_indeksi, indeks_numarasına_göre_eklenecek_ürün)
            
            if kategori == 'meyveler':
                print(ürünler['meyveler'])
                indeks_numarasına_göre_eklenecek_ürün = input('indeks numarasına göre eklemek istediğiniz ürünü giriniz : ')
                eklenecek_ürünün_indeksi = int(input('eklenecek ürünün indeks numarasını giriniz : '))
                if indeks_numarasına_göre_eklenecek_ürün not in ürünler['meyveler']:
                    ürünler['meyveler'].insert(eklenecek_ürünün_indeksi, indeks_numarasına_göre_eklenecek_ürün)

            if kategori == 'bakliyatlar':
                print(ürünler['bakliyatlar'])
                indeks_numarasına_göre_eklenecek_ürün = input('indeks numarasına göre eklemek istediğiniz ürünü giriniz : ')
                eklenecek_ürünün_indeksi = int(input('eklenecek ürünün indeks numarasını giriniz : '))
                if indeks_numarasına_göre_eklenecek_ürün not in ürünler['bakliyatlar']:
                    ürünler['bakliyatlar'].insert(eklenecek_ürünün_indeksi, indeks_numarasına_göre_eklenecek_ürün)
            


        
        if islem == '7':

            kategori = input('kategori seçiniz (sebzeler, meyveler, bakliyatlar) : ')

            if kategori == 'sebzeler':
                print(ürünler['sebzeler'])
                adedini_görmek_istediğimiz_ürün = input('adedini görmek istediğiniz ürün adını giriniz : ')
                ürün_adedi = ürünler['sebzeler'].count(adedini_görmek_istediğimiz_ürün)
                print(f"girmiş olduğuğunuz ürün {adedini_görmek_istediğimiz_ürün} ve bu ürünün adedi = {ürün_adedi} tanedir.")

            if kategori == 'meyveler':
                print(ürünler['meyveler'])
                adedini_görmek_istediğimiz_ürün = input('adedini görmek istediğiniz ürün adını giriniz : ')
                ürün_adedi = ürünler['meyveler'].count(adedini_görmek_istediğimiz_ürün)
                print(f"girmiş olduğunuz ürün {adedini_görmek_istediğimiz_ürün} ve bu ürünün adedi = {ürün_adedi} tanedir.")

            if kategori == 'bakliyatlar':
                print(ürünler['bakliyatlar'])
                adedini_görmek_istediğimiz_ürün = input('adedini görmek istediğiniz ürün adını giriniz : ')
                ürün_adedi = ürünler['bakliyatlar'].count(adedini_görmek_istediğimiz_ürün)
                print(f"girmiş olduğunuz ürün {adedini_görmek_istediğimiz_ürün} ve bu ürünün adedi = {ürün_adedi} tanedir.")

                
'''

'''
from pprint import pprint
from uuid import uuid4

ogrenciler = {}

while True:
    print("manuel giriş : yapmak istediğiniz işlemi seçiniz.\n"
          '1 - yarat\n'
          '2 - listele\n'
          '3 - güncelle\n'
          '4 - sil\n'
          '5 - çıkış')
    print()
    
    islem = input('yapmak istediğiniz işlemi seçiniz : ')
    print()

    if islem == '1': 
        ogrenci_id = str(uuid4())
        ad = input('öğrencinin adı : ')
        soyad = input('öğrencinin soyadı : ')
        telefon = input('öğrencinin telefon numarası : ')

        ogrenciler.update({
            
            ogrenci_id : {
                'isim' : ad,
                'soyisim' : soyad,
                'telefon no' : telefon
            }
        })

        pprint('ekleme işlemi başarıyla gerçekleştirilmiştir...')
        print()
    
    if islem == '2':
        pprint(ogrenciler)
    
    if islem == '3':
        
        id_no = input('güncellenecek olan öğrencinin id numarasını giriniz : ')
        
        if id_no in ogrenciler:
            
            print('öğrenci sözlükte mevcut. öğrenci bilgilerini güncelleyebilirsiniz...')

            
            güncellenen_ad = input('öğrencinin yeni adını giriniz : ')
            
            ogrenciler[id_no]['isim'] = güncellenen_ad

            
            güncellenen_soyad = input('öğrencinin yeni soyadını giriniz : ')
            
            ogrenciler[id_no]['soyisim'] = güncellenen_soyad

            
            güncellenen_telefon = input('öğrencinin yeni telefon numarasını giriniz : ')
            
            ogrenciler[id_no]['telefon no'] = güncellenen_telefon
            
            

            pprint(f"{ogrenci_id} id numarasına sahip öğrenci başarıyla güncellenmiştir...")
            pprint(ogrenciler)
        
        
        else:
            print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı güncelleme işlemi başarısız olmuştur!')
    
    if islem == '4':

        id_no = input('silinecek olan öğrencinin id numarasını giriniz : ')

        if id_no in ogrenciler:

            print('öğrenci sözlükte mevcut. öğrenci silme işlemini gerçekleştirebilirsiniz...')

            del ogrenciler[id_no]

            print(f"{id_no} id numarasına sahip öğrenci başarıyla silinmiştir...")
        
        else:
            print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı silme işlemi başarısız olmuştur!')
    
    if islem == '5':
        print('uygulamadan çıkıldı...')
        break
        
'''


'''
from pprint import pprint
from uuid import uuid4



def islem_menüsü():
    print('yapmak istediğiniz işlemi seçiniz\n'
          '1 - ekle\n'
          '2 - listele\n'
          '3 - güncelle\n'
          '4 - sil\n'
          '5 - email adres bilgisi ekle\n'
          '6 - not bilgisi ekle\n'
          '7 - çıkış')



def ekle():
    ogrenci_id = str(uuid4())
    ad = input('öğrencinin adı : ')
    soyad = input('öğrencinin soyadı : ')
    telefon = input('öğrencinin telefon numarası : ')

    ogrenciler.update({
            
            ogrenci_id : {
                'isim' : ad,
                'soyisim' : soyad,
                'telefon no' : telefon
            }
        })

    pprint('ekleme işlemi başarıyla gerçekleştirilmiştir...')




def listele():
    pprint(ogrenciler)




def güncelle():
    id_no = input('güncellenecek olan öğrencinin id numarasını giriniz : ')
        
    if id_no in ogrenciler:
            print('öğrenci sözlükte mevcut. öğrenci bilgilerini güncelleyebilirsiniz...')
            güncellenen_ad = input('öğrencinin yeni adını giriniz : ')
            ogrenciler[id_no]['isim'] = güncellenen_ad
            güncellenen_soyad = input('öğrencinin yeni soyadını giriniz : ')
            ogrenciler[id_no]['soyisim'] = güncellenen_soyad
            güncellenen_telefon = input('öğrencinin yeni telefon numarasını giriniz : ')
            ogrenciler[id_no]['telefon no'] = güncellenen_telefon
            pprint(f"{id_no} id numarasına sahip öğrenci başarıyla güncellenmiştir...")
            pprint(ogrenciler)
    else:
        print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı güncelleme işlemi başarısız olmuştur!')



def sil():
    id_no = input('silinecek olan öğrencinin id numarasını giriniz : ')

    if id_no in ogrenciler:
            print('öğrenci sözlükte mevcut. öğrenci silme işlemini gerçekleştirebilirsiniz...')
            del ogrenciler[id_no]
            print(f"{id_no} id numarasına sahip öğrenci başarıyla silinmiştir...")
    else:
        print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı silme işlemi başarısız olmuştur!')



def email_adres_ekle():
    id_no = input('email adres bilgisi eklenecek öğrencinin id numarasını giriniz : ')

    if id_no in ogrenciler:
            print('öğrenci sözlükte mevcut. email adresi ekleme işlemini gerçekleştirebilirsiniz...')
            email_adres = input('lütfen bir email bilgisi giriniz : ')
            ogrenciler[id_no]['e-mail adresi'] = email_adres
            print('email adresi ekleme işlemi başarıyla gerçekleştirilmiştir...')
    else:
        print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı email adresi ekleme işlemi gerçekleştirilemedi!')


def not_bilgisi():
    id_no = input('not bilgisi eklenecek öğrencinin id numarasını giriniz : ')

    if id_no in ogrenciler:
            print('öğrenci sözlükte mevcut. not bilgisi hesaplama işlemini gerçekleştirebilirsiniz...')
            vize_notu = int(input('lütfen öğrencinin vize notunu giriniz : '))
            final_notu = int(input('lütfen öğrencinin final notunu giriniz : '))
            
            if 0 <= vize_notu <= 100 and 0 <= final_notu <= 100:
                ogrenciler[id_no]['not ortalaması'] = vize_notu * 0.40 + final_notu * 0.60
                print('not bilgisi ekleme işlemi başarıyla gerçekleştirilmiştir...')
            else:
                print('vize ve final notları 0 dan küçük 100 den büyük olamaz!')
    
    else:
        print('girmiş olduğunuz id sözlükte mevcut olmadığından dolayı not bilgisi ekleme işlemi gerçekleştirilemedi!')
         
         
     
ogrenciler = {}



while True:
    islem_menüsü()

    islem_türü = input('bir işlem türü seçiniz : ')

    if islem_türü == '1':
        ekle()
    
    if islem_türü == '2':
        listele()
    
    if islem_türü == '3':
        güncelle()
    
    if islem_türü == '4':
        sil()
    
    if islem_türü == '5':
        email_adres_ekle()
    
    if islem_türü == '6':
        not_bilgisi()
        
    if islem_türü == '7':
        print('uygulamadan çıkış yapıldı...')
        break
        
'''







import requests
import json
from pprint import pprint

'''
bolgeler_url = 'https://data.police.uk/api/forces'

response = requests.get(bolgeler_url)

print(response)

print('__' * 30)

print(response.status_code)

print('__' * 30)

print(response.url)

print('__' * 30)

#print(response.text)

print('__' * 30)

pprint(response.json())

print('__' * 300)

data = response.json()

for i in data:
    print(f"tüm id'ler = {i['id']} \t\t\t\t tüm isimler = {i['name']}")

'''





'''
suc_kategorileri_url = 'https://data.police.uk/api/crime-categories?'

payload = {'date' : '2020-01'}

response2 = requests.get(suc_kategorileri_url, params = payload)

print(response2)

print('__' * 30)

print(response2.status_code)

print('__' * 30)

print(response2.url)

print('__' * 100)

pprint(response2.json())

print('__' * 300)

'''





'''
suc_url = 'https://data.police.uk/api/leicestershire/NC04'

payload2 = {
    'category' : 'all-crime',
    'force' : 'city-of-london',
    'date' : '2020-01'}

response3 = requests.get(suc_url, params = payload2)

print(response3)

print('__' * 30)

data = response3.json()

pprint(data)

print('__' * 300)

print(f"merkez = {data['centre']}")
print()
print(f"enlem = {data['centre']['latitude']}")
print()
print(f"boylam = {data['centre']['longitude']}")
print()

print(f"açıklaması =\n {data['description']}")
print()

print(f"kimlik = {data['id']}")
print()

print(f"linkler = {data['links']}")
print()
for i in data['links']:
    print(f"linkler içindeki url = {i['url']}")
    print(f"linkler içindeki açıklaması = {i['description']}")
    print(f"linkler içindeki başlık = {i['title']}")

print()

print(f"isim = {data['name']}")
print()

print(f"nüfus = {data['population']}")
print()

print(f"url foce = {data['url_force']}")

'''



'''
url = "https://newsapi.org/v2/everything?q=apple&from=2024-03-13&to=2024-03-13&sortBy=popularity&apiKey=59ec4cdb786f49c485924479e7bdc09e"

response = requests.get(url)

data = response.json()

print(type(data))

print('__' * 30)

'''


'''
print(data['status'])
print()
print(data['totalResults'])
print()
print(data['articles'][0])
print()
print(data['articles'][0]['source']['name'])
print()
print(data['articles'][0]['author'])
print()
print(data['articles'][0]['title'])
print()
print(data['articles'][0]['url'])
print()
print(data['articles'][0]['publishedAt'])
'''

'''
print(data['articles'][1]['source']['id'])
print()
print(data['articles'][1]['source']['name'])
print()
print(data['articles'][1]['author'])
print()
print(data['articles'][1]['publishedAt'])

'''

'''
print(data['articles'][2]['source']['name'])
print()
print(data['articles'][2]['author'])
print()
print(data['articles'][2]['title'])
print()
print(data['articles'][2]['publishedAt'])

'''

'''
print(data['articles'][9]['source']['name'])
print()
print(data['articles'][9]['author'])
'''

'''
print(data['articles'][14]['publishedAt'])
print()
print(data['articles'][14]['source']['name'])
'''

'''
print(data['articles'][17]['source']['id'])
print()
print(data['articles'][17]['author'])
'''


'''
yazarlar_listesi = []


for i in data['articles']:
    yazarlar_listesi.append(i['author'])
pprint(yazarlar_listesi)
print('__' * 100)

while True:
        
    yazar_adi = input('bir yazar adı giriniz : ')

    if yazar_adi in yazarlar_listesi:
        print('yazar sözlükte mevcuttur...')

    else:
        print('yazar sözlükte mevcut değildir!!!')
        break
        
'''









    
    
        

   
        

            
































         




    
     







    
    
    




























































 

    


    











































