peso_maximo = 50.00
mensagem = "O peso está dentro do limite, sem multas por hoje."
print("Bom dia, Sr. João.")
peso = float(input("Peso de hoje: "))
excedente = peso - peso_maximo
multa = excedente* 4
if(peso >peso_maximo):
	mensagem = "O peso está " +str(excedente)+"kg acima do permitido. Haverá multa de  R$ " + str(multa) + "."
print(mensagem)
