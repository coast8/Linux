## [grupo e permissões]
adduser paulo	   	#adiciona o usuário pedro
	
	## Em seguida pedira senha
	## confirmação de senha
	## As outras informações podem ser deixadas em branco
	## Obs.: todos os usuários criados estão dentro da pasta /home.


addgroup nome_do_grupo            #adicionando grupo
gpasswd -a paulo nome-do_grupo    #adicionando usuário ao grupo
gpasswd -d paulo nome-do_grupo    #removendo usuário do grupo


cat /etc/group   		=verificando grupos
cat /etc/passwd			=visualiza os usuários do sistema
cat /etc/shadow    		=visualizar senhas do usuários

	
## criando usuários dentro de grupos
adduser - -ingroup grupo novo_usuario
	

##  comando para que os usuários sejam criados com as pastas já gravadas.
mkdir /etc/skel/{Downloads,Documentos,Musicas,Vídeos}


##  para criação de pastas em série ex:
mkdir {pasta1,pasta2,pasta3,pasta4}


##  deletando usuarios.
userdel -r  	=apaga tudo
userdel     	=deleta o usuário mais suas pasta continuam 
	
##  deletando grupos
groupdel  =apagando grupos


su – usuario    	//já entra direto em outro usuário.
passwd           	//comando para altera a senha.

who               	//mostra quais são os usuários que estão usando o sistema no exato momento.
Users             	// ------------------//   ---//////////////--------­
finger             	// ----------//------- /// --------- mostra também horas 
whoami         		//------------//---------//      mostra qual usuario você estar ligado
id                  // mostra statos dos usuários como qual grupo ele pertence e permissões 
chfn            	//mudar os dados do comando finger
hostname   			//mostra o nome do computor


