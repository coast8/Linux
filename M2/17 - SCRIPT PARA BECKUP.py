#!/bin/bash



INICIO='date +%d/%m/%Y-%H%M%S'

LOG=/tmp/log/'date +%Y-%m-%d'_log.backup_rsync.txt'



echo " " >> $LOG

echo " " >> $LOG

echo "| --------------- --------------- --------------- |" >> $LOG

echo " Sincronização iniciada em $INICIO" >> $LOG



## rsync -Cravzp /diretório_origem/ /diretorio_destino/

rsync -av --progess -e ssh senac@192.168.10.20:/home/senac/arquivos/ /tmp/bkp/ >> $LOG



FINAL='date +%d/%m/%Y-%H%M%S'

echo "  Sincronização finalizada em $FINAL" >> $LOG

echo "| --------------- --------------- --------------- |" >> $LOG

echo " " >> $LOG

echo " " >> $LOG


