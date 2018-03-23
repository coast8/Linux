## programas usados no widows:
	winrar
	winzip

## comandos linux para compactar 
	tar
	gzip  	=tamanho do arquivo compactado diminui +- 50%
	bzip2  	=reduz o tamanho em +- 75%




## TEMOS AQUI ABAIXO UMA TABELA DE EXEMPLO DE COMO SE COMPACTAR
## o arquivo bin esta sendo usado como exemplo.

comando     copiar/verificar      novo_nome      arquivo 
tar          -cvf                bin.tar           /bin
tar          -cvzf               bin.tar.gz        /bin
tar          -cvjf          	 bin.tar.bz2       /bin
	

## Na hora de descompactar é só trocar o c pelo x.
tar 	-xvjf	  bin.tar.bz2	 /bin 

## listando arquivos compactados
tar   -tf   nome_do_arq_compactado  
