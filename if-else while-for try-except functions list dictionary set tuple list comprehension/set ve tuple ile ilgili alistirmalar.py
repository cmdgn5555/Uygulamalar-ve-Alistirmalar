
# TUPLE

'''
sayilar = (2,3,4,5,6,7,8)

print(type(sayilar))

print(sayilar[0])
print(sayilar[-1])

for i in sayilar:
    print(i)


numbers = (1,)

print(type(numbers))
print(numbers)

rakamlar = 1, 2, 3, 4

print(type(rakamlar))

print(rakamlar)
print(rakamlar[-1])

isim, soyisim, yas = ('ali', 'sadi', 66)

print(isim)
print(soyisim)
print(yas)

personel = ('murat', 'arslan', 43)

print(personel[0])

# personel[0] = 'selim'

print(personel)

print(dir(tuple))
print('\n')

ögrenciler = ('bilal', 'sami', 'hakan', 'osman', 'caner', 'ali', 'sami', 'sami', 'bilal', 'bilal', 'ali', 'ali','ali','ali')

print(ögrenciler.count('ali'))

print(ögrenciler.index('caner'))

import sys

isim_list = ['ahmet', 'orhan', 'kemal', 12, 33, 50, 34.55555, True, False]
tuple_list = ('ahmet', 'orhan', 'kemal', 12, 33, 50, 34.55555, True, False)

print(sys.getsizeof(isim_list))
print('_____' * 90)
print(sys.getsizeof(tuple_list))

print(len(tuple_list))
print()

tuple = (12, 'abc', 'xyz', 'asdfd', 39, 1000, 44)
print(tuple[1:4])
print('*' * 300)
print(tuple.count(3432))

try: 
    print(tuple.index('abc'))

except Exception as e:
    print(f"try kısmındaki kodda sıkıntı çıktığı için {e}")

else:
    print('try kısmında hata yoktur. burasıda else kısmı..')

finally:
    print('bu finally bloğu her durumda çalışır!!!')

print('_____' * 200)


demet = (13,15,20,'elma','çilek','ayva')

del demet

print(demet)


liste = [3,5,6,7,8,'ali','veli']

del liste[2]

print(liste)




demet1 = (5,10,15,20,25)
demet2 = (20,25,30,35)
demet3 = ('python',)

demet4 = demet1 + demet2 + demet3
print(demet4)


demet = ([10,20,30], 40, (50,60,70))
print(demet[-1][1])
print(demet[0][0])

demet[0][-1] = 2345

print(demet)

demet[1] = 969679

print(demet)

x = 5
y = 10

print(x, y)
print()

(x, y) = (y, x)

print(x, y)



x, y, z = 1, 2, 3

print(x, y, z)
print()

(x, y, z) = (z, y, x)

print(x, y, z)

'''

'''
menü = (
    ('hamburger', 200),
    ('köfte', 250),
    ('iskender', 350),
    ('döner', 150),
    ('lahmacun', 100),
    ('kebap', 400)
)

for i, j,  in menü:
    print(i, j)

'''
'''
meyveler = ('elma', 'kivi', 'ananas', 'vişne')

liste = list(meyveler)

liste[0] = 'armut'

meyveler = tuple(liste)

print(meyveler)

'''

'''
meyveler = ('erik', 'şeftali', 'kayısı')

liste = list(meyveler)

liste.append('avokado')

meyveler = tuple(liste)

print(meyveler)

'''

'''
meyveler = ('muz', 'mandalina', 'incir', 'kavun')

liste = list(meyveler)

liste.remove('muz')

meyveler = tuple(liste)

print(meyveler)

'''

'''
demet1 = ('pırasa', 'patlıcan', 'fasulye', 'bezelye')

demet2 = demet1

print(demet2)

'''
'''
meyveler = ('portakal', 'şeftali', 'karpuz', 'çilek')

if 'çilek' not in meyveler:
    print('yok')
else:
    print('var')

'''

'''
while True:
    demet = ('php', 'python', 'java', 'css', 'html', 'c++', 'php', 'java', 'css')

    eleman = input('bir eleman giriniz : ')

    if eleman in demet:
        print(f"girmiş olduğunuz eleman demet içinde mevcuttur. index no : {demet.index(eleman)} ve elemanın demet içindeki sayısı : {demet.count(eleman)}")

    else:
        print(f"girmiş olduğunuz eleman olan {eleman} demet içersinde mevcut değildir!!!")
        break
'''

'''
demet = ('aaa','abc','xyz',123,456)

def tuple_length(x):
    return len(x)

print(tuple_length(demet))

'''

