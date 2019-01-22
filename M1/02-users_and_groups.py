
##############################
#                            #
#          USER              #
#                            #
##############################

## USER ADD
	adduser $_new_user		=criar atributos de forma automatica.
	useradd $_new_user		=criar atributos de forma manual.   	


## USER LIST
	getent passwd | cut -d \: -f1
	cat /etc/passwd         =visualizar todos os usuarios
	cat /etc/shadow    		=visualizar senhas do usuários


## USER UPDATE
	chage		=informacoes de expiracao
	passwd		=password
	usermod		=altera caracteristicas


## USER DELETE
	userdel -r  	=apaga tudo
	userdel     	=deleta o usuário mais suas pasta continuam 


## USER	deactivating
## comentar linha que contem o nome do usuario
	/etc/passwd


##############################
#                            #
#          GROUP             #
#                            #
##############################

## GROUP ADD
	addgroup $_group 				=adiciona grupo


## GROUP LIST
	cat /etc/group 					=lista todos os grupos.


## GROUP UPDATE
	gpasswd			=password
	groupmod		=altera caracteristicas


## GROUP DELETE
	groupdel -r


##############################
#                            #
#      USERS IN GROUP        #
#                            #
##############################

## ADD
	gpasswd -a paulo nome-do_grupo    		=add user in grupo
	adduser - -ingroup grupo novo_usuario   =create user in group.


## LIST
	groups $_namoe_user				=mostra os grupos de um user.
	cat /etc/group | grep root 		=mostra os usuarios do grupo root.	


## DELETE
	gpasswd -d paulo nome-do_grupo    	=removendo usuário do grupo


##############################
#                            #
#      DIRETORIOS            #
#                            #
##############################

##  comando para que os usuários sejam criados com as pastas já gravadas.
	mkdir /etc/skel/{Downloads,Documentos,Musicas,Vídeos}

##  para criação de pastas em série ex:
	mkdir {pasta1,pasta2,pasta3,pasta4}


##############################
#                            #
#      EXTRAS                #
#                            #
##############################

su – usuario    	=já entra direto em outro usuário.
who               	=mostra quais são os usuários que estão usando o sistema no exato momento.
Users             	= ------------------//   ---//////////////--------­
finger             	= ----------//------- /// --------- mostra também horas 
whoami         		=------------//---------//      mostra qual usuario você estar ligado
id                  = mostra statos dos usuários como qual grupo ele pertence e permissões 
chfn            	=mudar os dados do comando finger
hostname   			=mostra o nome do computor
w 					=usuarios conectados ao sistema.

#################################
#                               #
#   user with root privileges   #
#                               #
#################################

## EX1
## __________________


## file users sudoers
	sudo adduser novo_usuario


## Adicionando o nome do usuário e as mesmas permissões como root sob a especificação de privilégios 
## do usuário irá conceder-lhes os privilégios sudo.
	sudo /usr/sbin/visudo
		## User privilege specification
		root            ALL=(ALL:ALL) ALL 
		novo_usuario    ALL=(ALL:ALL) ALL


## EX2
## __________________
	adduser sammy					
	usermod -aG sudo sammy
	su - sammy
	exit


#################################
#                               #
#      WebServe Apache          #
#                               #
#################################

## Script para descobrir o user_web_server
## user_web_server.php
	<?php
	# user do web_server
	echo shell_exec("whoami");


## Conf VirtualHosts em WebServe
	sudo chown user_linux:user_web_server /var/www/html -R
	sudo chmod 775 /var/www/html -R


## Conf em Distros Debian
	sudo chown ubuntu:www-data /var/www/html -R
	sudo chmod 775 /var/www/html -R