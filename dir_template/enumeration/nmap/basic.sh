#!/bin/bash
export TARGET="{{TARGET}}"

# Basic Scan
sudo nmap $TARGET -oN basic.nmap -Pn -sV -sC -A