FROM debian:bullseye-slim

RUN \
	apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get autoclean -y && \
	apt-get autoremove -y && \
	apt-get install --no-install-recommends -y \
		build-essential \
		python3-dev \
        python3-setuptools \
		python3-tornado

RUN \
	mkdir /usr/share/fexpress && \
	chmod -R 0755 /usr/share/fexpress

COPY fexpressServer.py /usr/share/fexpress
COPY util.py /usr/share/fexpress

CMD [ "python3", "/usr/share/fexpress/fexpressServer.py" ]