'''
demet1 = ('a', 'b', 'c')
demet2 = (1,2,3,4,5,6,7)

def concatenate_tuples(x, y):
    return x + y

print(concatenate_tuples(demet1, demet2))

'''

'''
demet = ('abc','xyz',15,20)
index = int(input('bir indeks no girin : '))

def access_element(tup, ind):
    return tup[ind]

print(access_element(demet, index))

'''
'''
demet = (3,10,10,10,3,2,2,2,2,2,2)

def count_element(tup, value):
    return tup.count(value)

print(count_element(demet, 2))

'''

'''
demet = ('ali', 'veli', 'python', 'java')

eleman = input('bir eleman giriniz : ')

def element_exists(tup, value):
    return value in tup

print(element_exists(demet, eleman))

'''

'''
demet = (1,5,9,10,'ababab', 'abcdef')

def tuple_to_string(tup):
    return str(tup)

print(tuple_to_string(demet))

'''

'''
demet = ('35', '40', '50', 'selam', 'merhaba')

eleman = input('bir eleman giriniz : ')

try:
    def find_index(tup, ind):
        return tup.index(ind)

    print(find_index(demet, eleman))

except:
    print('böyle bir eleman yok!!')

'''
'''
liste = ['salam', 'sosis', 'peynir', 'zeytin', 'tereyağı']

def list_to_tuple(lis):
    return tuple(lis)

print(list_to_tuple(liste))

'''

'''
demet = (46, 13, 22, 30, 88, 62)

def max_min_elements(tup):
    return max(tup), min(tup)

maksimum, minimum = max_min_elements(demet)
print('maksimum : ', maksimum)
print('minimum : ', minimum)

'''

'''
demet = ('s','e','l','a','m','l','a','r')

def tuple_to_single_string(tup):
    return ''.join(tup)

print(tuple_to_single_string(demet))
'''

'''
demet = (10,20,30,40,50,60)

sil = int(input('silinecek sayıyı giriniz : '))

def remove_element(tup, value):
    return tuple(x for x in tup if x != value)

print(remove_element(demet, sil))

'''

'''
demet1 = (5,10,15,20,25,30)
demet2 = (20,25,30,35,40,45)

def common_elements(tup1, tup2):
    return tuple(i for i in tup1 if i in tup2)

print(common_elements(demet1, demet2))

'''
'''
demet = (13,4,5,8,15,2,18)

def sort_tuple(tup):
    return tuple(sorted(tup))

print(sort_tuple(demet))

'''
'''
demet = (3,4,6,8,12,30)

def sum_tuple(tup):
    return sum(tup)

print(sum_tuple(demet))

'''

'''
demet1 = (4,8,12,16,20,24,28)
demet2 = (24,28,32,36,40)

def merge_and_remove_duplicates(tup1, tup2):
    return tuple(set(tup1).union(tup2))

print(merge_and_remove_duplicates(demet1, demet2))

'''
'''
demet1 = (10,20,30,40)
demet2 = (50,60,70,80)

def merge_tuples(tup1, tup2):
    return tuple(tup1 + tup2)

print(merge_tuples(demet1, demet2))

'''

'''
demet1 = (10,20,30,40,50,60,10,20,30)


def remove_duplicates_from_tuples(tup1):
    return tuple(set(tup1))

print(remove_duplicates_from_tuples(demet1))

'''

'''
demet1 = (80, 35, 22, 27, 60, 38)

def first_and_last_element(tup1):
    return tup1[0], tup1[-1]

first, last = first_and_last_element(demet1)
print('ilk eleman : ', first)
print('son eleman : ', last)

'''
'''
demet1 = (2, 3, 5, 6, 8, 10)

def int_to_str_tuple(tup1):
    return tuple(str(i) for i in tup1)

print(int_to_str_tuple(demet1))

'''
'''
demet = (11,12,13,14,15,16,17,18)

def count_even_odd(tup):
    even_count = tuple(i for i in tup if i % 2 == 0)
    odd_count = tuple(i for i in tup if i % 2 == 1)
    return even_count, odd_count

even_numbers, odd_numbers = count_even_odd(demet)
print('çift sayılar : ', even_numbers, 'adedi = ', len(even_numbers))
print('tek sayılar : ', odd_numbers, 'adedi =', len(odd_numbers))

'''
'''
demet = (2,3,4,5,10,20)

def product_tuple():
    product = 1
    for i in demet:
        product *= i
    return product

print(product_tuple())

'''

