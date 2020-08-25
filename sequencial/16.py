import math
parede = 10.00
parede = float(input("Quantos metros quadrados de parede precisam ser pintados: "))
lata_preco=80.00
lata_eficiencia = 3.00
lata_qtd = (math.ceil(parede / lata_eficiencia))
lata_sobra = lata_qtd*lata_eficiencia - parede
print("Você precisa comprar " + str(lata_qtd) + " latas para pintar " + str(parede) +"m² de parede.")
print("Vai sobrar " + str(round((lata_sobra/lata_eficiencia)*100,2))+r"% da lata")
