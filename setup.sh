#!/bin/sh
cd /home/teresa/fsexpressServer;

python3 -m venv /home/teresa/fsexpressServer/fexpress;

mv /home/teresa/fexpressServer/fexpressServer.py /home/teresa/fexpressServer/fsexpress/fexpressServer.py;
mv /home/teresa/fexpressServer/util.py /home/teresa/fexpressServer/fsexpress/util.py;

cd /home/teresa/fsexpressServer/fexpress;
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
