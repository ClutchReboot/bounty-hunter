## FFUF
With HTTP, always `ffuf` after you find something.

### Directories
```bash
export TARGET="{{TARGET}}"
export WORDLIST="/opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt"

ffuf -ic -w $WORDLIST:FUZZ -u http://$TARGET/FUZZ -e .php,.html
```

### Sub Domains
```bash
export TARGET="{{TARGET}}"
export WORDLIST="/opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt"

ffuf -ic -w $WORDLIST:FUZZ -u http://10.10.11.196/ -H "HOST: FUZZ.$TARGET"
```