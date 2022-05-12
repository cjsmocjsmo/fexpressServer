#!/bin/sh
cd /home/teresa/fexpressServer;

python3 -m venv /home/teresa/fexpressServer/fexpress;

mv /home/teresa/fexpressServer/fexpressServer.py /home/teresa/fexpressServer/fexpress/fexpressServer.py;
mv /home/teresa/fexpressServer/util.py /home/teresa/fexpressServer/fexpress/util.py;

cd /home/teresa/fexpressServer/fexpress;
sudo apt-get update && \
sudo apt-get install --no-install-recommends -y \
	build-essential \
	python3-dev \
    python3-setuptools \
	python3-tornado;
echo "Compoete";

python3 /home/teresa/fexpressServer/fexpress/fexpressServer.py;
