#!/usr/bin/env python3.4

M=[[0,1], [2,3], [4,5]]
condicao1 = [5,1] not in [x for x in M]
condicao2 = [0,1] in [x for x in M]
print (condicao1, condicao2)

# Onde [x for x in M] percorre todos os elementos da matriz M
