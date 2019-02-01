##  VALUES FOR PERMISSIONS
R  	=leitura 	valor= 4
W 	=escrita 	valor= 2
X 	=execução 	valor= 1




# HOW TO READ THE LIST OF FILES
 _______         ______        ________                                                                                                                                    
propietario      grupos         outros

drwxr-xr-x  5 root root 4096 Mar 16 14:39 ./
drwxr-xr-x 14 root root 4096 Jan  8 11:59 ../
drwxrwxrwx  4 root root 4096 Mar 13 12:06 pasta-x/
drwxr-xr-x 12 root root 4096 Mar  9 20:12 pasta-y/
drwxrwxrwx  2 root root 4096 Mar 16 15:06 pasta-z/




# HOW TO READ THE LIST OF FILES
comando ls -l no inicio mostra essas informações
chmod 		## alterar as permições de arquivos e diretorios
chown 		## alterar o propietário do arquivo
chgrp 		## alterar o grupo de um arquivo ou pasta




# [prática]
chmod go-rw teste   ## retirando leitura e escrita
chmod g+r teste    	## adicionando leitura ao grupo
chmod o=g teste   	## grupo = outros nas permições
chmod a=rw          ## comando para todos os usuarios

# []
chmod 760  teste            ## rwx rw-  - - -  ficara nesse esquema.
Chmod -R 700 download/      ## mudando as permições do diretorio recursivamente

# []
chown $_usuario $_arquivo 
chown $_usuario $_diretorio

# []
chgrp $_grupo $_arquivo
chgrp $_grupo $_diretorio