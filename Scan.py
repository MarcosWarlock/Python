#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
########################################
# Descobrir todos os ips ativos na rede
# por: Marcos Rodrigues de Carvalho 
# nickname: warlock
# IRC: #labmacambira

import sys
import os
import socket
from re import search
def descobre(ip):
	f = open('data_ON.txt', 'w')
	g = open('data_OFF.txt', 'w')
	new = [x for x in ip.split('.')]
	new.remove(new[len(new)-1])
	new = ".".join(new) + '.'
	for i in range(1,255):
		ip = new + str(i)
		cmd = 'ping -c1 -w1 ' + ip
	        r = ''.join(os.popen(cmd).readlines())
		if search('1 received', r):
			print ('[+] HOST ON : ' + ip)
			f.writelines(str(ip) + '\n')
		else:
			print ('[-] HOST OFF: ' + ip)
			g.writelines(str(ip) + '\n')
	f.close()
	g.close()        
descobre(sys.argv[1])        

# Para usar o programa basta executar:
# python2.7 Scan.py <endereço de ip>
