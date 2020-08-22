echo '[!] O`rnatilmoqda...'
pacman -Sy > install.log
echo
echo '[!] Tekshirilmoqda...'
echo '    Python3 o`rnatilmoqda'
yes | pacman -S python3 python-pip --needed &>> install.log
echo '    PHP o`rnatilmoqda'
yes | pacman -S php --needed &>> install.log
echo '    Ssh o`rnatilmoqda'
yes | pacman -S openssh --needed &>> install.log
echo '    Requests qabul qilinmoqda'
pip3 install requests &>> install.log
echo
echo '[!] Sozlanmoqda...'
chmod 777 template/nearyou/php/info.txt
chmod 777 template/nearyou/php/result.txt
echo
echo '[!] O`rnatildi va sozlandi!'
