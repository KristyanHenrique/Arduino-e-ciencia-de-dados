#python -m pip install pyserial
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=0)
arquivo = open("a.csv", "a")
while True:
	line = ser.readline()#ler entrada serial // limpar a porta
	valor = line.decode()#decodificar
	escrever = (valor+'-')#Colocar indicador da leitura 
	print(escrever)#Mostrar dados que irão pro arquivo
	arquivo.write(escrever)#Escrever no arquivo
	time.sleep(1)#Bufferar entrada serial