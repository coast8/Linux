




[global]
            ;;; Diretivas do Servidor de dominio
	server string      =  Servidor PDC Samba 20
	netbios name     =  debvbox
	workgroup         = DOMINIO
	wins support         = yes
            
           ;;; Diretivas de segurança
	security                          =  user
	ancrypted passwords     =  yes
	passwd backend            = tdbsam
	wins support                  = yes
	obey pam restrictions     = yes
'	pam password change    = yes
	unix password sync       = yes
	; interfaces                     = eth0 192.168.10.0/24
	
	;;; Gerenciamento de usuarios e computadores
	add user scrit = /usr/sbin/adduser - -quiet - -disabled-passwdord - -gecos “ “ %u
	delete user script            = /usr/sbin/userdel -r %u
	addgroup script              = /usr/sbin/addgroup - -force-badname %g

[Lixeira]
	comment        = lixeira da rede
	path                = /EMPRESA/lixeira   //criar diretorio. Chmod 1777 /EMPRESA/lixeira
	read only        = no
	creat mask     = 0600
	directory mask = 1700
	force create mode      = 0600





























//procurando comando. Prorar parâmetros.
cat /etc/samba/smb.conf | grep *Enter





//pesquisar 
samba

nano /etc/hosts

testparm  smb.conf

DNS:





http://www.vivaolinux.com.br/