'''
demet = (5,6,7,8,9,10)

def add_tuple():
    toplam = 0
    for i in demet:
        toplam += i
    return toplam

print(add_tuple())

'''

'''
demet1 = (1,2,3,4,5,6,7,8)
demet2 = (1,4,6,8)

def tuple_difference(tup1, tup2):
    return tuple(i for i in tup1 if i not in tup2)

print(tuple_difference(demet1, demet2))

'''
'''
demet = (23, 11, 14, 46, 53, 5, 8)

def second_largest(tup):
    sorted_tuple = sorted(demet)
    return sorted_tuple[-2]

print(second_largest(demet))

'''
'''
demet = (96,7,12,44,51,68,90)

def smallest(tup):
    sorted_tuple = sorted(tup)
    return sorted_tuple[0]

print(smallest(demet))

'''
'''
örnek_liste = [(25, 10), (13, 25), (18, 20), (44, 52), (25, 4), (11, 25)]

yirmibes_listesi = []
for i in örnek_liste:
    if i[0] == 25 or i[1] == 25:
        yirmibes_listesi.append(i)
print(yirmibes_listesi)

'''





# SET


# print(dir(set))

'''
küme = {'css', 'html', 'python', 'java', 'php', 'css', 'css', 'java', 'html', 'html', 'php'}
print(type(küme))
print(küme)
'''

'''
a = 'python'
print(a)
print()

küme = set(a)
print(küme)
'''
'''
küme = {12, 13, 14, 15}
print(type(küme))
print(küme)
küme.add(16)
print(küme)
'''

'''
a = 'python'

küme = set(a)
print(küme)
print()

küme.update('yazılım')
print(küme)

küme.remove('p')
print(küme)
'''

'''
a = 'serkan'

küme = set(a)
print(küme)
print()

küme.pop()
print(küme)
'''

'''
a = 'caner'

küme = set(a)
print(küme)
print()

küme.discard('c')
print(küme)
'''

'''
sample_set = {}

print(sample_set)

print(type(sample_set))



asal_sayilar = {3,5,7,11,17,19,23,29}
asal_sayilar.add('python')
print(asal_sayilar)
print('____'* 50)

asal_sayilar.add(29)
print(asal_sayilar)
print('____'* 50)

asal_sayilar.add(True)
asal_sayilar.add(430943)
print(asal_sayilar)
print('____'* 50)

asal_sayilar.remove(True)
print(asal_sayilar)
print('____'* 50)

asal_sayilar.discard(23)
print(asal_sayilar)
print('____'* 50)

asal_sayilar.discard(250)
print(asal_sayilar)
print('____'* 50)

asal_sayilar.pop()
print(asal_sayilar)
print('____'* 50)

sample_set = set()
sample_set.pop()
print(sample_set)

'''

'''
asal_sayilar = {3,5,7,11,13,17,19,23}
print(asal_sayilar)
print('___' * 50)

asal_sayilar.update({29, 31, 37})
print(asal_sayilar)
print('___' * 50)

asal_sayilar.update(('abc', 'xyz'), [9999, 8888])
print(asal_sayilar)
print('___' * 50)

asal_sayilar.clear()
print(asal_sayilar)
print('___' * 50)

cift_sayilar = {2,4,6,8,10,12}
print(cift_sayilar)
print(type(cift_sayilar))
print('___' * 50)

del cift_sayilar
print(cift_sayilar)

'''
'''
cift_sayilar = {i for i in range(1,51) if i % 2 == 0}
print(cift_sayilar)
print('__' * 30)

tek_sayilar = {i for i in range(1,51) if i % 2 == 1}
print(tek_sayilar)
print('__' * 30)

üc_sayisinin_katlari = {i for i in range(1, 51) if i % 3 == 0}
print(üc_sayisinin_katlari)
print('__' * 30)

bes_sayisinin_katlari = {i for i in range(1, 51) if i % 5 == 0}
print(bes_sayisinin_katlari)
print('__' * 30)

print(len(cift_sayilar))
print(len(tek_sayilar))
print(len(üc_sayisinin_katlari))
print(len(bes_sayisinin_katlari))
print('__' * 30)

'''

#print(cift_sayilar.union(tek_sayilar))
#print('__' * 30)
#
#print(üc_sayisinin_katlari.union(bes_sayisinin_katlari))
#print('__' * 30)
#
#print(tek_sayilar.union(üc_sayisinin_katlari))

#print(cift_sayilar.intersection(tek_sayilar))
#print('__' * 30)
#print(cift_sayilar.intersection(bes_sayisinin_katlari))
#print('__' * 30)
#print(tek_sayilar.intersection(üc_sayisinin_katlari))

