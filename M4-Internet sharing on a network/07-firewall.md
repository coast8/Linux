# vamos criar uma linha de defesa para um cliente de pequeno porte que usa a internet, 
# um cliente de email e também acessa o servidor linux via ssh.



#  Identificar o tipo de protocolo e as portas usadas pelos serviços


# Portas HTTP e HTTPS (normalmente 80 e 443)
	cat /etc/services | grep www


#Portas referente ao serviço de email (confirmar com o provedor)

Recebimento de email
POP3: (110 e 995)
IMAP: (143 e 993)
Envio de email
SMTP: (25, 26, 465 e 587)

Porta referente ao DNS (normalmente a 53)
	netstat -antp | grep 53

Porta referente ao SSH (normalmente a 22)
	netstat -antp | grep 22






#########################################
#        Montagem do script             #
#########################################

/etc/init.d/firewall

#***************************************** // *********************************

#!/bin/sh
# para que ninguem pinge no servidor
iptables -A INPUT -p ICMP -j DROP
# Defesa: syncookies (evita ataques de DoS “Negação de serviços”)
echo 1 > /proc/sys/net/ipv4/tcp_syncookies
#Defesa: rpfilter (evita ataque de spoofing “falsificação de ip”)
echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter
# Elimina pacotes inválidos (evita diversos tipos de ataques)
iptables -A INPUT -m state –state INVALID -j DROP
# Carregando o módulo correspondente
modprobe iptable_nat
# Regra
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
# Ativando o módulo ip_forward
echo 1 > /proc/sys/net/ipv4/ip_forward
#fim do complartilhamento da internet
# Liberando acesso a interface de loopback:
iptables -A INPUT -p tcp -i lo -j ACCEPT
# Liberando DNS:
iptables -A INPUT -p tcp –dport 53 -j ACCEPT
iptables -A INPUT -p udp –dport 53 -j ACCEPT
#Regra de iptables para liberar a porta 3128:
iptables -A INPUT -p tcp –dport 3128 -j ACCEPT
# Liberando HTTP e HTTPS:
iptables -A INPUT -p tcp –dport 80 -j ACCEPT
iptables -A INPUT -p tcp –dport 443 -j ACCEPT
# Libera envio e recebimento de email. Obs Verificar portas junto ao provedor
iptables -A INPUT -p tcp –dport 110 -j ACCEPT
iptables -A INPUT -p tcp –dport 25 -j ACCEPT
# Liberando o acesso remoto via SSH:
iptables -A INPUT -p tcp –dport 22 -j ACCEPT
# Bloqueia as portas UDP de 0 a 1023 (com exceção das abertas acima):
iptables -A INPUT -p udp –dport 0:1023 -j DROP
# Bloqueia conexões nas demais portas:
iptables -A INPUT -p tcp –syn -j DROP

#***************************************** // *********************************


# renicia o servidor
	reboot


# Acrescente a linha abaixo no início do script para evitar que a rede seja “scaneada”
# Protecao contra port scanners ocultos
iptables -A INPUT -p tcp –tcp-flags SYN,ACK,FIN,RST RST -m limit –limit 1/s -j ACCEPT