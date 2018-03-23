


R  	=leitura 	valor= 4
W 	=escrita 	valor= 2
X 	=execução 	valor= 1


 _______      ______        ________                                                                                                                                    
usuarios      grupos         outros

comando ls -l no inicio mostra essas informações
chmod
chown
chgrp


## prática
chmod go-rw teste   //retirando leitura e escrita
chmod g+r teste    	//adicionando leitura ao grupo
chmod o=g teste   	//grupo = outros nas permições

chmod a=rw          //comando para todos os usuarios

chmod 760  teste            //rwx rw-  - - -  ficara nesse esquema.

Chmod -R 700 download/      //mudando as permições do diretorio
