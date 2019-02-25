#!/bin/bash
sudo apt install python-pip
cd /app
pip install -r requirements.txt
obs
python videoPlayer.py
python videoPlaylist.py
