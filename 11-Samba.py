

### srcip simple do samba

# 
/etc/samba/smb.conf
#------------------------------------------------------

[global]

	netbios name     = Chacal
	server string    = Servidor de arquivos Samba.
	workgroup        = relacoes_publicas

[homes]

	path             = /home/%u
	valid users 	 = %S
	read only 		 = no 
	create mask      = 0700
	directory mask   = 0700
	browseable       = no 

[arquivos]
	
	path 			 = /home/arquivos
	comment 		 = Pasta de arquivos diversos. 
	writable		 = yes  # usuarios tem permicoes.

#-----------------------------------------------------------


#criando a pasta descrita no samba
mkdir arquivos

# dando permições 
chmod -R 777 arquivos

#restarta o samba
/etc/init.d/smbd restart

# criando usuarios no linux
useradd lucassousa
passwd lucassousa

# senha para o samba
smbpasswd -a lucassousa





################################
# monitorando o samba          #
################################
smbstatus # mostra quem esta conectados

watch -n1 smbstatus