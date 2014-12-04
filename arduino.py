#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-
###############################################
# programa para controle de luz via internet
# com python e arduino
# por: Marcos Rodrigues de Carvalho
# nickname: warlock
# VOL: www.vivaolinux.com.br/~marcos_warlock
###############################################

#módulos que serão utilizados
import socket, time, sys
from re import search
from pyfirmata import Arduino

#definir a porta no qual o arduino estará conectado
board = Arduino(raw_input('Informe a porta usb: '))

# classe que conterá métodos de controle do arduino
class Controle:
	def __init__(self):
		None
	def ligar(self):
		board.digital[13].write(1) # envia sinal 1 para a porta 13 do arduino, isto é, HIGH (ligado)
		time.sleep(1)
	def desligar(self):
		board.digital[13].write(0) # envia sinal 0 para a porta 13 do arduino, isto é, LOW (desligado)
		time.sleep(1)
# criar uma instância da classe Controle
action = Controle()

# criar a classe socket do programa, ou seja, a parte 
# servidor do programa que irá se conectar no irc

# definir o servidor a ser conectado
server = 'irc.freenode.net'
porta = 6667
canal = '#ControleArduinoByPython'
nick = 'Servidor'
senha = '123456'

#classe do servidor socket
# para mais informações sobre socket digite no python: help(socket)
class Servidor:
	def __init__(self):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um socket 
		except socket.error, msg:
			print 'Falha na criação do socket. Código de erro: ' + str(msg[0] + ' Mensagem de erro: ' + msg[1])
			sys.exit()
		print ('Socket criado com sucesso!')

		try:
			self.ip = socket.gethostbyname(server) # obtem o ip do server
		except socket.gaierror:
			print ('Host: %s não foi resolvido' %str(self.ip))
			sys.exit()
		print ('Ip address de ' + server + ' é ' + self.ip)

		self.s.connect((server, porta)) # conecta o socket no server na porta especificada
		print ('Socket conectado com ' + server + ' sobre o ip ' + self.ip)
		time.sleep(1)
		print (self.s.recv(1024))

	# Verifica o que será digitado no canal do IRC
	def testar(self):
		self.teste = False
		while self.teste != True:
			self.msg = self.s.recv(5000)
			print (self.msg)
			if self.msg[0:4] == 'PING':
				try:
					self.s.send(self.msg.replace('PING', 'PONG'))
				except socket.error:
					print ('Falha no envio dos dados ao host ' + server + ' IP: \r\n' + self.ip)
				print ('Enviando dados ao host ' + server + ' IP: ' + self.ip)
			if search('@conectar %s' %senha, self.msg): # se for digitado @conectar + senha 
				try:
					self.s.send('PRIVMSG %s : Conectado a ' + host + 'IP: ' + self.ip + ' Porta: \r\n' + porta %canal)
					self.teste = True # CONECTADO
				except socket.error:
					print ('Falha ao se conectar')
		# também verifica o que será digitado no canal do IRC
		while True:
			self.msg = self.s.recv(5000)
			print (self.msg)
			if self.msg[0:4] == 'PING':
				try:
					self.s.send(self.msg.replace('PING', 'PONG'))
				except socket.error:
					print ('Falha no envio dos dados ao host ' + server + ' IP: ' + self.ip)
				print ('Enviando dados ao host ' + server + ' IP: ' + self.ip)
			if search('@ligar', msg): # se for digitado @ligar 
				action.ligar() # chama o metodo para ligar o led
				try:
					self.s.send('PRIVMSG %s : Luz ligada\r\n' %canal)
				except socket.error:
					self.s.send('PRIVMSG %s : Erro ao enviar\r\n' %canal)
				print ('Comando para ligar a luz foi recebido de ' + server + ':' + porta)
			if search('@desligar', msg):
				action.desligar() # chama o metodo para apagar o led
				try:
					self.s.send('PRIVMSG %s : Luz desligada\r\n' %canal)
				except socket.error:
					self.s.send('PRIVMSG %s : Erro ao enviar\r\n' %canal)
				print ('Comando para desligar a luz foi recebido de ' + server + ':' + porta)
Servidor().testar()






