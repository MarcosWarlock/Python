#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
########################################
# Descobrir todos os ips ativos na rede
# por: Marcos Rodrigues de Carvalho 
# nickname: warlock
# IRC: #labmacambira

import GeoIP
import sys
import os
import socket
from re import search
def descobre(ip):
	geo = GeoIP.new(GeoIP.GEOIP_STANDARD)
        new = [x for x in ip.split('.')]
	new.remove(new[len(new)-1])
	new = ".".join(new) + '.'
        cmd = 'ping -c1 -w1'
        for i in range(1,255):
		ip = new + str(i)
	        cmd = 'ping -c1 -w1 ' + ip
	        r = ''.join(os.popen(cmd).readlines())
	        if search('1 received', r):
			print ('[+] HOST ON: ' + ip + ' [+] HOSTNAME : ' + str(socket.gethostbyaddr(str(ip))[0]) + ' [+] Country: ' + str(geo.country_code_by_addr(str(ip))))
        
descobre(sys.argv[1])        
  
