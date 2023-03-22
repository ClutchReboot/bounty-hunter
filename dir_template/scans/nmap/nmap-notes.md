## Nmap
Top Nmap Scans
```bash
export TARGET="{{TARGET}}"

# Basic Scan
sudo nmap $TARGET -oN basic.nmap -Pn -sV -sC

# All Ports
sudo nmap $TARGET -oN all-ports.nmap -Pn -p- --min-rate=1000

# UDP Scan
sudo nmap $TARGET -oN udp.nmap -Pn -SU
```