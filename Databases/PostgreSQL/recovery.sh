
#5. Recovery, Here is the procedure:

#Stop the server, if it's running.

#  If you have the space to do so, copy the whole cluster data directory and any tablespaces to a #temporary location in case you need them later. Note that this precaution will require that you #have enough free space on your system to hold two copies of your existing database. If you do not #have enough space, you should at least save the contents of the cluster's pg_xlog subdirectory, as #it might contain logs which were not archived before the system went down.

#  Remove all existing files and subdirectories under the cluster data directory and under the root #directories of any tablespaces you are using.

#  Restore the database files from your file system backup. Be sure that they are restored with the #right ownership (the database system user, not root!) and with the right permissions. If you are #using tablespaces, you should verify that the symbolic links in pg_tblspc/ were correctly restored.

#  Remove any files present in pg_xlog/; these came from the file system backup and are therefore #probably obsolete rather than current. If you didn't archive pg_xlog/ at all, then recreate it with #proper permissions, being careful to ensure that you re-establish it as a symbolic link if you had #it set up that way before.

# If you have unarchived WAL segment files that you saved in step 2, copy them into pg_xlog/. (It #is best to copy them, not move them, so you still have the unmodified files if a problem occurs and #you have to start over.)

#  Create a recovery command file recovery.conf in the cluster data directory (see Chapter 26). You #might also want to temporarily modify pg_hba.conf to prevent ordinary users from connecting until #you are sure the recovery was successful.

# Start the server. The server will go into recovery mode and proceed to read through the archived #WAL files it needs. Should the recovery be terminated because of an external error, the server can #simply be restarted and it will continue recovery. Upon completion of the recovery process, the #server will rename recovery.conf to recovery.done (to prevent accidentally re-entering recovery #mode later) and then commence normal database operations.

# Inspect the contents of the database to ensure you have recovered to the desired state. If not, #return to step 1. If all is well, allow your users to connect by restoring pg_hba.conf to normal.


#Important thing is that sometime, you need to specify timeline
recovery_target_time = ''  # for example '2013-11-06 10:00:05'
