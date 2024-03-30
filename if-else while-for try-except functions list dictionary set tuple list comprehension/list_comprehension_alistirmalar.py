
'''
liste = [1,2,3,4,5,6,7]

liste2 = [i*i for i in liste]

print(liste2)
print()

'''
'''
liste = [2,4,6,8,10,12,14]

liste2 = [i**3 for i in liste]

print(liste2)

'''

'''
liste = []

adet = int(input('listeye kaç adet eleman eklemek istiyorsunuz : '))

for i in range(adet):
    eleman = input('listeye eleman ekleyiniz : ')
    liste.append(eleman)
print(liste)
print()

liste2 = [i for i in liste]

print(liste2)

'''

'''
liste = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

liste2 = [i for i in liste if i % 2 == 0]

print(liste2)
print()

liste3 = [i for i in liste if i % 2 == 1]
print(liste3)
print()

liste4 = [i for i in liste if i % 3 == 0]
print(liste4)
print()

liste5 = [i for i in liste if i % 5 == 0]
print(liste5)
print()

liste6 = [i for i in liste if i % 7 == 0]
print(liste6)
print()

liste7 = [i**2 for i in liste if i % 2 == 0]
print(liste7)
print()

liste8 = [i**2 for i in liste if i % 2 == 1 and i > 15]
print(liste8)
print()

'''

'''
sayilar = [5,10,15,20]

harfler = 'abcd'

liste = []

for i in sayilar:
    for j in harfler:
        liste.append((i, j))

print(liste)

'''

'''
sayilar = [5,10,15]

harfler = 'abc'

liste = [(i, j) for i in sayilar for j in harfler]
print(liste)

'''

'''
sayilar = [5,6,7,8,9,10,11,12,13]

harfler = 'ABC'

liste = [(i, j) for i in sayilar for j in harfler if i % 2 == 0]

print(liste)

'''

'''
sayilar = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

harfler = 'ABCDE'

liste = [(i, j) for i in sayilar for j in harfler if i % 2 == 1 and i < 20]

print(liste)

'''

'''
liste1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

liste2 = [1,2,3,4,5,6,7,8]

liste3 = [i**2 for i in liste1 if i not in liste2]
print(liste3)

'''

'''
liste = [[10,20,30,40], [50,60,70,80,90], [100,110,120,130,140,150]]

liste2 = [j for i in liste for j in i]

print(liste2)

'''

'''
liste_metodlar = [i for i in dir(list) if not i.startswith('__')]

print(liste_metodlar)

'''

'''
tuple_metodlar = [i for i in dir(tuple) if not i.startswith('__')]

print(tuple_metodlar)

'''

'''
set_metodlar = [i for i in dir(set) if not i.startswith('__')]

print(set_metodlar)

'''
'''
dictionary_metodlar = [i for i in dir(dict) if not i.endswith('__')]

print(dictionary_metodlar)

'''

'''
liste = [i for i in range(20, 0, -1)]

print(liste)

'''
'''
liste = [i**2 for i in range(15, 0, -2)]

print(liste)

'''

'''
liste = [i for i in range(1,50) if i % 2 == 0 and i % 3 == 0]

print(liste)

'''

'''
liste = [-10,-9,-8,-7,-6,-5,0,3,5,7,8,10,11,12]

liste2 = [i for i in liste if i <= 0]

print(liste2)

'''

'''
meyveler = ['elma', 'armut', 'nar', 'muz', 'erik']

liste = [i.upper() for i in meyveler]

print(liste)

'''

'''
sebzeler = ['LİMON', 'HAVUÇ', 'KEREVİZ', 'LAHANA', 'TURP']

liste = [i.lower() for i in sebzeler]

print(liste)

'''

'''
renkler = ['Mavi', 'yeşil', 'Siyah', 'turuncu', 'sarı']

liste = [i[0] for i in renkler]

print(liste)

'''

'''
renkler = ['beyaz', 'eflatun', 'pembe', 'yeşil', 'kırmızı', 'mavi', 'turuncu', 'mor']

liste = [i for i in renkler if 'e' in i]

print(liste)

'''

'''
renkler = ['beyaz', 'eflatun', 'pembe', 'yeşil', 'kırmızı', 'mavi', 'turuncu', 'mor']

liste = [i for i in renkler if 'u' not in i]

print(liste)

'''














