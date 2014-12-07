#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
import socket, time, sys
from re import search
from pyfirmata import Arduino

class Controle:
	def __init__(self, board=Arduino(raw_input('Informe a porta USB: '))):
		self.board = board

	def ligar(self):
		self.board.digital[13].write(1) # envia sinal 1 para a porta digital 13 do arduino
	
	def desligar(self):
		self.board.digital[13].write(0) # envia sinal 0 para a porta digital 13 do arduino

# Cria uma instancia da classe Controle
action = Controle()

# definir o servidor 
server = 'irc.freenode.net'
porta = 6667 # port utilizado pelo IRC no linux
canal = '#ControleArduinoPython'
nick = 'Servidor'
senha = 'senha1234'

class Servidor:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((server, porta))
		self.s.send('NICK %s\r\n' %nick)
		self.s.send('USER ' + nick + ' ' + nick + ' ' + nick + ' .:\n')
		self.s.send('Join %s\r\n' %canal)
		time.sleep(2)
		print(self.s.recv(1024))

	def testar(self):
		self.teste = False
		while self.teste != True:
			self.msg = self.s.recv(5000)
			print (self.msg)
			if self.msg[0:4] == 'PING':
				self.s.send(self.msg.replace('PING', 'PONG'))
			if search('@conectar %s' %senha, self.msg):
				self.teste = True
				self.s.send('PRIVMSG %s : Conectado com sucesso!\r\n' %canal)

		while True:
			self.msg = self.s.recv(5000)
			print (self.msg)
			if self.msg[0:4] == 'PING':
				self.s.send(self.msg.replace('PING', 'PONG'))
			if search('@ligar', self.msg):
				action.ligar()
				self.s.send('PRIVMSG %s : Led ligado\r\n' %canal)
			if search('@desligar', self.msg):
				action.desligar()
				self.s.send('PRIVMSG %s : Led desligado\r\n' %canal)		
		
Servidor().testar()
