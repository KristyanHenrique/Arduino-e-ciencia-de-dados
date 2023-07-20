python -m pip install pyserial
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=0)
arquivo = open("a.csv", "a")

while True:
	line = ser.readline()
	valor = line.decode()
	print(valor)
	arquivo.write(valor)
	time.sleep(1)

