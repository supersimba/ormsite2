export ORACLE_SID=comstardb
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1
export ORACLE_BASE=/u01/app/oracle
export LD_LIBRARY_PATH=/replicate/elib32


soft_home="/replicate/sync-s1"
echo $soft_home

/replicate/sync-s1/bin/vman<<EOF
@/replicate/sync-s1/bin/vm
quit

EOF
echo "data export completed"