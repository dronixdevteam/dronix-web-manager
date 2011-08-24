#!/system/bin/sh


PASSWD=`echo "$QUERY_STRING" | /system/xbin/grep -oE "(^|[?&])passwd=[^&]+" | /system/xbin/sed "s/%20/ /g" | /system/xbin/cut -f 2 -d "="`
#USER=`echo "$QUERY_STRING" | grep -oE "(^|[?&])user=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`

echo Content-type: text/html
echo ""

/system/xbin/mount -o rw,remount -t yaffs2 /dev/block/mtdblock4 /system
echo $PASSWD > /system/etc/ssh/passwd
/system/xbin/mount -o ro,remount -t yaffs2 /dev/block/mtdblock4 /system

echo "*!SUCCESS!*"