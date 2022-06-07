FROM python:3.9-slim-buster
WORKDIR /var

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY health-checker /var/health-checker
COPY entrypoint.sh /var/entrypoint.sh
COPY health.sh /var/health.sh
RUN chmod 777 /var/health-checker /var/entrypoint.sh /var/health.sh
RUN chmod +x /var/health-checker /var/entrypoint.sh /var/health.sh

RUN useradd -ms /bin/bash icon
USER icon

ENTRYPOINT ["/var/entrypoint.sh"]