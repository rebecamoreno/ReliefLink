#!/bin/sh
while IFS='' read -r line || [[ -n "$line" ]]; do
    IFS=' ' read name url <<< "$line"
	echo "Text read from file: $name $url"
	wget --user='unhcr\morenoji' --password='XXXXXXXX' $url -O $name
done < "$1"
