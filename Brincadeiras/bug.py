#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
#############################################
# pastas infinitas  em python 
# por: Marcos Rodrigues de Carvalho
# nickname: warlock
# VOL: www.vivaolinux.com.br/~marcos_warlock 
# distribuição Gnu/Linux: Slackware 14.1
#############################################

import os
#loop infinito
def infinito(i=0, j=1):
    while True:
        yield(i)
        i += j
for i in infinito():
    os.mkdir("Pasta_%d" %i)
