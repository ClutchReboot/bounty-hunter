## Nmap
Top Nmap Scans
```bash
export TARGET="{{TARGET}}"

# Basic Scan
sudo nmap -oN basic.nmap -Pn -sV -A $TARGET

# All Ports
sudo nmap -oN all-ports.nmap -Pn -p- $TARGET

# UDP Scan
sudo nmap -oN udp.nmap -Pn -SU $TARGET
```