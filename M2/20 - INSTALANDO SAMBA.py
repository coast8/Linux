Instalando Servidor Samba
//É sempre bom atualiazar o sistema primeiro

apt-get install update
apt-get install upgrade

apt- get install samba smbclient smbfs

O samba foi instalado dentro do /etc
cd /etc/samba
ls samba

O samba já vem configurado devemos apagar e reconfigurar
nano smb.conf                  //documento configurado
rm     smb.conf                 //apagando o arquivo
touch  smb.conf                //criando novamente o arquivo

O próximo passo é criar duas pastas dentro de home, que devem ser compartilhadas.
Mkdir  fundacao publico

Permissões nas pastas
chmod 777 fundacao
chmod 777 publico

Devemos configurar o script do samba com as pastas que serão compartilhadas
nano  /etc/samba/smb.conf

[global]

	netbios name = Servidor
	server string = Servidor de arquivos no Samba GNU/Linux
	workgroup = Alunos

[fundacao]

	path = /home/fundacao
	comment = pasta de arquivos da fundacao
	writable = yes

[publico]

	path = /home/publico
	comment = pasta de arquivos publico
	writable = yes

salva e pronto

Criar um usuário do servidor para acessar em máquina cliente.

Autenticando senha
Smbpasswd  -a  usuario

