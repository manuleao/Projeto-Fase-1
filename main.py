class Jogos:
  def __init__(self, arquivo):
    self.arquivo = arquivo
    self.jogos = []
  def Abrir_Arquivo(self):
    try:
      with open(self.arquivo, 'r', encoding='utf-8') as f:
        primeira = True
        for linha in f:
          if primeira:
           primeira = False
           continue
          self.jogos.append(linha.strip().split(';'))
    except FileNotFoundError:
      print(f"Erro: O arquivo '{self.arquivo}' não foi encontrado.")
    except Exception as e:
      print(f"Erro ao abrir o arquivo: {e}")


  def calcular_ano_mais_lancamentos(self):
    try:
      lista_ano = []
      lista_repeticao = []
      lista_ano_repeticao = []
      for jogo in self.jogos:
        ano_jogo = jogo[2][:4]
        lista_repeticao.append(ano_jogo) 
        if ano_jogo not in lista_ano:
          lista_ano.append(ano_jogo)
      for x in lista_ano:
        lista_ano_repeticao.append((lista_repeticao.count(x)))
      anos_indices = [i for i, valor in enumerate(lista_ano_repeticao) if valor == max(lista_ano_repeticao)]
      anos_com_mais_lancamentos = [lista_ano[i] for i in anos_indices]
      if len(anos_com_mais_lancamentos) > 1:
        return f"Anos com mais lançamentos: {', '.join(anos_com_mais_lancamentos)}"
      if len(anos_com_mais_lancamentos) == 1:
        return f"Ano com mais lançamentos: {anos_com_mais_lancamentos[0]}"
    except Exception:
      return "Erro ao calcular o(s) ano(s) com mais lançamentos."
  
  def calcular_gratuitos_pagos(self):
    try:
      gratuitos = 0
      pagos = 0
      for jogo in self.jogos:
        preco_jogo = jogo[6]
        if preco_jogo == "0":
         gratuitos += 1
        if preco_jogo != "0":
          pagos += 1
      return f"Percentual de jogos gratuitos: {gratuitos/(gratuitos+pagos)*100}%" + f" e percentual de jogos pagos: {pagos/(gratuitos+pagos)*100}%"
    except Exception:
     return "Erro ao calcular percentual de jogos gratuitos/pagos."

  def calcular_jogos_menos_dez_bem_avaliados(self):
    try:
      jogos_baratos_bem_avaliados = 0
      for jogo in self.jogos:
        try:
          av_positivas_jogo = int(jogo[22])
          av_negativas_jogo = int(jogo[23])
      
          if int(jogo[6]) < 1000 and av_positivas_jogo > av_negativas_jogo:
            jogos_baratos_bem_avaliados += 1
      
        except (ValueError, IndexError):
          continue
          
      return jogos_baratos_bem_avaliados
    except Exception:
      return "Erro ao calcular jogos baratos bem avaliados."

  def exibir_resultados_ano(self):
    ano_com_mais_lancamentos = self.calcular_ano_mais_lancamentos()
    print(ano_com_mais_lancamentos)
    return ano_com_mais_lancamentos
    
  def exibir_resultados_gratuitos_pagos(self):
    gratuitos_pagos = self.calcular_gratuitos_pagos()
    print(gratuitos_pagos)
    
  def exibir_jogos_baratos_bem_avaliados(self):
    jogos_baratos_bem_avaliados = self.calcular_jogos_menos_dez_bem_avaliados()
    if isinstance(jogos_baratos_bem_avaliados, int):
        print(f"A quantidade de jogos que custam menos de dez dólares e possuem mais avaliações positivas que negativas é {jogos_baratos_bem_avaliados}")
    else:
      print(jogos_baratos_bem_avaliados)

  def exibir_resultados(self):
    self.exibir_resultados_ano()
    self.exibir_resultados_gratuitos_pagos()
    self.exibir_jogos_baratos_bem_avaliados()
    
if __name__ == "__main__":
  visao = Jogos("games_amostra.csv")
  visao.Abrir_Arquivo()
  visao.exibir_resultados()

