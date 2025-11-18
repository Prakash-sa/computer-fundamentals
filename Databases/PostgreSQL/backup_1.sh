#!/bin/bash
 


LOG=/home/backups/pgsql_data/backuplog.`date +%m%d%y%H`.log; export LOG

configuring_continuous_archiving ()
{
echo "Configuring Continuous Archiving ..."

#Create the archive directory (if not present).
sudo mkdir database_archive

#Give the default PostgreSQL user, postgres, permission to write to this directory.
sudo chown postgres:postgres database_archive

#Enable archiving in the postgresql.conf (/etc/postgresql/12/main/postgresql.conf) file.
#sudo nano /etc/postgresql/12/main/postgresql.conf

#update the following
archive_mode = on
archive_command = 'test ! -f /home/backups/archivelogs/%f && cp %p /home/backups/archivelogs/%f'
wal_level = replica


sed -i '/archive_mode = */d' /etc/postgresql/12/main/postgresql.conf      
sed -i '/archive_command = = */d' /etc/postgresql/12/main/postgresql.conf  
sed -i '/wal_level = */d' /etc/postgresql/12/main/postgresql.conf  


echo "archive_mode = on" >> /etc/postgresql/12/main/postgresql.conf
echo "archive_command = 'test ! -f /home/backups/archivelogs/%f && cp %p /home/backups/archivelogs/%f'" >> /etc/postgresql/12/main/postgresql.conf
echo "wal_level = replica" >> /etc/postgresql/12/main/postgresql.conf

echo "archive_mode = on" >> tmp.sh
echo "archive_command = 'test ! -f /home/backups/archivelogs/%f && cp %p /home/backups/archivelogs/%f'" >> tmp.sh
echo "wal_level = replica" >> tmp.sh
#The following two are optional, suggest you test your system before you chagne them

#To put a limit on how old unarchived data can be, you can set archive_timeout to force the server to switch to a new WAL segment file at least that often. Note that archived files that are archived early due to a forced switch are still the same length as completely full files. It is therefore unwise to set a very short archive_timeout — it will bloat your archive storage. archive_timeout settings of a minute or so are usually reasonable.

echo "archive_timeout = 60" >> /etc/postgresql/12/main/postgresql.conf
echo "checkpoint_timeout = 1h" >> /etc/postgresql/12/main/postgresql.conf



echo "Configuring Continuous Archiving Done!"
 
}

physical_backup(){

echo "Physical Backup ..."

#Make the backup directory:
sudo mkdir database_backup

#Ensure that the postgres user has permission to write to the directory by changing the ownership:
sudo chown postgres:postgres database_backup

sudo -u postgres pg_basebackup -D /path/to/database_backup

echo "Physical Backup Done!"

}

configuring_continuous_archiving
physical_backup

echo "Backup Complete!"


