
# instalar, configurar e proteger um servidor FTP (VSFTPD em completo “Very Secure FTP Daemon“) no 
# Ubuntu para ter uma poderosa segurança contra vulnerabilidades no FTP


# O FTP é um protocolo de rede padrão relativamente antigo e mais usado usado 
# para fazer o upload ou download de arquivos entre dois computadores em uma rede. 
# No entanto, o FTP por ser naturalmente inseguro, pois ele transmite dados juntamente 
# com credenciais de usuário (nome de usuário e senha) sem criptografia.


## Se você planeja usar FTP, considere a possibilidade de configurar a conexão 
## com SSL/TLS. Caso contrário, é sempre melhor usar FTP seguro, como SFTP.



# atualizar a lista de fontes do pacotes do sistema  e 
# instalar o pacote binário VSFTPD.
	sudo apt-get update
	sudo apt-get install vsftpd

# iniciá-lo manualmente
	systemctl start vsftpd

# ativá-lo para iniciar automaticamente a partir do próximo boot do sistema.
	systemctl enable vsftpd



# Existem mais configurações de segurança a serem realizadas.
# as conf estão no linkin.
# FONTES:
	https://sempreupdate.com.br/como-instalar-um-servidor-ftp-ubuntu/

