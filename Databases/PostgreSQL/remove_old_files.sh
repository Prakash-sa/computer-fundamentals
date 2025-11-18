
#4. cleanup old backups script
set -x
#
#  Cleanup old database log files daily.
#

# ask time duration remove the old file only

if [ `whoami` != 'postgres' ]; then
  echo '$cmd: you must be logged in as the postgres user'
  exit 1
fi

nice /usr/bin/find /home/backups/pgsql_data -name "*.log*" \
-mtime +1 -exec rm {} \;
#
nice /usr/bin/find /home/backups/pgsql_data -name "*.tgz" \
-mtime +1 -exec rm {} \;
#
nice /usr/bin/find /home/backups/archivelogs -name "*.bz2" \
-mtime +1 -exec rm {} \;

