

#######################################################
#  Regras de iptables para compartilhar a internet    #
#######################################################

/etc/init.d/firewall

## as regras para compartilhamento de internet devem 
## estar abaixo das linhas aqui citadas.

	## Elimina pacotes inválidos (evita diversos tipos de ataques)
	iptables -A INPUT -m state –state INVALID -j DROP




# Carregando o módulo correspondente
modprobe iptable_nat
# Regra
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
# Ativando o módulo ip_forward
echo 1 > /proc/sys/net/ipv4/ip_forward
#fim do complartilhamento da internet





#observações importantes:
-t nat –> utiliza o tabela de tradução de ips
-A POSTROUNTIG –> adiciona a regra para saída (eth1 no caso)
-o eth0 –> interface WAN
-j MASQUERADE –> mascaramento dos pacote

