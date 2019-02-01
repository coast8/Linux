# [Partições]

## obtendo informações das partições
cat /proc/partitions     //

fdisk -l /dev/sda        ## obtendo informações das partições
cfdisk /dev/sda          ##  - - -  / / --------/ / -----------------


## motando partição
mount -t auto /dev/sda3 /mnt/      ## montando uma partição windows para ler lido no linux.
## obs:  /dev/sda3  é a unidade de disco. 


## Desmontando partição
umount        /mnt/         ## desmontando a pasta mnt.
umount     /dev/sda3   		## desmontando a partição

## obs: os dois comandos tem as mesmas finalidades.
