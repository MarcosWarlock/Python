#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
#
# por: Marcos Rodrigues de Carvalho
# nickname: warlock

from pyfirmata import Arduino

class Controle:
	def __init__(self, board=Arduino(raw_input('Informe a porta USB: '))):
		self.board = board

	def ligar(self):
		self.board.digital[13].write(1) # envia sinal 1 para a porta digital 13 do arduino
	
	def desligar(self):
		self.board.digital[13].write(0) # envia sinal 0 para a porta digital 13 do arduino

