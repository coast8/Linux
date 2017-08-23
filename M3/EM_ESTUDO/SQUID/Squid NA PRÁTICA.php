## Squid

//para testar
aptitude search squid
aptitude install squid3


//iniciando a instalação do squid
apt-get update
apt-get upgrade
apt-get install squid

cd /etc/squid
ls
squid.conf
cp squid.conf squid.conf.backup
ls


//editando o squid
nano squid.conf						//editando o arquivo de configuração

http_access deny all				//linha a seer alterada
http_access allow all				//como deve ficar a linha

//3 linhas acima, no espaço em branco digitar
acl block url_regex -i "/etc/squid/block.txt"
http_access deny block

//salva o documento
//criando o arquivo de bloqueio
touch block.txt				//criando o arquivo
nano block.txt				//editando o arquivo
www.google.com.br			//bloqueando site
www.bol.com.br				//bloqueando site
//salva o arquivo

//próximo passo configurar a placa de rede.
ifconfig		//mostra todas as plaacas d redes e suas configurações.

//por padrão ja vem configurada a eth0, então vamos subir a eth1.
subindo a eth1
ifconfig eth1 1.1.1.1 netmask 255.255.255.240 up	//
enter
ifconfig	//verificando se as configurações pegaram

//redirecionamento da porta 80
//para a porta padrão do Squid 3128
iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 80 -j REDIRECT --to-port 3128

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

echo 1 > /proc/sys/net/ipv4/ip_forward

cd /etc/init.d		//entrar nesse diretorio
stop squid			//parando o squid
start aquid			//startando o squid

//vamos testar o squid com um sistema op microsoft
configurações de rede/propiedades/tcpIP/propiedades

ip					1.1.1.2		//mesma faixa de rede do servidor
mascara				255.255.255.240
gateway				1.1.1.1		//endereço do servidor

dns preferencial	8.8.8.8		//dns gratuito da google
dns alternativo		1.1.1.1		//endereço do servidor
ok


//configurando o navegador
//o navegador tem uma opção de marca o proxy
ferramentas/opções da internet/conexões/configuração da lan/marca usar servidor proxy para a rede local
endereço	1.1.1.1
porta		3128
não usar proxy para endereços locais
ok
ok

//AS paginas bloqueadas devem aparecer a seguinte mensagem.
Acesses Danied






tutorias passo a passo web doc
http://www.vivaolinux.com.br/etc/squid.conf-virtualboy


tutorias passo a passo web doc
http://www.marceloeiras.com.br/linux/tutorial/squid/squid.htm