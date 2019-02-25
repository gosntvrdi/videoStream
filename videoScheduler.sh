#!/bin/bash
sudo apt install python-pip
cd /app
pip install -r requirements.txt
python videoPlayer.py &
python videoPlaylist.py
sudo apt-get install wmctrl
sudo apt-get install xdotool
sleep 20
wmctrl -k on
xdg-open http://127.0.0.1:5000
sleep 5
xdotool key F11
