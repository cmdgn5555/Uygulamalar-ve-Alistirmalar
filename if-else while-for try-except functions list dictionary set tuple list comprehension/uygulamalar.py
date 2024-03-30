
'''
import random
import time

def rastgele_secim():
    x = random.randint(1, 3)
    if x == 1:
        return 'taş'
    elif x == 2:
        return 'kagıt'
    else:
        return 'makas'

kullanici_skoru = 0
ps_skoru = 0

while True:
    kullanici_secimi = input('(taş mı = ? kagıt mı = ? makas mı = ?) : ').lower()

    random_choice = rastgele_secim()
    print('random : ', random_choice)

    if kullanici_secimi == 'taş' or kullanici_secimi == 'kagıt' or kullanici_secimi == 'makas':

        if random_choice == kullanici_secimi:
            print('berabere')
            print()

        elif random_choice == 'taş' and kullanici_secimi == 'kagıt':
            print('kazandınız..')
            print()
            kullanici_skoru += 1

        elif random_choice == 'makas' and kullanici_secimi == 'taş':
            print('kazandınız..')
            print()
            kullanici_skoru += 1

        elif random_choice == 'kagıt' and kullanici_secimi == 'makas':
            print('kazandınız..')
            print()
            kullanici_skoru += 1

        else:
            print('kaybettiniz!!')
            print()
            ps_skoru += 1
    
    else:
        print('lütfen taş, kagıt yada makas dışında başka bir input girmeyiniz!!!')
    
    print('kullanıcı skoru : ', kullanici_skoru, 'ps skoru : ', ps_skoru)
    print()

    if ps_skoru == 5 or kullanici_skoru == 5:
        time.sleep(3)
        break

if ps_skoru > kullanici_skoru:
    print(f'OYUNU KAYBETTİNİZ!\n\noyun sonucu = ps skoru : {ps_skoru}\nkullanıcı skoru : {kullanici_skoru}')

else:
    print(f'OYUNU KAZANDINIZ..\n\noyun sonucu = ps skoru : {ps_skoru}\nkullanıcı skoru : {kullanici_skoru}')

'''



'''
import random


def rakam_sec():
    return random.randint(1,10)
    
ps_skor = 0
kullanici_skor = 0


while True:

    try:
        kullanici_secimi = int(input('sadece 5 rakamını giriniz : '))
        
        rastgele_rakam = rakam_sec()
        print(f"rastgele seçilen = {rastgele_rakam}")

        if kullanici_secimi == 5:
            
            if kullanici_secimi == rastgele_rakam:
                print('berabere...')
            
            elif kullanici_secimi > rastgele_rakam:
                print('kazandınız.')
                kullanici_skor += 1
            
            else:
                print('kaybettiniz!')
                ps_skor += 1
        
        else:
            print('lütfen sadece 5 rakamını giriniz!!!')
        
        print(f"kullanıcı skoru = {kullanici_skor} ps skoru = {ps_skor}")
        
        if kullanici_skor == 5 or ps_skor == 5:
            break
    
    except:
        print('lütfen harf girmeyiniz!!')

if kullanici_skor > ps_skor:
    print(f'OYUNU KAZANDINIZ..\n\noyun sonucu = ps skoru : {ps_skor}\n\n\tkullanıcı skoru : {kullanici_skor}')

else:
    print(f'OYUNU KAYBETTİNİZ..\n\noyun sonucu = ps skoru : {ps_skor}\n\n\tkullanıcı skoru : {kullanici_skor}')

'''


