#!/system/bin/sh
echo Content-type: text/html
echo ""

if [ -e /system/etc/ssh/passwd ]; then
   PASSWD=`/system/xbin/cat /etc/ssh/passwd`
   echo $PASSWD
else
echo "*!ERROR!*"
fi