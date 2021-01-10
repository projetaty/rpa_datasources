#!/bin/bash

### BEGIN INIT INFO
# Provides:             Notify inbound folder event service
# Required-Start:       $remote_fs $syslog
# Required-Stop:        $remote_fs $syslog
# Should-Start:         $network
# Should-Stop:          $network
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    Script part of single RPA
# Author:          		Sandro Regis Cardoso | Software Eng.
### END INIT INFO

parent_dir="$(dirname "$(pwd)")"
current_dir=${PWD##*/}
bash_log_dir=$parent_dir/log/bash
log_file=$bash_log_dir/datasource_notify.log
dir_inbound=$parent_dir/inbound
inotify=/usr/bin/inotifywait
actions=CREATE,MOVED_TO,DELETE
xmlfile="xml"

set -e

if ! [[ -e $bash_log_dir ]]
	then
		mkdir -p $bash_log_dir;
fi
if ! [[ -e $log_file ]]
	then
		touch $log_file
fi

#TODO: Test multiples files inbounding
inbound_monitor() {
	while $inotify --recursive --event $actions "$dir_inbound"
		do
			sleep 3
			file_name=$(ls $dir_inbound)
			file_extension=${file_name##*.}
			if [ $file_extension == $xmlfile ]
				then
					echo "Action : Call parser to $file_extension file"
					rm -f $dir_inbound"/"$file_name;
			fi
		done
}

inbound_monitor &



