#Talktome

<pre><code><b>Install Requirements </b>
	pip install -r requirements.txt


<b>For running server on HTTPS (required for speech recognition)</b>
<i>Run the following commands on terminal</i>
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
	sudo stunnel4 dev_https
	HTTPS=on ./manage.py runserver 0.0.0.0:8000

In browser type https://0.0.0.0:8443/questionnaire/

</pre></code>