#print(cift_sayilar.difference(bes_sayisinin_katlari))
#print('__' * 30)
#print(bes_sayisinin_katlari.difference(üc_sayisinin_katlari))

#print(cift_sayilar.symmetric_difference(bes_sayisinin_katlari))

#alt_küme = {11,13,15,17,19}
#
#if alt_küme.issubset(tek_sayilar):
#    print('alt küme tek sayılar kümesinin alt kümesidir.')
#
#else:
#    print('alt küme tek sayılar kümesinin alt kümesi değildir!!!!.')

#alt_küme = {21, 33, 39, 45}
#
#if alt_küme.issubset(üc_sayisinin_katlari):
#    print('alt küme üç sayısının katları kümesinin alt kümesidir.')
#
#else:
#    print('alt küme üç sayısının katları kümesinin alt kümesi değildir!!!!.')

#alt_küme = {16, 18, 24, 30, 36}
#
#if cift_sayilar.issuperset(alt_küme):
#    print('cift sayilar kümesi alt kümenin üst kümesidir.')
#
#else:
#    print('cift sayilar kümesi alt kümenin üst kümesi değildir!!!')

#alt_küme = {15, 20, 25, 30}
#
#if bes_sayisinin_katlari.issuperset(alt_küme):
#    print('beş sayısının katları kümesi alt kümenin üst kümesidir.')
#
#else:
#    print('beş sayısının katları kümesi alt kümenin üst kümesi değildir!!!')

#küme1 = {2,4,7,9}
#print(küme1)
#küme2 = {9,4,2,7}
#print(küme2)
#
#if küme1 == küme2:
#    print('küme1 ile küme2 eşittir...')
#
#else:
#    print('küme1 ile küme2 eşit değildir!!!...')

#yazi = 'python yazılım programı'
#print(yazi)
#print()
#
#string_küme = set(yazi)
#print(string_küme)
#print()
#
#böl = set(yazi.split())
#print(böl)

#mail = 'ahmet.mehmet.12345@gmail.com'
#
#küme = set(mail)
#
#print(küme)
#
#böl = set(mail.split('.'))
#
#print(böl)

'''
yazi = 'merhaba selam hello naber'

sesli_harfler = {'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü'}

küme_yazi = set(yazi)
print(küme_yazi)
print()

string_sesli_harfler = küme_yazi.intersection(sesli_harfler)
print(string_sesli_harfler)

'''

'''
cümle = input('bir cümle yazınız : ')
print(cümle)
print()

sesli_harfler = {'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü'}
print(sesli_harfler)
print()

kümeye_cevrilmis_cümle = set(cümle)
print(kümeye_cevrilmis_cümle)
print()

cümle_icinde_sesli_harf_kontrol = kümeye_cevrilmis_cümle.intersection(sesli_harfler)
print(cümle_icinde_sesli_harf_kontrol)

'''
'''
cümle = input('bir cümle yazınız : ')
print(cümle)
print()

rakamlar = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
print(rakamlar)
print()

kümeye_cevrilmis_cümle = set(cümle)
print(kümeye_cevrilmis_cümle)
print()

cümle_icinde_rakam_kontrol = kümeye_cevrilmis_cümle.intersection(rakamlar)
print(cümle_icinde_rakam_kontrol)

'''
'''
cümle = input('bir cümle yazınız : ')
print(cümle)
print()

kümeye_cevrilmis_cümle = set(cümle)
print(kümeye_cevrilmis_cümle)
print()

harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
print(harfler)
print()

kümeye_cevrilmis_harfler = set(harfler)
print(kümeye_cevrilmis_harfler)
print()


for i in kümeye_cevrilmis_harfler:
    if i in kümeye_cevrilmis_cümle:
        cümle_icindeki_harfler_kontrol = set(i)
        

        print(cümle_icindeki_harfler_kontrol)

'''
'''
cümle = input('bir cümle giriniz : ')
print(set(cümle))

if 'a' in cümle:
    print('a harfi cümle içinde mevcuttur.')

else:
    print('a harfi cümle içinde mevcut değildir!!!')

'''
'''
frz_set = frozenset(['java', 'css', 'html', 10, 23])

küme = {'hi', 'hello'}

print(frz_set)
print()
print(type(frz_set))

frz_set.union(küme)
print(frz_set)

'''

'''
küme = {3, 6, 144, 'yazılım'}
print(küme)
print()
küme2 = küme.copy()
print(küme2)

'''








        




























