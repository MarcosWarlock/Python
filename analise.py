#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Download do scapy disponível em [ http://www.secdev.org/projects/scapy/files/scapy-latest.tar.gz ]
# VOL: http://www.vivaolinux.com.br/~marcos_warlock
#

from scapy.all import *
import socket

def mac(ip):
    a = sr1(ARP(pdst=str(ip)))
    return a.hwsrc

def so(ip):
    a = sr1(IP(dst=str(ip))/ICMP())
    if a.ttl == 128:
        return 'Windows'
    elif a.ttl == 64:
        return 'Linux'
    else:
        return 'Outro'

def hostname(ip):
    a = socket.gethostbyaddr(str(ip))
    return a[0]

def iphost(hostname):
    return socket.gethostbyname(str(hostname))

def grupo(hostname):
    return socket.gethostbyname_ex(str(hostname))[0]

'''
Exemplo de como utilizar o programa:

[1] Abra o python no modo interativo
ATENÇÂO: Os argumentos de cada função devem ser passados entre " "

[2] Digite o nome da função passando o parametro

>>> from analise import *
>>> mac('192.168.0.1') #retorna o endereço mac referente ao ip 192.168.0.1
'01:02:AC:33:20:11'
'''
