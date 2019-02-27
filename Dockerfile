FROM python:3.6-slim

#RUN git clone https://github.com/housong12590/gongfudou_data.git /var/www/app

RUN  mkdir -p /var/www/app && cd /var/www/app
COPY . /var/www/app/
WORKDIR /var/www/app/

# 配置运行环境
RUN pip install -r /var/www/app/requirements.txt
CMD python  /var/www/app/main.py

