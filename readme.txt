25/january/2014
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
------------------------------------------------------------------------------------------------------------------------------------
For running server on HTTPS (required for speech recognition)
//Setup stunnel
//Run the following commands on terminal

sudo aptitude install stunnel
sudo su -
cd /etc
mkdir stunnel
cd stunnel
openssl req -new -x509 -days 365 -nodes -out stunnel.pem -keyout stunnel.pem
openssl gendh 2048 >> stunnel.pem
chmod 600 stunnel.pem
logout
cd

//Now create a file called dev_https with the following text:

pid=
foreground=yes
debug = 7

[https]
accept=8443
connect=8000
TIMEOUTclose=1
cert = /etc/stunnel/stunnel.pem

//Note: this assumes your web server is running on port 8000. If it’s not, change the value of “connect” to the appropriate port.

//Finally, run:

sudo stunnel4 dev_https
HTTPS=on ./manage.py runserver 0.0.0.0:8000

//In browser type https://0.0.0.0:8443/questionnaire/ to run .
----------------------------------------------------------------------------------------------------------------------------------------

For setting up django user registration
//Download registration templates at location /talktome/templates using the following command
wget https://bitbucket.org/devdoodles/registration_templates/get/3fa26711b938.zip

//Add csrf token to each form in each template using {% csrf_token %}

//Add the following url for the registration templates in urls.py

(r'^$', direct_to_template, 
            { 'template': 'index.html' }, 'index'), 

//Make the following changes  to settings.py file

ACCOUNT_ACTIVATION_DAYS = 2
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
LOGIN_REDIRECT_URL = '/'

Add  'registration' to INSTALLED_APPS 

----------------------------------------------------------------------------------------------------------------------------------------

