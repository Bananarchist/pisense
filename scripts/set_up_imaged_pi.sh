#!/bin/bash

if [ $# -eq 0 ]; then
	cat <<EOS

ERROR! Please specify an SSID

Example:
$0 SSID [PWK] [path/to/sd/root]

path/to/sd/root if unspecified defaults to /Volumes/boot
EOS
	exit	
fi


ssid=$1
wfpw=${2:-""}
sdcp=${3:-"/Volumes/boot"}

# permits headless
touch "$sdcp/ssh"

# connects to network
cat <<EOT > $sdcp/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
	ssid="${ssid}"
	psk="${wfpw}"
}
EOT
