#!/bin/bash

### BEGIN INIT INFO
# Provides:             Notify inbound folder event service
# Short-Description:    Script part of single RPA
# Author:          		Sandro Regis Cardoso | Software Eng.
### END INIT INFO

parent_dir="$(dirname "$(pwd)")"
current_dir=${PWD##*/}
bash_log_dir=$parent_dir/log/bash
log_file=$bash_log_dir/datasource_notify.log
dir_inbound=$parent_dir/inbound
inotify=/usr/bin/inotifywait
actions=CREATE,MOVED_TO,DELETE,ACCESS
xmlfile="xml"
xlsfile="xls"
csvfile="csv"
txtfile="txt"

set -e

if ! [[ -e $bash_log_dir ]]
	then
		mkdir -p $bash_log_dir;
fi

if ! [[ -e $log_file ]]
	then
		touch $log_file
fi

inbound_monitor() {
	while $inotify --recursive --event $actions "$dir_inbound"
		do
			sleep 0.7
			FILES=$(ls $dir_inbound)
			for file_name in $FILES
				do
				  	file_extension=${file_name##*.}
					if [ $file_extension == $xmlfile ]
						then
							echo "Action : Call parser to $file_extension file"
							rm -f $dir_inbound"/"$file_name;
					
					elif [ $file_extension == $xlsfile ]
						then
							echo "Action : Call parser to $file_extension file"
							rm -f $dir_inbound"/"$file_name;
					
					elif [ $file_extension == $csvfile ]
						then
							echo "Action : Call parser to $file_extension file"
							rm -f $dir_inbound"/"$file_name;
					
					else
						echo "Action : Send mail file extension $file_extension not supported."
					fi
				done
		done
}

inbound_monitor &



