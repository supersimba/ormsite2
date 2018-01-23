export ORACLE_SID=comstardb
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1
export ORACLE_BASE=/u01/app/oracle
export LD_LIBRARY_PATH=/replicate/elib32


soft_home=$1

$soft_home/bin/vman<<EOF
@$soft_home/bin/dic.vm
exit
EOF


sleep 1 
echo "objects of database export completed"