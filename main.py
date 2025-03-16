
f = open("games_amostra.csv")

######### ano #
lista_ano = []
lista_repeticao = []
lista_ano_repeticao = []


gratuitos = 0
pagos = 0

jogos_menosdez_saldo_avpositivo = 0

primeira = True
for linha in f:
  if primeira:
    primeira = False
    continue
  lista = linha.strip().split(";")
  if int(lista[6]) < 1000 and int(lista[22]) > int(lista[23]):
    jogos_menosdez_saldo_avpositivo += 1
  ######### perecentual de jogos gratuitos e pagos na plataforma #########


  if lista[6] == "0":
    gratuitos += 1
  if lista[6] != "0":
    pagos += 1


######### ano com mais jogos novos #########
  
  if lista_ano.count(lista[2][:4]) == 0:
          lista_ano.append(lista[2][:4])
  if lista_ano.count(lista[2][:4]) > 0:
          lista_repeticao.append(linha.strip().split(';')[2][:4])


for l in lista_ano:
  lista_ano_repeticao.append((lista_repeticao.count(l)))
  

#print(lista_ano)
#print(lista_repeticao)
#print(lista_ano_repeticao)
print('O ano com maior número de jogos novos é: ', lista_ano[(lista_ano_repeticao.index(max(lista_ano_repeticao)))])

######### perecentual de jogos gratuitos e pagos na plataforma #########

print('Percentual de jogos gratuitos: ', gratuitos/(gratuitos+pagos)*100, '%')
print('Percentual de jogos pagos: ', pagos/(gratuitos+pagos)*100, '%')


######### jogos de menos de 10 dolares com mais avaliacao positiva que negativa #########

print('Quantidade de jogos que custam menos de 10 dólares e que possuem mais avaliações positivas que negativas: ', jogos_menosdez_saldo_avpositivo)