LINUX DEBIAN

## Primeiro passo entra no sistema como superusuário
	su = comando para superusuário

## Em linux as partições são representadas como
	 /
## diferente do widows que são representadas como 
	c:




	## comandos básicos
ls 		= listar
ls -a   =lista os diretórios ocultos
ls -m   =lista na horizontal
ls -lh  =listar todas a informação com todos os detalhes



mkdir 				= criar um diretório
touch nome_arquivo 	= criando um arquivo
ls -l 				= listar conteudo detalhado
	se -  		= conteúdo é um arquivo
	se letra  	= conteúdo é um diretório
cd 			= entrada e saída de diretório
cd ..		= retorna um diretório
cd / 		= retorna ao diretório raiz



cat  nome_do_arquivo 		=executa o arquivo
nano arquivo 				=editar o arquivo
cp 	caminho_que_taoarquivo 	destino 	=copiar um arquivo
mv 	caminho_que_taoarquivo  destino 	=mover um arquivo
history 					=lista dos comandos executados
	


shift+pageUP 		=visualizar o que estar em cima
shift+pageDown 		=tela para baixo
shutdown 			=desligar, esse cmd tem parametros de segundos.
poweroff 			=deliga o sistema




	## Editores de texto
nano
pico
vim




	## Excluindo arquivos
rm  			=apaga arquivos
rmdir  			=apaga diretórios vazios
rm -r  			=apaga diretórios com arquivos


	## criando arquivos e diretorios
mkdir		=criar diretórios
mkdir -p 	=força a criar pastas e sub pastas.
touch  		=cria arquivos


	## informações extras
file arquivo 			   			  = mostra informações sobre o tipo de arquivo
echo “teste” | rev   =etset     	  == rev vira a palavra
echo “teste” | rev | cut -b -2   =et  == cut corta a palavra


df  					= espaço e disco em modo makina
df -h  					== – / / – em modo humano
free -h   				= memória
du -h  diritorio  		= espaço que o diretório ocupa
bc 					    =calculadora
cal  08 2012 			=calendario
fdisk -l   				=listar as partições
man comando   			=mostra o manual e oq o comando faz.


| wc -l    contando quantas linhas



man chgrp
man chmod
