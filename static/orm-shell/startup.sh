#!/bin/bash
#
SOFTHOME=/replicate/sync-s1

echo "begin to startup processes.............."
sh $SOFTHOME/scripts/start_vagentd>/dev/null
sleep 1
sh /u01/ss/scripts/check
echo "-----------------------startup completed--------------------------------"
echo "startup completed!"