python3 makeconf.py > /shanghaitechSIST/shanghaitech_SIST/CONFIG.py

# python3 manage.py createcachetable
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

nohup gunicorn shanghaitechSIST.wsgi:application -b 127.0.0.1:8080 --workers 4 --worker-connections 65535&
service nginx start

while true
do
    sleep 1
done
