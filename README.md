# flask_part
React part with Semantic-UI-React see
https://github.com/vpplatonov/React_part

#on ubuntu 16.04

sudo -i -u postgres
[postgres#] \i /var/www/html/.../project/db/create.sql
[postgres=#] \db
[postgres=#] \q
[postgres@ncp-test:~$] exit

python3 manage.py recreate_db
python3 manage.py seed_db


apt search virtualenv

sudo apt install virtualenv
dpkg -L virtualenv
virtualenv --help

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

export APP_SETTINGS=project.config.DevelopmentConfig
export DATABASE_URL=mysql+pymysql://palms:palms@localhost:3306/palms_dev
export DATABASE_TEST_URL=mysql+pymysql://palms:palms@localhost:3306/palms_test
export SECRET_KEY=!paL@ms1

sudo virtualenv --system-site-packages --python=python3 .venv
source .venv/bin/activate

[valeri.platonov@ncp-test:/var/www/html/portal_flask/venv$] python3 -V
Python 3.6.3

python3 manage.py test

`production env`
export REACT_APP_USERS_SERVICE_URL=http://ncp-test.smtp.com/api
python3 manage.py runserver -p 4000
