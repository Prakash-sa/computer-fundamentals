#!/bin/bash
 


physical_backup(){

echo "Point in time Recovery..."

sudo -u postgres psql -c "SHOW data_directory;"


}


physical_backup

echo "Done!"
