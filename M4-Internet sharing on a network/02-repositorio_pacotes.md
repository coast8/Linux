
nano /etc/apt/sources.list

## modo como o repositorio deve esta configurado

	deb http://security.debian.org/ jessie/updates main

	deb-src http://security.debian.org/ jessie/updates main



	deb http://ftp.debian.org/debian/ jessie-updates main
	deb-src http://ftp.debian.org/debian/ jessie-updates main

	deb http://ftp.br.debian.org/debian/ jessie main
	deb-src http://ftp.br.debian.org/debian/ jessie main






# atualiza 
	apt-get update