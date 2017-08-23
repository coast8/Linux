#site do SQUI
# www.squid-cache.org

# instalação do squid
apt-get install squid3

# virificando se o serviço esta funcionando
service squid3 status


## arquivo chave de configuração
# este arquivo eh enorme, 7300 linhas
cd /etc/squid3/squid.conf


# devemos sempre fazer backup do arquivo original


	

#######################################################
#              squid.conf Ramos                       #
#######################################################

/etc/squid3/squid.conf

#***************************************** // *********************************

# acl -> é o comando para criar regras no squid
# porta padrao do squid
http_port 3128
# criar o chache, bizu deixa 1/3 da memoria total.
cache_mem 128 MB
# tamanh max dos arquivos
maximum_object_size_in_memory 64 KB
# tamanh max dos arquivos em HD
maximum_object_size 512 MB
#  tamanh minimos
minimum_object_size 0 KB
# porcentagem para descartar os arq mais entigos. 
cache_swap_low 90
cache_swap_high 95
cache_dir ufs /var/spool/squid3 2048 16 256
cache_access_log /var/log/squid3/access.log
#fim da conf do cache
# permitir tudo
acl all src all
#obrigam a autenticação do usuario PARA USAR A INTERNET
auth_param basic program /usr/lib/squid3/basic_ncsa_auth /etc/squid3/squid_passwd
acl autenticados proxy_auth REQUIRED
#regra para lista negra
acl lista_negra dstdom_regex "/etc/squid3/lista_negra"
http_access deny lista_negra
http_access allow autenticados
#fim-autenticação
#permitir acesso ao protocolo http
http_access allow all

#***************************************** // *********************************

service squid3 restart




#######################################################
#              squid.conf Wagner Fonseca              #
#######################################################

/etc/squid3/squid.conf

#***************************************** // *********************************
#####################
### autenticacao ####
#####################
#auth_param basic program /usr/lib/squid/pam_auth#usar as contas do linux.
auth_param basic program /usr/lib/squid3/basic_ncsa_auth /etc/squid3/squid_passwd
auth_param basic children 10#numero de conexoes simultaneas.
auth_param basic realm Altentique-se para acessa a internet#sera mostrado p usuario.
auth_param basic credentialsttl 4 hours#secao de 3 horas
auth_param basic casesensitive off
##
#################################
### Controles de Acesso (acl) ###
#################################
acl all src all
acl localhost src 127.0.0.1/32
### Controle de acesso ###
acl usuarios proxy_auth REQUIRED
acl negados url_regex sexy playboy sexo puta ultrasurf
acl liberados url_regex libsexy computador sexoesaude
acl downloads urlpath_regex \.avi$ \.rmvb$ \.mp3$  \.avi? \.rmvb? \.mp3?
##
###################
### htpp access ###
###################
http_access allow liberados
http_access deny negados
http_access deny downloads
http_access allow usuarios
###
http_access allow localhost
http_access deny all
###
#################################
### Configurações gerais      ###
#################################
http_port 3128
cache_mem 512 MB
maximum_object_size_in_memory 4 MB
cache_dir ufs /var/spool/squid 3000 16 256
access_log /var/log/squid/access.log squid
error_directory /usr/share/squid/errors/pt-br 




#***************************************** // *********************************

service squid3 restart








#######################################################
#              proxy autenticado no loda cliente     #
#######################################################

## opcoes do navegador para configurar o prox
# os demais navegadores como mozila e crome pegam as conf
# do internet explorer. 
# dica configurar no internet explorer para ver se os demais navegadores
# pegam as configurações do explorer.
configurações/conf avancadas/rede/conf da lan/servidor proxy



#instalando o apache, ele traz autenticação dos usuarios
#e sera usado
# apos intalação aponta para local-host
apt-get install apache2


#squid_passwd-> arquivo onde ficaram cadastrados usuarios e senhas.
/etc/squid3/squid_passwd

#cadastrando usuario no apache para serem usados no squid para acesso
# para intenet.
htpasswd squid_passwd nome_usuario  #comando tbm troca senha.












#######################################################
#             criando lista negra                     #
#######################################################

#bjetivo criar um arquivo que contenha palavras proibidas. 
#lista_negra-> este eh o arquivo que contem as palavras proibidas
/etc/squid3/lista_negra












#######################################################
#             cache do proxy squid                    #
#######################################################

# para questões de demsenho da internet
# os arquivos baixados ficam em cache no servidor
# cinsequentimente diminue a lagura de banda



#SCRIPT de configuração do cache:

#***************************************** // ***
cache_mem 128 MB
maximum_object_size_in_memory 64 KB
maximum_object_size 512 MB
minimum_object_size 0 KB
cache_swap_low 90
cache_swap_high 95
cache_dir ufs /var/spool/squid3 2048 16 256
cache_access_log /var/log/squid3/access.log

#***************************************** // ***


## BIZU

# Quantidade de memória RAM dedicada ao cache. 
# Reserve até 1/3 da memória RAM total do Servidor
cache_mem 128 MB

# Determina o tamanho máximo dos arquivos que serão guardados 
# no cache feito na memória RAM (o resto vai para o cache feito no HD).
maximum_object_size_in_memory 64 KB

# Configuração do cache em disco, que armazenará o “grosso” dos arquivos.
maximum_object_size 512 MB
minimum_object_size 0 KB

# Porcentagem de uso do cache que fará o Squid começar a 
# descartar os arquivos mais antigos. Por padrão, sempre 
# que o cache atingir 95% de uso, serão descartados arquivos 
# antigos até que a porcentagem volte para um número abaixo de 90%
cache_swap_low 90
cache_swap_high 95

# (/var/spool/squid) indica a pasta onde o Squid armazena os arquivos do cache, 
# o segundo (2048) indica a quantidade de espaço no HD (em MB) que será usada 
# para o cache, os números 16 e 256 indicam a quantidade de subpastas que serão 
# criadas dentro do diretório.
cache_dir ufs /var/spool/squid 2048 16 256

# Você pode definir ainda o arquivo onde são guardados os logs de acesso 
# do Squid. Por padrão, o Squid guarda o log de acesso no arquivo 
# “/var/log/squid3/access.log”.
cache_access_log /var/log/squid3/access.log




#######################################################
# personalizando a pag. de ERRO do proxy squid        #
#######################################################

https://www.vivaolinux.com.br/dica/Squid-Personalizando-o-arquivo-ERR_ACCESS_DENIED-ACESSO-NEGADO