


###############################
#    instalando o DNS         #
###############################


# o DNS não precisa configurar nada, basta a intalação 
# restart o serviço e verificar se estar funcionando.

#atualizando o repositorio.
apt-get update 

# serviço de DNS.
apt-get install bind9


#restartando o serviço.
service bind9 restart

#status.
service bind9 status