'''
ali_account = {
    'account_no': 12345,
    'full_name': 'Ali Yiğit',
    'password': 123,
    'balance': 3000,
    'additional_balance': 1000
}

ahmet_account = {
    'account_no': 98765,
    'full_name': 'Ahmet Şener',
    'password': 123,
    'balance': 5000,
    'additional_balance': 1000
}

mehmet_account = {
    'account_no': 101010,
    'full_name': 'Mehmet Keskin',
    'password': 123,
    'balance': 8000,
    'additional_balance': 1000
}

users = [ali_account, ahmet_account, mehmet_account]

def login(account_no, password):
    account = {}

    for user in users:
        if user["account_no"] == account_no and user["password"] == password:
            account.update(user)
            print(account)
            break
    return account


def menu(account):
    print(f"""
    Welcome, {account['full_name']}
    ==============================
    1 - Withdraw Money          
    2 - Deposit Money            
    3 - Account Info            
    4 - EFT                     
    5 - Exit                     
    """)


def balance_result(account):
    print(f'You have {account["balance"]} TL.\nAccount No: {account["account_no"]}\n'
          f'Additional Balance has: {account["additional_balance"]}')


def withdraw_money(amount, account):
    if account['balance'] >= amount:
        account['balance'] -= amount
        print("Do not forget to take money..!")
        balance_result(account)
    else:
        total_balance = account['balance'] + account['additional_balance']
        print(f"your total balance : {total_balance}")

        if total_balance >= amount:
            use_additional_balance = input('Insufficent balance. Do you want to use additional balance? ("yes" or "no")').lower()

            if use_additional_balance == 'yes':
                amount_used_additional_balance = amount - account['balance']
                account['balance'] = 0
                account['additional_balance'] -= amount_used_additional_balance
                balance_result(account)
            
            elif use_additional_balance == 'no':
                    print('Transaction has been cancelled..!')
                    balance_result(account)
            
            else:
                print('Please choose valid answer. ("yes" or "no")')
        
        else:
            print('Insufficent total balance. Transaction has been cancelled..!')


def deposit_money(account, amount):
    account['balance'] += amount
    if account['additional_balance'] < 1000:
        transferred_amount = 1000 - account['additional_balance']
        account['balance'] -= transferred_amount
        account['additional_balance'] += transferred_amount
    balance_result(account)


def show_account_info(account) -> None:
    print(f"Account Information\n"
          f"===================== "
          f"Full Name: {account['full_name']} "
          f"Account No: {account['account_no']} "
          f"Password: {account['password']} "
          f"Balance: {account['balance']} "
          f"Additional Balance: {account['additional_balance']} ")


def eft_transaction(sender_account, receiver_account_no, amount):
    for user in users:
        if user['account_no'] == receiver_account_no:
            withdraw_money(amount, sender_account)
            deposit_money(user, amount)
    
        
def main():
    
    user_account = login(int(input('Account No: ')), int(input('Password: ')))

    if user_account != {}:
        menu(user_account)
        
        while True:
            
            process = int(input('Please choose a process: '))

            if process == 1:
                amount = int(input('Amount: '))
                withdraw_money(amount, user_account)
            
            elif process == 2:
                amount = int(input('Amount: '))
                deposit_money(user_account, amount)
            
            elif process == 3:
                show_account_info(user_account)
            
            elif process == 4:
                amount = int(input('Amount: '))
                receiver_no = input('Receiver Account No: ')
                eft_transaction(user_account, receiver_no, amount)
                
            
            elif process == 5:
                print('Application has been closing..!')
                break
            
            else:
                print('Please choose a valid process number..!')
    
    else:
        print('Authentication failed. Please check your credentials..!')

main()

'''


