peso_ideal = 0
altura = float(input("Digite sua altura: "))
peso_atual = float(input("Digite seu peso atual: "))
if altura > 3.00:
	altura = altura / 100
genero = input("Homem ou mulher? ")
if (genero == "homem"):
	peso_ideal = (72.7*altura) - 58
elif (genero == "mulher"):
		peso_ideal= (62.1*altura) - 44.7
peso_ideal= round(peso_ideal, 2)
print("O peso ideal é "+ str(peso_ideal)+"kg")
if(peso_atual>peso_ideal):
	print("Precisa reduzir " + str(round(float(peso_atual-peso_ideal),2)) +"kg, para atingir o peso ideal")