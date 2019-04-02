#!/bin/bash
# https://pimylifeup.com/raspberry-pi-wiimote-controllers/
sleep 1 # Wait until Bluetooth services are fully initialized
hcitool dev | grep hci >/dev/null

MAC="00:19:1D:63:93:5C"

if test $? -eq 0 ; then
    wminput -d -c  /home/pi/catbot/mywminput $MAC &
else
    echo "Bluetooth adapter not present!"
    exit 1
fi
