#!/bin/sh
cd /home/teresa;
git clone https://github.com/cjsmocjsmo/fexpress;
cd /home/teresa/fsexpress

python3 -m venv /home/teresa/fexpress/fexpressServer;
cd /home/teresa/fexpress/fexpressServer;
mv /home/teresa/fexpress/fexpressServer.py /home/teresa/fexpress/fsexpressServer/fexpressServer.py
mv /home/teresa/fexpress/util.py /home/teresa/fexpress/fsexpressServer/util.py

sudo apt-get update && \
sudo apt-get dist-upgrade -y && \
sudo apt-get autoclean -y && \
sudo apt-get autoremove -y && \
sudo apt-get install --no-install-recommends -y \
	build-essential \
	python3-dev \
    python3-setuptools \
	python3-tornado;

python3 /home/teresa/fexpressServer/fexpress/fexpressServer.py;
