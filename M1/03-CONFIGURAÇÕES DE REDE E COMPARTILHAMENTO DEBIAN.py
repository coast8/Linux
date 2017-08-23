LINUX DEBIAN


	## Passo a passo configuração das interfaces de rede
ifconfig -a   =verificando as interfaces de rede

 	## diretório de configurações de interfaces de redes
cd /etc/network 

	## responsável pelas configurações de interfaces de redes
nano   interfaces 
       


#####################################################################################
#                                                                                   #
#                  ARQUIVO CONFIGURADO EM SENAC -PI                                 #
#                                                                                   #
#####################################################################################

	## arquivo de configuração.
auto eth1                          //essa é a interface de conexão com a internet
iface eth1 inet static
address 192.168.1.155
netmask 255.255.255.0
gateway 192.168.1.1            //endereço IP de conexão com a internet.
nameserve 192.168.1.1       //servidor de DNS.





	## configuração da segunda interface de rede.
auto eth2                        //interface de conexão com a rede local
iface eth2 inet static
addres 192.168.50.50         //interface de rede de devera ficar ligada ao suite    
netmask 255.255.255.0      //as makinas da rede loca

	## salvo arquivo
	## sair

	#reiniciar os serviços sem ´reiniciar reiniciar os pc.
invoke-rc.d networking restart  

	#após as configurações, as interfaces de redes devem ser reiniciadas.
/etc/init.d/networking restart

	#se falha devemos verificar o que deu errado.
nano interfaces

	## fim





#####################################################################################
#                                                                                   #
#                  ARQUIVO CONFIGURADO EM AULAEAD - PROF. JOSE DE ASSIS             #
#                                                                                   #
#####################################################################################

#the loopback networking interface
auto lo
iface la inet loopback

#interface de internet com ip dinâmico
auto eth0
iface eth0 inet dhcp


#interface de rede local com ip manual
auto eth1
iface eth1 inet static
address 192.168.0.1
netmask 255.255.255.0
network 192.168.0.0
broadcast 192.168.0.255



# comando para subir  
ifup eth0



======================================================================================================

======================================================================================================
======================================================================================================


======================================================================================================

Obs.:
auto eth1
iface eth1 inet dhcp    ##configura os ips automaticamente, dispensando as linhas abaixo.
Ifconfig -a   			##verificando como ficaram as interfaces de rede depois das configurações.

	## CRIAR O ROTEMAENTO E COMPARTILHAMENTO COM A INTERNET  ATRAVES DA INTERFACE DE COMUNICAÇÃO COM O MODEM.
cd /etc
nano rc.local

	## navegar até ficar exatamente acima da linha exit 0.

echo 1 > /proc/sys/net/ipv4/ip_forward    # valor1 ativa o reteamento
iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE

	## SALVA O ARQUIVO E SAIR 
/etc/rc.local


	## agora é configurar a interface de rede das outras maquinas, usar a placa eth2
ip 192.168.50.60
máscara de rede 255.255.255.0
gateway 192.168.50.50
DNS 8.8.8.8   //DNS do google.

	## confirmar e já estará pingando nas maquinas
