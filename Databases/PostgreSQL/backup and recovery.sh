#1. Prepare disk space for the archived files.
#By default, PostgreSQL maintains a write ahead log(WAL) in the pg_xlog subdirectory of the server #data directory. By default, these files are rotating and get overwritten, under archiving mode, we #configure PostgreSQL to copy WAL files to archive directory, to be noted, you need to take care of #the archive directory by yourself.
BKUPDIR=/home/backups/pgsql_data


#2. PostgreSQL setting, a restart is need to enable the change
#The following three essential, you can even call a script in archive_command
wal_level = archive
archive_mode = on
archive_command = '/bin/cp -p %p /home/backups/archivelogs/%f </dev/null'

#The following two are optional, suggest you test your system before you chagne them

#To put a limit on how old unarchived data can be, you can set archive_timeout to force the server to switch to a new WAL segment file at least that often. Note that archived files that are archived early due to a forced switch are still the same length as completely full files. It is therefore unwise to set a very short archive_timeout — it will bloat your archive storage. archive_timeout settings of a minute or so are usually reasonable.

archive_timeout = 60
checkpoint_timeout = 1h


#3. continuous backup script
#set -v        # debugging tools
#set -x

cmd=`basename $0`


BKUPDIR=/home/backups/pgsql_data; export BKUPDIR
LOG=/home/backups/pgsql_data/backuplog.`date +%m%d%y%H`.log; export LOG

typeset -i res

function exitMsg() {
  mylog=$1
  mymsg=$2
  echo "$cmd: Unsuccessful PostgreSQL database hotbackup at `/bin/date`" >>$mylog
  echo "$mymsg" >>$mylog
  cat $mylog >> $LOG
  cat "$LOG" | mail -s "PostgreSQL database hotbackup failed (`/bin/date`)" $EMAIL
  exit 1
}

LOG1=$LOG"_hotbackup"
cat /dev/null >$LOG1 2>/dev/null

echo "" >> $LOG
echo "On `/bin/date` Daily PostgreSQL database hot backup:" >> $LOG

/usr/bin/psql -U postgres -c "SELECT pg_start_backup('/home/backups/pgsql_data/label');" postgres &>backup.log

nice tar -zcf /home/backups/pgsql_data/data.`date +%m%d%y%H`.tgz /var/lib/pgsql/9.1/data >>backup.log

/usr/bin/psql -U postgres -c "SELECT pg_stop_backup();" postgres &>backup1.log

res=$?
if [ $res -ne 0 ] ; then
  exitMsg $LOG1 "ERROR: PostgreSQL database hotbackup failed."
fi

nice /usr/bin/find /home/backups/archivelogs -not -name "*.bz2" | xargs -n 1 -P 5 bzip2
 

cat $LOG1 >> $LOG
cat /dev/null >$LOG1 2>/dev/null
rm $LOG1 2>/dev/null
cat backup1.log >> backup.log
cat backup.log >> $LOG
rm backup.log backup1.log

echo "On `/bin/date` End of PostgreSQL hotbackup :" >> $LOG
cat "$LOG" | mail -s "PostgreSQL Hotbackup SUCCEEDED! (`/bin/date`)" $EMAIL;


exit 0


