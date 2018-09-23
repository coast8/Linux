######################################################
# 1 - ElasticIP 
######################################################

## criar ip elastico

## associar ip elastico com a vps
	Obs: o servidor vai ser acessado usando o ip do elasticIP




######################################################
# 2 - Amazon Route 53
######################################################
## Apontando o dominio 

	* 1 - criar uma zona
		domain zone: dominio sem o http ex =>  site.com.br
		Type: Public hosted zone

	* 2 - deve gerar os enderecos de DNS
		  deve usar os enderecos sem o ponto no final

	* 3 - Create Recort Sets
			3.1
				Name: *
				value: elasticIP
				TTL(Seconds): 1 hora
			3.2
				Name: www
				value: elasticIP
				TTL(Seconds): 1 hora
			3.3
				Name: 
				value: elasticIP
				TTL(Seconds): 1 hora

## para finalizar devemos aponta o DNS do amazon para as conf de DNS 
## para o serviço de dominio.