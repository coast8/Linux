[global]
        ;;; Diretivas do servidor e do domÃ­nio
        server string   = Servidor PDC Samba 20
        netbios name    = debvbox20
        workgroup       = DOMINIO20
        wins support    = yes
        ;;; Diretivas de seguranÃ§a
        security        = user
        encrypt passwords = yes
        passdb backend  = tdbsam
        obey pam restrictions   = yes
        pam password change     = yes
        unix password sync      = yes
        ; interfaces    = eth0 192.168.10.0/24
        ;;; Gerenciamento de usuÃ¡rios e computadores
        add user script = /usr/sbin/adduser --quiet --disabled-password --gecos " " %u
        delete user script      = /usr/sbin/userdel -r %u
        add group script        = /usr/sbin/addgroup --force-badname %g
        delete group script     = /usr/sbin/groupdel -r %g
        add user to group script        = /usr/sbin/usermod -G %g %u
        passwd program  = /usr/bin/passwd %u
        passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
        add machine script  = /usr/sbin/useradd -g computadores -c "%u Conta computador" -d /var/lib/samba -s /bin/false %u
        ;;; Administradores do sistema
        admin users     = root
        ;;; ConfiguraÃ§Ãµes de LOG
        syslog  = no
        max log size    = 1000
        log file        = /var/log/samba/log.%m
        ;;; Diretivas do PDC (Controlador de domÃ­nio primÃ¡rio)
        os level        = 75
        local master    = yes
        preferred master        = yes
        domain logons   = yes
        ;;; Diretivas NETLOGON e PROFILES
        logon drive = U:
        logon script    = %G.bat
        logon path      = \\%L\profiles\%U
        ;;; Sistema de impressÃ£o
        printing        = cups
        printcap name   = cups
        cups options    = Raw

[netlogon]
        ;;; NÃ£o esquecer de criat o dirtÃ³rio /var/samba/netlogon
        comment         = Scripts de logon
        path            = /var/samba/netlogon
        guest ok        = yes
        read only       = yes

[profiles]
        ;;; NÃ£o esquecer de criat o dirtÃ³rio /var/samba/profiles
        ;;; e ajustar as permissÃµes para: 1777
        comment         = Perfil mÃ³vel de usuÃ¡rios
        path            = /var/samba/profiles
        browseable      = yes
        read only       = no
        create mask     = 0600
        directory mask  = 0700

[Lixeira]
        comment         = Lixeira da rede
        path            = /EMPRESA/lixeira
        read only       = no
        create mask     = 0600
        directory mask  = 1700
        force create mode       = 0600

[Marketing]
        comment         = Arquivos do Marketing
        path            = /EMPRESA/marketing
        public          = yes
        ; writeable     = yes 
        read only       = yes
        write list      = +marketing, ivan
        valid users     = +marketing, ivan
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

[Recursos Humanos]
        comment         = Arquivos do RH
        path            = /EMPRESA/rh
        public          = yes
        ; writeable     = yes 
        read only       = yes
        write list      = +rh, ivan
        valid users     = +rh, ivan
        create mask     = 0660
        directory mask  = 0770
        force group     = rh
        ## Controle de conteÃºdo
        veto files      = /*.mp3/*.avi/*.bmp/*.wav/*.zip
        ## Lixeira do compartilhamento
        vfs object              = recycle
        recycle:keeptree        = yes
        recycle:version         = yes
        recycle:repository      = /EMPRESA/lixeira/%U
        recycle:exclude         = *.bak, *.iso, *.obj
        recycle:exclude_dir     = tmp, cache

[Diretoria]
        comment         = Arquivos da diretoria
        path            = /EMPRESA/diretoria
        public          = yes
        ; writeable     = yes
        read only       = yes
        write list      = +diretoria
        valid users     = +diretoria
        create mask     = 0660
        directory mask  = 0770
        force group     = diretoria
        ## Controle de conteÃºdo
        veto files      = /*.mp3/*.avi/*.bmp/*.wav/*.zip
        ## Lixeira do compartilhamento
        vfs object              = recycle
        recycle:keeptree        = yes
        recycle:version         = yes
        recycle:repository      = /EMPRESA/lixeira/%U
        recycle:exclude         = *.bak, *.iso, *.obj
        recycle:exclude_dir     = tmp, cache
