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
-------     ----------------     -------------   --------
tar          -cvf                file.tar        file
tar          -cvzf               file.tar.gz     file
tar          -cvjf          	 file.tar.bz2    file
	

## Na hora de descompactar é só trocar o c pelo x.
-----   -----   ----------
tar 	-cvf	file.tar 

## listando arquivos compactados
-----   -----     ---------
tar     -tf       file.tar  
