#!/bin/bash
 


pitr(){

echo "Point in time Recovery..."

#if the database is still running, you’ll need to shut it down. You can do this by running the systemctl stop command
sudo service postgresql stop

#Move the pg_wal directory to a different place as this might contain unarchived WAL files that are important for recovery. Use the mv command to move the pg_wal directory as follows:
sudo mv /var/lib/postgresql/12/main/pg_wal ~/

#remove the PostgreSQL’s data directory (/var/lib/postgresql/12/main) entirely and recreate it as such:
sudo rm -rf /var/lib/postgresql/12/main
sudo mkdir /var/lib/postgresql/12/main

#Copy all the files from the physical backup you made in the previous section (9.2) to the new empty data directory.
sudo cp -a /path/to/database_backup/. /var/lib/postgresql/12/main/

#Ensure the data directory has the postgres user as the owner and the appropriate permissions:
sudo chown postgres:postgres /var/lib/postgresql/12/main
sudo chmod 700 /var/lib/postgresql/12/main

#Remove the pg_wal file in the /var/lib/postgresql/12/main directory as follows:
sudo rm -rf /var/lib/postgresql/12/main/pg_wal

#Now copy the files from the pg_wal directory you saved before clearing out the data directory:
sudo cp -a ~/pg_wal /var/lib/postgresql/12/main/pg_wal

#Configure the recovery settings in postgresql.conf file in the /etc/postgresql/12/main/ directory. 
sudo nano /etc/postgresql/12/main/postgresql.conf

restore_command = 'cp /path/to/database_archive/%f %p'
recovery_target_time = '2019-06-04 14:10:00'
recovery_target_action = 'pause'       


#Before restarting the database cluster, you need to inform PostgreSQL that it should start in recovery mode. You can achieve this by creating an empty file in the cluster’s data directory called recovery.signal. To create an empty file in the directory
sudo touch /var/lib/postgresql/12/main/recovery.signal


#Now you can restart the database cluster by running:
sudo service postgresql start

#Check postgres service status with below command: 
sudo systemctl status postgresql@12-main




}

pitr

echo "Done!"
