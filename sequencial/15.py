taxa_ir = 0.11
taxa_inss = 0.08
taxa_sindicato = 0.05
sobra_salario = 1 - taxa_ir - taxa_inss - taxa_sindicato

valor_hora = float(input("Insira o valor da hora de tabalho: "))
horas_trabalhadas = float(input("Insira o número de horas trabalhadas no mês: "))

salario_bruto = round(valor_hora*horas_trabalhadas,2)
ir = round(salario_bruto * taxa_ir,2)
inss = round(salario_bruto * taxa_inss,2)
sindicato = round(salario_bruto * taxa_sindicato,2)
salario_liq = round(salario_bruto * sobra_salario,2)

print("+ Salário Bruto : ..........R$" + str(salario_bruto))
print("- IR (11%) : ...............R$"+ str (ir))
print("- INSS (8%) : ..............R$"+ str(inss))
print("- Sindicato ( 5%) : ........R$" + str(sindicato))
print("= Salário Liquido : ....... R$" + str(salario_liq))
