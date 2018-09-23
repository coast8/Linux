# - upadate system/install software ######################################################

## Comandos que configuram o servidor, atualizados 06.05.2017(PHP7)
	sudo su
	apt-get update
	apt-get dist-upgrade
	apt-get install apache2
	a2enmod rewrite
	service apache2 start
	apt-get install libapache2-mod-php
	/etc/init.d/apache2 restart
	chown ubuntu /var/www/html
	chmod 777 /var/www/html
	apt-get install php-curl
	apt-get install mysql-server
	apt-get install php-mysql
	apt-get install phpmyadmin
	chmod 755 /var/www/html﻿