
# instalando ssh
apt-get install openssh-server


# por medidas de segurança nao podemos fazer o acesso 
# como root.


# mais podemos liberar o acesso como root
/etc/ssh/sshd_config
	#comenta a linha
	PermitRootLogin without-passw


# reinicia o serviço
service ssh restart