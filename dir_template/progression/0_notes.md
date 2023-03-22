## {{TARGET}}

### Update `/etc/hosts`
```bash
{{TARGET_IP}} {{TARGET}}
```
 
### Set Aliases
```bash
echo "{{QUICK_DIR}}" >> ~/.bash_aliases
source ~/.profile
```