



# aplicativo para monitoramento do servidor em moda grafico. dependencias (apache2 e php5) 
apt- get install munin munin-node munin-plugins-extra


# verificar se estar permintdo localhost
/etc/munin/munin-node.conf
	allow from all


# restartando 
/etc/init.d/munin-node restart

# apache
/etc/init.d/apache2 restart


# no navegador
servidor/munin




