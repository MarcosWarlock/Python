#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
from re import search

ip = str(input('Entre com o endereço de IP: '))

#cria uma lista contendo cada parte do ip
ip = [x for x in ip.split('.')]
'''
ip = [x for x in ip.split('.')] é a mesmo que:

    lista = []
    for x in ip.split('.'):
        lista.append(x)
'''

#remover o ultimo numero do ip
ip.remove(ip[-1])
'''
exemplo:
    antes  --> ip = ['192', '168', '0', '1']
                
                ip.remove(ip[-1])

    depois --> ip = ['192', '168', '0']

'''
#juntar todos os elementos da lista numa unica string
ip = '.'.join(ip) + '.'

#gerar numeros de 1 a 254
for y in range(1,255):
    n = (ip + str(y))
    r = ''.join(os.popen('ping -c1 -w1 ' + n).readlines())
    if search('1 received', r):
        with open('ip.txt', 'a') as f:
            f.write('HOST ON [+] ' + n + '\n')
        print('HOST ON [+] ', n)
