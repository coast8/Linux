

# sistema para relatorios de acesso
apt-get install sarg



# neste configurações imprtantes
/etc/sarg/sarg.conf
	

	#log de acesso tem que ser igual ao do squid
	access_log

	output_dir /var/www/sarg #local do diretorio web

# confugurações do relatorio
/etc/sarg/sarg-reports.conf

# comando para gerar o relatorio
sarg-reports today export LANG=pt_BR.UTF-8


#agendado tarefas
crontab -e
	*/5 * * * * /usr/sbin/sarg-reports today > /dev/null 2>&1


