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

######### ano #
  def calcular_ano_mais_lancamentos(self):
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
    
  def exibir_resultados_ano(self):
    ano_com_mais_lancamentos = self.calcular_ano_mais_lancamentos()
    print(ano_com_mais_lancamentos)
    return ano_com_mais_lancamentos


if __name__ == "__main__":
  visao = Jogos("games_amostra.csv")
  visao.Abrir_Arquivo()
  visao.exibir_resultados_ano()

