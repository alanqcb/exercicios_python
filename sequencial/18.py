# tamanho = float(input("Insira o tamanho do arquivo em megabytes: "))
# velocidade = float(input("Insira a velocidade da internet megabytes: "))
tamanho = 90501
velocidade = 1
tempo = (tamanho / velocidade)
segundos = tempo
minutos = 0
horas = 0
dias = 0
dias = round((((segundos/60)/60)/24))
horas = round(((segundos/60)/60))
minutos = round(segundos/60) 
print("tempo: " +str(dias)+" dias: "+str(horas-dias*24)+" horas : "+str(minutos-horas*60)+" minutos : "+str(segundos-minutos*60)+" segundos")
