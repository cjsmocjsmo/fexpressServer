python3 -m venv /home/teresa/fexpressServer;
cd /home/teresa/fexpressServer;
sudo apt-get update && \
sudo apt-get dist-upgrade -y && \
sudo apt-get autoclean -y && \
sudo apt-get autoremove -y && \
sudo apt-get install --no-install-recommends -y \
	build-essential \
	python3-dev \
    python3-setuptools \
	python3-tornado;
git clone https://github.com/cjsmocjsmo/fexpress;
python3 /home/teresa/fexpressServer/fexpress/fexpressServer.py
