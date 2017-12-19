# flask_part
flask part of testdriven.io TDD course

React part with Semantic-UI-React see
https://github.com/vpplatonov/React_part

#on ubuntu 16.04

sudo -i -u postgres
[postgres#] \i /var/www/html/.../project/db/create.sql
[postgres=#] \db
[postgres=#] \q
[postgres@ncp-test:~$] exit

apt search virtualenv

sudo apt install virtualenv
dpkg -L virtualenv
virtualenv --help

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

export APP_SETTINGS=project.config.DevelopmentConfig
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/users_dev
export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/users_test
export CRM_API_ROOT=http://crmapi.qa.smtp.com/v1/
export SECRET_KEY=...
export CRM_API_SECRET=...

sudo virtualenv --system-site-packages --python=python3 .venv
source .venv/bin/activate

[valeri.platonov@ncp-test:/var/www/html/portal_flask/venv$] python3 -V
Python 3.6.3

python3 manage.py test

`production env`
export REACT_APP_USERS_SERVICE_URL=http://ncp-test.smtp.com/api
python3 manage.py runserver -p 4000
