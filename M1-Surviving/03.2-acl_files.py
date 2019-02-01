
# Varificando se o pacote esta instalado
	dpkg --list | grep acl

# instalando pacote
	apt-get install acl

# verificar as acl de um arquivo
	getfacl $_arquivo

# configurar as acl de um arquivo[usuarios, grupo, outros]
	setfacl [opcoes] ugo:nome:permissoes listar-arquivos
	
	EX:
	setfacl -m u:renata:r-x arquivo1
	setfacl -m g:financeiro:r-x arquivo2
	setfacl -m o:jose:r-x arquivo3

# retirando as acl de um arquivo ou grupo
	setfacl -m -x u:renata arquivo1

# retirando todas acl de um arquivo.
	setfacl -b arquivo1