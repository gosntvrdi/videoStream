#!/bin/bash
sudo apt install python-pip
sudo apt-get install wmctrl
sudo apt-get install xdotool
cd /app
pip install -r requirements.txt
python videoPlayer.py &
python videoPlaylist.py
sleep 3
wmctrl -k on
sleep 10
xdg-open http://127.0.0.1:5000
sleep 5
xdotool key F11
