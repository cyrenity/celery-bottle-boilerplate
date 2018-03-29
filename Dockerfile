FROM python:2.7

WORKDIR /app

RUN apt-get update && apt-get install -y nginx locales

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Setup Supervisord
RUN mkdir -p /var/log/supervisor
COPY extras/docker/supervisord.conf /etc/supervisord.conf

# Setup smsgwapp
COPY extras/docker/*_start.sh /scripts/

RUN chmod +x /scripts/*_start.sh

COPY extras/docker/nginx.conf /etc/nginx/sites-available/default

#Update rabbitmq server address
RUN sed -i s/localhost/rabbitmq/ tasks.py

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# Run app.py when the container launches
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
