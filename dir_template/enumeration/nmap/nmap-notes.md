# Nmap
Top Nmap Scans
```bash
export TARGET="{{TARGET}}"

# Basic Scan
sudo nmap $TARGET -oN basic.nmap -Pn -sV -sC -A

# All Ports
sudo nmap $TARGET -oN all-ports.nmap -Pn -p- --min-rate=1000

# UDP Scan
sudo nmap $TARGET -oN udp.nmap -Pn -sU

# Fragment
sudo nmap $TARGET -oN fragment.nmap -Pn -ff
```