#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__autor__ = 'Marcos Rodrigues de Carvalho'

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

