#!/bin/bash
export TARGET="{{TARGET}}"

# Basic Scan
sudo nmap -oN basic.nmap -Pn -sV -A $TARGET