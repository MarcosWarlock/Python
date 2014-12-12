#!/usr/bin/env python
import serial
porta = '/dev/ttyACM0'
dados = 9600
a = serial.Serial(porta, dados)
while True:
    op = int(input('''
    [1] >> Ligar led
    [2] >> Apagar led
    : '''))
    if op == 1:
        a.write('a')
    else:
        a.write('b')
