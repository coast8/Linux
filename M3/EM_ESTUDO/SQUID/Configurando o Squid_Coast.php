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