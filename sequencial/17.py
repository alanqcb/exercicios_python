import math
lata_preco=60.00
lata_litros = 15.00
lata_mq = 6.00*lata_litros
lata_qtd = 0
lata_custo = 0
lata_sobra = 0
galao_preco = 25.00
galao_litros =3.60
galao_mq = 6.00 * galao_litros
galao_qtd = 0
galao_custo = 0
galao_sobra = 0
parede_mq = float(input("Quantos metros quadrados de parede precisam ser pintados: "))
## cenário de apenas lata
lata_qtd = math.ceil(parede_mq/lata_mq)
lata_custo = lata_qtd * lata_preco
lata_sobra = (lata_qtd*lata_litros - parede_mq/6)
lata_sobra = round(lata_sobra,2)
## cenário apenas galão
galao_qtd = math.ceil(parede_mq/galao_mq)
galao_custo = galao_qtd*galao_preco
galao_sobra = (galao_qtd*galao_litros - parede_mq/6)
galao_sobra = round(galao_sobra,2)
## cenário mesclado 1
mesc_mq = lata_litros*6+galao_litros*6
mesc_custo = lata_custo - 1*lata_preco + galao_preco
mesc_qtd = lata_qtd-1
## latas + 1 galão
mesc_sobra1 = ((lata_qtd-1)*lata_litros +galao_litros - parede_mq/6)
mesc_sobra1 = round(mesc_sobra1,2)
## latas + 2 galões
mesc_sobra2 = ((lata_qtd-1)*lata_litros +2*galao_litros - parede_mq/6)
mesc_sobra2 = round(mesc_sobra2,2)
## latas + 3 galões
mesc_sobra3 = ((lata_qtd-1)*lata_litros +3*galao_litros - parede_mq/6)
mesc_sobra3 = round(mesc_sobra3,2)
## resultado
print("Comprando apenas latas, precisaria de "+str(lata_qtd)+" unidades, o preço final é R$" +str(lata_custo) + ".")
print("Sobraria " + str(lata_sobra) + " litros.")
print("uma lata faz " +str(lata_litros*6)+" m².")
print("Comprando apenas galões, precisaria de "+str(galao_qtd)+" unidades, e o preço final é R$" +str(galao_custo) + ".")
print("Sobraria " + str(galao_sobra) + " litros.")
print("um galão faz " +str(galao_litros*6)+"m².")
print("Comprando latas e galões, precisaria de "+str(mesc_qtd)+" latas e um galão, o preço final é R$" +str(mesc_custo) + ".")
print("Sobraria " + str(mesc_sobra1) + " litros.")
