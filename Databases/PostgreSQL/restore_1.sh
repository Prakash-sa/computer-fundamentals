#!/bin/bash
 


pitr(){

echo "Point in time Recovery..."

sudo -u postgres psql -c "SHOW data_directory;"


}

pitr

echo "Done!"
