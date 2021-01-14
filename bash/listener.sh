#!/bin/bash
### BEGIN INIT INFO
# Provides:             Notify inbound folder event service
# Short-Description:    Script part of single RPA
# Author:          		Sandro Regis Cardoso | Software Eng.
### END INIT INFO


actions=CREATE,MOVED_TO,DELETE,ACCESS

parent_dir="$(dirname "$(pwd)")"
bash_log_dir=$parent_dir/log/bash
current_dir=${PWD##*/}
dir_datasource=$parent_dir/datasource
dir_inbound=$parent_dir/inbound
inotify=/usr/bin/inotifywait
log_file=$bash_log_dir/datasource_notify.log

know_extensions=("csv" "xml" "xls" "xlsx")


set -e

if ! [[ -e $bash_log_dir ]]
	then
		mkdir -p $bash_log_dir;
fi

if ! [[ -e $log_file ]]
	then
		touch $log_file
fi

gen_unique_key() {
	sleep 1s
	unique_key=$( date +%Y%m%d%H%M%S%s )
	echo $unique_key
}

get_client_ip() {
	client_ip=$( netstat -putan | awk '/:22 / && / ESTABELECIDA / {split($4, result, ":"); print result[1]}' ) 
	echo $client_ip
}

get_auth_user() {
	client_auth_user=$( netstat -putan | awk '/:22 / && / ESTABELECIDA / {split($8,result,":"); print result[1]}' )
	echo $client_auth_user
}

rename_inbound_file() {
	filename=$1
	ukey=$( gen_unique_key );
	new_file_name=$ukey"_"$file_name
	echo $new_file_name
}

inbound_monitor() {
	while $inotify --recursive --event $actions "$dir_inbound"
		do
			sleep 0.7
			#($client_ip, $client_auth_user) will be used on json rest data header
			client_ip=$( get_client_ip );
			echo $client_ip;
			client_auth_user=$( get_auth_user );
			echo $client_auth_user;
			
			FILES=$(ls $dir_inbound)
			
			for file_name in $FILES
				do
				  	file_extension=${file_name##*.}
					
					case "${know_extensions[@]}" in 
						*"$file_extension"* )
							#change font color for dev proposal only
							tput setaf 2;
							echo "Action : Move $file_extension file to parser dir.";
							newfile_name=$( rename_inbound_file $file_name );
							
							#@todo: create bash function to move files
							mv $dir_inbound"/"$file_name $dir_datasource"/"$file_extension"/"$newfile_name;
							#reset font color
							tput sgr 0;;
						* )
							#change font color for dev proposal only
							tput setaf 1;
							echo "Action : Send push and mail notification: Extension $file_extension not supported.";
							newfile_name=$( rename_inbound_file $file_name );
							mv $dir_inbound"/"$file_name $dir_inbound"/.not_supported/"$newfile_name;
							#reset font color
							tput sgr 0;;
			  		esac
				done
		done
}


datasource_monitor() {
	while $inotify --recursive --event $actions "$dir_datasource"
		do
			sleep 0.7
			echo "Action : Run parser to added $new_file_name..."
			#set PYTHONPATH for test proposal
			#export PYTHONPATH="$PYTHONPATH:/opt/projetos/Django/logger_framework/:/opt/projetos/Django/logger_framework/logger_multi_modules/:/opt/projetos/Django/rpa_datasources/addons_community/pid-3.0.4"
			#python "../main.py";;
		done
}


inbound_monitor & datasource_monitor & 


