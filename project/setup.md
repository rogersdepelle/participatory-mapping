## Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04

### Basic packages
```
sudo apt-get update && sudo apt-get -y upgrade
apt-get install htop python3-pip python3-dev python3-pip libpq-dev nginx binutils libproj-dev gdal-bin postgresql postgresql-contrib postgresql-10-postgis-2.4 postgresql-10-postgis-2.4-scripts postgresql-10-postgis-scripts
```

### PostgreSQL
```
sudo -u postgres psql
CREATE DATABASE pmapping;
CREATE USER pmapping SUPERUSER;
ALTER USER pmapping PASSWORD '@pmapping#';
ALTER ROLE pmapping SET client_encoding TO 'utf8';
ALTER ROLE pmapping SET default_transaction_isolation TO 'read committed';
ALTER ROLE pmapping SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pmapping TO pmapping;
\q
```

### SSH
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```

### Clone Repository
```
mkdir /webapps
cd /webapps
git clone git@github.com:rogersdepelle/participatory-mapping.git
mv participatory-mapping pmapping
cd pmapping
git fetch
git checkout prod
```

### Virtualenv
```
pip install virtualenvwrapper
pip install --upgrade pip
mkvirtualenv -a /webapps/pmapping --no-site-packages pmapping
```

### Bashrc
Local: *~/bashrc*
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh
```

### Setup and Test Aplication
```
pip install -r project/requirements.txt
./manage.py makemigrations
./manage.py migrate
ufw allow 8000
./manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 project.wsgi:application
deactivate
ufw delete allow 8000
```

### User
```
groupadd --system webapps
useradd --system --gid webapps --home /webapps/pmapping/ pmapping
chown -R pmapping:users /webapps/pmapping/
```

### Gunicorn
Local: */etc/systemd/system/gunicorn_pmapping.service*
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=pmapping
Group=www-data
WorkingDirectory=/webapps/pmapping
ExecStart=/webapps/pmapping/venv/bin/gunicorn --workers 3 --bind unix:/webapps/pmapping/project/pmapping.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```
**Start**
```
systemctl daemon-reload
systemctl start gunicorn_pmapping
systemctl enable gunicorn_pmapping
systemctl status gunicorn_pmapping.service
```

### Nginx
Local: */etc/nginx/sites-available/pmapping*
Change server_name for test
```
server {
    listen 80;
    server_name www.mapacomunitario.ga mapacomunitario.ga;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /webapps/pmapping/project;
    }
    location /media/ {
        root /webapps/pmapping/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/webapps/pmapping/project/pmapping.sock;
    }
}

```
**Start**
```
ln -s /etc/nginx/sites-available/pmapping /etc/nginx/sites-enabled
nginx -t
systemctl restart nginx
ufw allow 'Nginx Full'
```

```
systemctl restart gunicorn_pmapping
systemctl restart nginx
```
