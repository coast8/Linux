
#####################################################################################
#                                                                                   #
#                  TRABALHANDO COM REDES                                            #
#                                                                                   #
#####################################################################################


# local onde sao configuradas as interfaces de rede. 
nano etc/network/interfaces

	# configura ip automaticamente.
	auto eth0
	iface eth0 inet dhcp

	# configura ip manualmente.
	auto eth1
	iface eth1 inet static
	address 192.168.0.1 
	netmask 255.255.255.0
	network 192.168.0.0
	broadcast 192.168.0.255


#para ativar a placa de rede que foi configurada.
ifup eth0
ifup eth1

# para testar se pegou as configurações de rede e verificar o IP.
ifconfig 

ifconfig eth0 #interface 0
ifconfig eth1 #interface 1




####################################
# comandos para as estações widows #
####################################

#ip a pipa, quando nao existe gateway
169.254.138.161

# configurando o ip
REDE_INTERNET/CENTRAL_REDE_COMPLARTILHAMENTO/ADAPTADOR/CONEXAO->propiedades/protocolo_TCP_IP4.