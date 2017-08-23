Intall tree
install vim
Addgroup marketing 
		rh
		diretoria



////criando os diretorios para compartilhamento
mkdir  -p  /EMPRESA/{marketing/geral,rh/geral,diretoria/geral}
cd  /EMPRESA
chmod  770 -R  *
chgrp marketing  -R  marketing
chgrp  rh  -R  rh
chgrp  diretoria  -R  diretoria		

para verificar use:
ls -l   ou   ls -lR


dentro de etc/samba  ls -l, vamos renomear o arquivo smb.conf para não perder o original
mv smb.conf  orig_smb.conf 
vim  smb.conf

[global]

	server string      = Nome do computador
	netbios name     = nome do computador
	workgroup         = sala010
	security             = share ou user

[Lixeira]
	comment        = lixeira da rede
	path                = /EMPRESA/lixeira   //criar diretorio. Chmod 1777 /EMPRESA/lixeira
	read only        = no
	creat mask     = 0600
	directory mask = 1700
	force create mode      = 0600

[Marketing]
	comment       = arquivis do marketing
	path               = /EMPRESA/marketing
	public            = yes
	
//alterações feitas para mudar permições no compartilhamento.
	; writeable         = yes
	read only           = no
	create mask       = 0660
	directory mask  = 0770
	force group        = marketing
	## contole de conteúdo 
	veto files            =  /*.mp3/*.avi/*.bmp/*.wav/*.zip 
## Lixeira do compartilhamento
	vfs object                 = recycle
	recycle:keeptree      = yes
	recycle:version        = yes
	recycle:repository      = /EMPRESA/liexeira/%U
	recycle:exclude         = *.bak, *.iso, *.obj
	recycle:exclude_dir      = tmp, cache

salva e pronto

////Restartando
service samba restart

////criando os usuarios
useradd  --no--create-home  -s  /bin/false  maria
useradd  --no--create-home  -s  /bin/false  teresa
useradd  --no--create-home  -s  /bin/false  ivan

////cadastrando os usuários no samba

smbpasswd  -a  maria

smbpasswd  -a  teresa

smbpasswd  -a  ivan

////adicionando usuários ao grupo
adduser  maria  marketing
adduser  teresa  rh
adduser  ivan  diretoria


//apagando vários arquivos de uma só vez
//find /EMPRESA/  -name '*.jpg'  -exec rm {} \: