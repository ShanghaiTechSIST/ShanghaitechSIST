FROM django:1.8.6-python3

MAINTAINER eastpiger @ Geek Pie Association

EXPOSE 80

RUN apt-get update && apt-get install nginx libjpeg-dev -y
RUN pip install --upgrade pip
RUN pip3 install mysqlclient gunicorn django-cms==3.4.1 djangocms-text-ckeditor==3.3.0 djangocms-picture==2.0.2 djangocms-file==2.0.1 easy-thumbnails==2.3 django-filer==1.2.5

RUN mkdir /logs
RUN mkdir /shanghaitechSIST
RUN mkdir /shanghaitechSIST/media
RUN mkdir /shanghaitechSIST/static

WORKDIR /shanghaitechSIST
COPY . /shanghaitechSIST
COPY shanghaitechSIST.conf /etc/nginx/sites-enabled/shanghaitechSIST.conf
RUN chmod +x ./loader.sh

CMD ./loader.sh
