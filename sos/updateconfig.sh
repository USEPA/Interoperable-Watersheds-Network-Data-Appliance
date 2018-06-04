#!/bin/bash
INPUT=configuration.csv
OLDIFS=$IFS
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read "name" "value"
do
	n="${name%\"}"
	n="${n#\"}"
	name="$n"
	v="${value%\"}"
	v="${v#\"}"
	value="$v"
	if [ "$name" != "name" ]
	then
		if [ "$name" == "service.sosUrl" ] || [ "$name" == "serviceProvider.site" ]
		then
			sqlite3 configuration.db "update uri_settings set value = '$value' where identifier = '$name'"
		else
			sqlite3 configuration.db "update string_settings set value = '$value' where identifier = '$name'"
		fi
	fi
done < $INPUT
IFS=$OLDIFS
