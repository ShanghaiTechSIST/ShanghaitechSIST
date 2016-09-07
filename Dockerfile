FROM django:1.8.6-python3

MAINTAINER eastpiger @ Geek Pie Association

EXPOSE 80

RUN apt-get update && apt-get install nginx libjpeg-dev -y
RUN pip3 install mysqlclient gunicorn django-cms djangocms-text-ckeditor djangocms-picture djangocms-file

RUN mkdir /logs
RUN mkdir /shanghaitechSIST
RUN mkdir /shanghaitechSIST/media
RUN mkdir /shanghaitechSIST/static

WORKDIR /shanghaitechSIST
COPY . /shanghaitechSIST
COPY shanghaitechSIST.conf /etc/nginx/sites-enabled/shanghaitechSIST.conf
RUN chmod +x ./loader.sh

CMD ./loader.sh
