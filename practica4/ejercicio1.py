class Generar_tarjeta():
	def __init__(self,BIN, cantidad=1, solo_impresion=False):
		self.BIN = BIN.replace(" ","")#Procesar espacios
		self.db_bins = "db_bins.txt"
 
		if(len(self.BIN) > 16 or len(self.BIN) < 15):#Tiene que tener la longitud indicada
			print("Por favor revisa la longitud del BIN.")
		elif(BIN[0].lower() == "x"):#Si no hay un bin especifico se elige uno de la db al azar
			print("No hay un BIN asignado, eligiendo uno al azar de la base de datos")
			bin_reg = list(self.BIN)
			bin_nuevo = self.bin_al_azar()
			for i in range(0,5):bin_reg[i] = bin_nuevo[i]
			self.BIN = "".join([i for i in bin_reg])
c=int(input("ingrese"))
print(Generar_tarjeta(c,10,))