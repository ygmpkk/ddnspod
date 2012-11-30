#!/bin/bash

EMAIL=''
PASSWORD=''
MYDOMAIN=''
DOMAINID=""
SUBDOMAIN=""
noupdate="No Update"

CURRIP=`curl -s http://iframe.ip138.com/ic.asp | grep -Eo [0-9]\{1,3\}+\.[0-9]\{1,3\}+\.[0-9]\{1,3\}+\.[0-9]\{1,3\}+ | head -n 1`
OLDIP=''
IPFILE="/var/run/lastip"

#echo $CURRIP
if [ -f "$IPFILE" ]; then
    OLDIP=`cat $IPFILE`
    if [ -z $OLDIP ]; then
        echo $CURRIP > $IPFILE
    fi
else
    echo $CURRIP > $IPFILE
    echo $CURRIP
fi

if [ "$CURRIP" != "$OLDIP" ]; then
    LOGIN=`curl -k -s -X GET 'https://www.dnspod.com/api/auth?email='$EMAIL'&password='$PASSWORD''`
    LOGININFO=`echo "$LOGIN" | sed -e 's:\:\s:=:g' | sed -r 's/^.{1}(.*).{1}$/\1/g' | sed 's/\"//g'`
    #DOMAIN=`curl -k -s -X GET 'https://www.dnspod.com/api/records/'$MYDOMAIN'' -b ''$LOGININFO''`
    #echo "curl -k -s -X PUT 'https://www.dnspod.com/api/records/$MYDOMAIN/$DOMAINID' -d '{\"sub_domain\":""$SUBDOMAIN"",\"area\":\"0\",\"record_type\":\"A\",\"value\":""$CURRIP""}' -b '$LOGININFO'"
    DOMAIN=`curl -k -s -X PUT 'https://www.dnspod.com/api/records/'$MYDOMAIN'/'$DOMAINID'' -d 'sub_domain='$SUBDOMAIN'&area=0&record_type=A&ttl=600&value='$CURRIP'' -b ''$LOGININFO''`
    echo $DOMAIN
    echo $DOMAIN | mail -s "Update Domain" root
    echo $CURRIP > $IPFILE
else
    echo "echo '$noupdate'"
fi
