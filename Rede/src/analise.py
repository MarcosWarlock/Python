#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__autor__ = 'Marcos Rodrigues de Carvalho'

from scapy.all import *
import socket

def mac(ip):
    return sr1(ARP(pdst=str(ip))).hwsrc

def so(ip):
    a = sr1(IP(dst=str(ip))/ICMP())
    return ('Linux [ttl] --> {t}'.format(t=a.ttl) if a.ttl == 64 else 'Windows [ttl] --> {t}'.format(t=a.ttl) if a.ttl == 128 else 'Outro [ttl] --> {t}'.format(t=a.ttl))


def hostname(ip):
    try:
        return socket.gethostbyaddr(str(ip))[0]
    except Exception as erro:
        return erro

def iphost(hostname):
    try:
        return socket.gethostbyname(str(hostname))
    except Exception as erro:
        return erro

def grupo(hostname):
    try:
        return socket.gethostbyname_ex(str(hostname))[0]
    except Exception as erro:
        return erro
