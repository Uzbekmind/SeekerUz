echo '[!] Yangilanmoqda...'
apt update > install.log
echo
echo '[!] O`rnatilmoqda...'
echo '    Python3 o`rnatimoqda'
apt install python &>> install.log
echo '    PHP o`rnatilmoqda'
apt install php &>> install.log
echo '    Ssh o`rnatilmoqda'
apt install openssh &>> install.log
echo 'Requests qabul qilinmoqda'
pip3 install requests &>> install.log
echo
echo '[!] Sozlanmoqda...'
chmod 777 template/nearyou/php/info.txt
chmod 777 template/nearyou/php/result.txt
echo
echo '[!] O`rnatildi va sozlandi!'