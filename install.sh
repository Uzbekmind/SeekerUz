echo '[!] Yangilanmoqda...'
apt-get update > install.log
echo
echo '[!] O`rnatilmoqda...'
echo '    Python3 o`rnatilmoqda...'
apt-get -y install python3 python3-pip &>> install.log
echo '    PHP o`rnatilmoqda'
apt-get -y install php &>> install.log
echo '    Ssh o`rnatilmoqda...'
apt-get -y install ssh &>> install.log
echo '    Requests qabul qilinmoqda...'
pip3 install requests &>> install.log
echo
echo '[!] Sozlanmoqda...'
chmod 777 template/nearyou/php/info.txt
chmod 777 template/nearyou/php/result.txt
echo
echo '[!] O`rnatildi va sozlandi!'
