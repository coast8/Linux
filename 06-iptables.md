###############################
#          ip_tables          #
###############################

# ip_tables é a ferramenta para montar o firewall
# firewall é a ferramenta mais importante contra ataques e invasões
# ele cria regras e so deixa passar os pacotes de acordo com essas regras.

Netfilter  —> módulo do kernel Linux com funções de firewall
Iptables   —> linguagem de programação do Netfilter (ferramenta)





#########################################
#               Netfilter               #
#########################################


# O Netfilter trabalha com 3 tabelas:

Tabela Filter (regras e políticas de restrições)
	INPUT, FORWARD e OUTPUT

Tabela Nat (mudanças de endereço “roteamento”)
	OUTPUT, PREROUTING e POSTROUTING

Tabela Mangle (serviços especias Ex: Qos)


Chains —> (cadeia) Listas de regras que podem ser aplicadas nas tabelas
	Ação da regra:
		
		ACCEPT —> O pacote é aceito.
		DROP —> O pacote é descartado sem aviso ao emissor.
		REJECT —> O pacote é descartado com aviso ao emissor.





#########################################
#       Comandos iptables:              #
#########################################

iptables -L —> listar as regras
iptables -F —> Apagar todas as regras (“matar o firewall”)
iptables -I —> Adicionar a regra no início da lista
iptables -i 3 —> Adiciona a regra na posição 3 da lista
iptables -A —> Adicionar a regra no final da lista


INPUT 	–> Trata os pacotes antes de entregar para aplicações locais
FORWARD —> Trata os pacotes que passam pelo firewall com destino a rede local
OUTPUT 	—> Trata os pacotes que saem das aplicações locais
PREROUTING 	—> Trata os pacotes que chegam na interface de rede (entrada)
POSTROUTING —> Trata os pacotes após deixar a interface de rede (saída)


#########################################
#                Parâmetros             #
#########################################

-p —> especificar o protocolo (ex: TCP)
-s —> especificar a origem
-d —> especificar o destino
-i —> especificar a interface de entrada (ex: eth0)
-o —> especificar a interface de saída (ex: eth1)
-sport —> especificar a porta de origem
-dport —> especificar a porta de destino
-j —> especificar a ação (ACCEPT DROP REJECT)










## COMANDOS EM LINHA DE COMANDO


#Bloqueio do ping
	iptales -A INPUT -p ICMP -J DROP



# este local é onde ficam os arquivos de scripts
# devemos criar o arquivo firewall
	/etc/init.d/






###########################################################
##    Passo a Passo: Criando um script de inicialização  ##
###########################################################

# 1: Instalar o rcconf
# rcconf - permiti escolher os serviços que seram iniciados com o servidor
	apt-get install rcconf

# 2: Criar um arquivo chamado firewall dentro do /etc/init.d
# acrescentar as regras do firewall, salvar e sair.
#*** observação: Todo script deve iniciar com #!/bin/sh

	# vi /etc/init.d/firewall
		#!/bin/sh
		iptables -A INPUT -p ICMP -j DROP

# 3: Dar permissão de execução a este arquivo
	chmod +x /etc/init.d/firewall

# 4: Executar o rcconf e marcar o firewall
	rcconf

# 5: Reiniciar o servidor
	reboot



# *** Não esqueça de fazer os testes pingando o servidor a partir do host interno