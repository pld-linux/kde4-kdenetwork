#!/bin/sh

PATH=/bin:/usr/bin

# Grab the full path to the smb.conf file
i=/etc/samba/smb.conf

# Create new smb.conf file with updated message command line
cp -f $i{,.rpmsave}
if grep -q '^include = /etc/samba/winpopup.conf' $i; then
	echo 'include = /etc/samba/winpopup.conf' >> $i
fi

cat > /etc/samba/winpopup.conf <<EOF
[global]
message command = $1 %s %m &
EOF

# Create a winpopup directory somewhere "safe"
#rm -rf /var/lib/winpopup --- a bit strong?
if [ ! -d /var/lib/winpopup ]; then
	mkdir -m 0777 -p /var/lib/winpopup
fi

chmod 0777 /var/lib/winpopup

# This is to help if somebody grades up from the old behavior
if [ -n "`ls -A /var/lib/winpopup/`" ]; then
	chmod 666 /var/lib/winpopup/*
fi

rm -f /var/lib/winpopup/message

# Force Samba to reread configuration
killall -HUP smbd
