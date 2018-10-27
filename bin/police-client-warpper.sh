#!/bin/bash 

HOSTNAME=$(hostname)
URL="https://police.netx.as/police/$HOSTNAME";
CURL="curl -s -k -H 'Content-Type: text/xml'"
POLICEC="/usr/bin/police-client"

#cat request.xml | police-client 
$CURL $URL | $POLICEC | $CURL --data-binary @- $URL