'''
cem_account = {
    'id_no': 11111,
    'full_name': 'Cem Ayas',
    'maaş': 50000,
    'prim' : 0,
    
}

can_account = {
    'id_no': 22222,
    'full_name': 'Can Ermutlu',
    'maaş': 30000,
    'prim' : 0

    
}

cumali_account = {
    'id_no': 33333,
    'full_name': 'Cumali Alparslan',
    'maaş': 40000,
    'prim' : 0
    
}


personeller = [cem_account, can_account, cumali_account]

personeller_info = {}

def menu():
    print(f" 1 - personel bilgilerini göster\n"
            "2 - personele prim yatır\n"
            "3 - personel maaşına zam yap\n"
            "4 - personele avans ver\n"
            "5 - personelin toplam maaşını göster(prim + maaş)\n"
            "6 - mevcut tüm personelleri göster\n")

menu()


def bilgileri_göster(personel_id):
    
    for personel in personeller:
        personeller_info.update(personel)
        if personeller_info['id_no'] == personel_id:
            print(f"bilgileri istenen personelin adı = {personeller_info['full_name']} maaşı = {personeller_info['maaş']}")
            
    else:
        print('böyle bir id numarasına sahip personel bulunamadı!')
            
        

def prim_yatir(id, prim_miktarı):
    
    for personel in personeller:
        if personel['id_no'] == id and prim_miktarı <= personel['maaş'] / 4:
            personel['prim'] = personel['prim'] + prim_miktarı
            print(f"prim yatırılan personelin adı = {personel['full_name']} primi = {personel['prim']}")
            break
    else:
        print('yatırılacak prim miktarı personelin maaşının çeyreğinden fazla olamaz!')
        print('böyle bir id numarasına sahip personel bulunamadı!')
            
            
            
def maas_zam(personel_id, zam_orani):
    
    for personel in personeller:
        if personel['id_no'] == personel_id and zam_orani <= 1.5:
            personel['maaş'] = personel['maaş'] * zam_orani
            print(f"maaşı güncellenen personelin adı = {personel['full_name']} zamlı maaşı = {personel['maaş']}")
            break
    else:
        print('yapılacak zam oranı yüzde 50 den fazla olamaz!')
        print('böyle bir id numarasına sahip personel bulunamadı!')



def avans_ver(id, avans):

    for personel in personeller:
        if personel['id_no'] == id and avans <= personel['maaş'] / 2:
            personel['maaş'] = personel['maaş'] - avans
            print(f"avans verilen personelin adı = {personel['full_name']} verilen avans miktarı = {avans} personelin bir sonraki ay alacağı maaş = {personel['maaş']}")
            break
    else:
        print('personele verilecek olan avans tutarı personelin maaşının yarısından fazla olamaz!')
        print('böyle bir id numarasına sahip personel bulunamadı!')


def toplam_maas_göster(id):

    for personel in personeller:
        if personel['id_no'] == id:
            print(f"personelin adı = {personel['full_name']}\npersonelin toplam maaşı = {personel['maaş'] + personel['prim']}")
            break
        else:
            print('böyle bir id numarasına sahip personel bulunamadı!')
            break


def mevcut_personeller():
    print(personeller)


def main():
    while True:
        islem_türü = int(input('bir işlem türü seçiniz : '))
        
        if islem_türü == 1:
            id_no = int(input('bilgileri göstermek için bir id no giriniz : '))
            bilgileri_göster(id_no)
        
        
        if islem_türü == 2:
            id_no = int(input('prim yatırılacak personelin id numarasını giriniz : '))
            yatırılacak_miktar = int(input('yatırılacak miktarı yazınız : '))
            prim_yatir(id_no, yatırılacak_miktar)
            
            
        if islem_türü == 3:
            id_no = int(input('maaş güncellemek için bir id no giriniz : '))
            maas_zam_orani = float(input('zam oranı giriniz : '))
            maas_zam(id_no, maas_zam_orani)
        

        if islem_türü == 4:
            id_no = int(input('avans verilecek personelin id numarasını giriniz : '))
            avans_miktarı = int(input('verilecek avans miktarını yazınız : '))
            avans_ver(id_no, avans_miktarı)
        

        if islem_türü == 5:
            id_no = int(input('personelin toplam maaşını(prim + maaş) görmek için bir id no giriniz : '))
            toplam_maas_göster(id_no)


        if islem_türü == 6:
            mevcut_personeller()

main()

'''


















   
    

        
    
    











        




    
        





         



    
