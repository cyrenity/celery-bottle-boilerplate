FROM python:2.7

#Setup any proxy parameters if you are behind a corporate proxy 
ENV http_proxy http://10.10.150.150:8118 
ENV https_proxy http://10.10.150.150:8118

WORKDIR /app

RUN apt-get update && apt-get install -y nginx locales

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Setup Supervisord 
RUN mkdir -p /var/log/supervisor /etc/supervisor/conf.d 
COPY extras/docker/supervisord.conf /etc/supervisord.conf 

# Setup smsgwapp 
COPY extras/docker/*_start.sh /app/scripts/ 

RUN chmod +x /app/scripts/*_start.sh 

COPY extras/docker/nginx.conf /etc/nginx/sites-available/default

ENV http_proxy '' 
ENV https_proxy '' 

#Update rabbitmq server address 
RUN sed -i s/localhost/rabbitmq/ tasks.py

RUN locale-gen en_US.UTF-8 
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8' 

# Run app.py when the container launches 
CMD ["supervisord"]
