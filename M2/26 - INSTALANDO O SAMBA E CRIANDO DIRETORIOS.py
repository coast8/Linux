INSTALANDO O SAMBA E CRIANDO OS DIRETÃ“RIOS A SEREM COMPARTILHADOS

Atualizando a base do pacotes do APT:
------------------------------------
# apt-get update
# apt-get upgrade -u

Instalando o SAMBA:
------------------
# apt-get install samba

Criando os grupos de trabalho:
-----------------------------
# addgroup marketing
# addgroup rh
# addgroup diretoria

Criando os diretÃ³rios para compartilhamentos:
--------------------------------------------

# mkdir -p /EMPRESA/{marketing/geral,rh/geral,diretoria/geral}
# cd /EMPRESA
# chmod 770 -R *
# chgrp marketing -R marketing 
# chgrp rh -R rh
# chgrp diretoria -R diretoria

Para verificar use:
# ls -l
ou
# ls -lR

Editando o arquivo de configuraÃ§Ã£o do SAMBA

# cd /etc/samba
# mv smb.conf orig_smb.conf
# vim smb.conf
[global]
        server string   = debvbox20
        netbios name    = debvbox20
        workgroup       = sala010
        security        = user

[Marketing]
        comment         = Arquivos do Marketing
        path            = /EMPRESA/marketing
        public          = yes
        ; writeable     = yes 
        read only       = yes
        write list      = +marketing
        valid users     = +marketing
        create mask     = 0660
        directory mask  = 0770
        force group     = marketing
        ## Controle de conteÃºdo
        veto files      = /*.mp3/*.avi/*.bmp/*.wav/*.zip
        ## Lixeira do compartilhamento
        vfs object              = recycle
        recycle:keeptree        = yes
        recycle:version         = yes
        recycle:repository      = /EMPRESA/lixeira/%U
        recycle:exclude         = *.bak, *.iso, *.obj
        recycle:exclude_dir     = tmp, cache


Testando:
--------
# service samba restart

Criando usuÃ¡rio para o samba:
----------------------------

# useradd --no-create-home -s /bin/false maria
# useradd --no-create-home -s /bin/false teresa
# useradd --no-create-home -s /bin/false ivan

# smbpasswd -a maria
# smbpasswd -a teresa
# smbpasswd -a ivan

# adduser maria marketing
# adduser teresa rh
# adduser ivan diretoria


Instalando o Clamav

# apt-get install clamav clamav-docs clamav-daemon clamav-freshclam
# apt-get install arc arj bzip2 cabextract lzop p7zip pax tnef unrar-free unzip zoo

Ajustando o tempo de atualizaÃ§Ã£o das vacinas:

# nano /etc/clamav/freshclam.conf

Checks 12

Iniciando o Antivirus
# /etc/init.d/clamav-freshclam start

Instalando arquivos de teste:

# apt-get install clamav-testfiles

# clamscan /usr/share/clamav-testfiles

Agendando scaneamentos:

# echo 'clamscan -r /EMPRESA/' >> /etc/crontab

# nano /etc/crontab

30 * * * * clamscan -r /EMPRESA/












