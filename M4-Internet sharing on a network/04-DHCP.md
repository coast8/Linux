#####################################################################################
#                                                                                   #
#                  INSTALNDO O SERVIÇO DE DHCP                                      #
#                                                                                   #
#####################################################################################


# procedimento a ser feito é atualização de pacotes
# instalaçao do DHCP, e apos a instalação deve observar os itens abaixo 
# arquivo chave de configuração deve ser configurado
# para que que o serviço possa funcionar, /etc/default/isc-dhcp-server
# e o dhcpd.conf tbm deve ser configurado apos isso o serviço esta habilitado.

apt-get update

# pacote de instalação do DHCP
	apt-get install isc-dhcp-server 


# configurar o dhcp, 2 configurações deve ser feitas

	
	###############################
	#    CONFIGURAÇÕES DE DHCP    #
	###############################

	# o arquivo chave vai pedir a interface que vai distribuir os ips. 
	# interface reponsavel por dispara os ip na rede.
		/etc/default/isc-dhcp-server
			INTERFACES="eth1"


	# arquivo principal do dhcp tem a função de conf o range de IPs. 
	# obs, é bom sempre fazer backup dos arquivos originais.
	# abixo modelo de scripts de dhcpd.conf 
		/etc/dhcp/dhcpd.conf

		## ****************** // **********************************
		
		# dhcpd.conf -- https://www.vivaolinux.com.br/etc/dhcpdconf/
		#
		# Configuration file for ISC dhcpd (see 'man dhcpd.conf')
		#
		authoritative;
		#Domínio configurado no BIND
		#option domain-name "seudominio.com.br";
		default-lease-time 600; #controla o tempo de renovação do IP
		max-lease-time 7200; #determina o tempo que cada máquina pode usar um determinado IP. 

		subnet 192.168.1.0 netmask 255.255.255.0 { #Define sua "sub-rede" 192.168.1.0 com a máscara 255.255.255.0 
		     range 192.168.1.101 192.168.1.200;  #faixa de IPs que o cliente pode usar.
		     option routers 192.168.1.100; #Este é o gateway padrão (neste caso).
		     option broadcast-address 192.168.1.255; #Essa linha é o endereço de broadcast (neste caso).

		#Aqui você coloca os servidores DNS de terceiros ou seu DNS próprio configurado no BIND. Nesse caso coloquei o DNS do Google.
		     option domain-name-servers 8.8.8.8; 
		     option domain-name-servers  8.8.4.4;
		}
		## ****************** // **********************************
		
		

		## ****************** // **********************************

		# dhcpd.conf -- A Smythy C Costa.
		# permite alterações dinamicas de dns
		ddns-update-style none;
		#define o servidor dns a ser entrege aos host
		option domain-name-servers 192.168.0.1;
		#determinam o tempo de vida do IP
		default-lease-time 600;
		max-lease-time 7200;
		#se este nao for o principal dhcp
		authoritative;
		#crias os logs
		log-facility loca17;
		#escopo
		subnet 192.168.0.0 netmask 255.255.255.0{
		range 192.168.0.50 192.168.0.200;
		option routers 192.168.0.1;
		}

		## ****************** // **********************************
		




	#comando para reiniciar os serviços
		service isc-dhcp-server restart

	#arquivo que contem a listem usuarios de dhcp
		cat /var/lib/dhcp/dhcpd.leases






		
		###############################
		#COMANDOS DAS ESTAÇÕES WIDOWS.#
		###############################

		#limpa as conf de IP
		ipconfig /release

		#força a reinilializaçao do ip
		ipconfig /renew

		#verificação detalhada sobre as configurações de IP
		ipconfig /all


		##obs a-pipa, quando nao encontra IP o widows obtem este 169.254.138.161.




# statos do servidor dhcp
service isc-dhcp-server status