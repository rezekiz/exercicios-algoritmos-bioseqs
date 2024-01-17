from auxiliares import print_matrix, reconstroi, score_subst


'''

Função de alinhamento que conjunta as subfunções e permite selecionar o algoritmo pretendido.

'''

def alinhar_sequencias(string_1, string_2, algoritmo, score_space = -4):
  
  if algoritmo == 'nw':

    needleman_wunch(string_1, string_2, score_subst, score_space)

  elif algoritmo == 'sw':

    smith_waterman(string_1, string_2, score_subst, score_space)

  else: raise ValueError("Algoritmo inválido - escolher entre Needleman-Wunch (NW) ou Smith-Waterman (SW)")


    



'''

Sub-funções da função alinhamento().

Algoritmo de Needleman-Wunch

'''


def needleman_wunch(string_1 : str, string_2 : str, score_subst : int, score_space : int = -4) -> tuple: 
  '''
  Parameters
  ----------
  string_1 : str
    primeira string

  string_2 : str 
    segunda string
  
  score_space : int
    valor penalidade atribuido a espaços vazios
  
  score_subst : int
    função que recebe dois caracteres e devolve o score da substituição de um pelo outro

  Returns
  -------

  tuple
    devolve um tuplo com o score do melhor alinhamento possível e o respetivo alinhamento
    
  '''
  # Garantimos que recebemos uma sequência. Este algoritmo não é só para DNA / aminoácidos por isso não usamos o validar_dna

  assert type(string_1) and type(string_2) == str

  # Acrescentamos os gaps para iniciar a matriz corretamente
  string_1 = '-' + string_1
  string_2 = '-' + string_2

  # Definimos o número de linhas e colunas da nossa matriz, posicionando as nossas strings
  # corretamente
  ncols = len(string_1)
  nlins = len(string_2)

  # Inicializar toda a matriz a zeros
  score = [[0 for gap in range(ncols)] for gap in range(nlins)]

  matriz_traceback = [[0 for gap in range(ncols)] for gap in range(nlins)]

  # Inicializar a primeira linha
  # Atribuí-se o valor de penalidade porque a primeira linha corresponde apenas a alinhamento espaços vazios
  # (ver output para visualizar)
  score[0] = [posicao_coluna * score_space for posicao_coluna, elemento in enumerate(string_1)]

  # Como estamos na primeira linha, estamos a alinhar apenas com espaços vazios
  # pelo que a matriz traceback indicará que devemos sempre caminhar à esquerda
  # (ver output para visualizar)

  matriz_traceback[0] = [0 if posicao_coluna == 0 else 'E' for posicao_coluna, elemento in enumerate(string_1)]


  # Inicializar a primeira coluna
  
  for posicao_linha, elemento in enumerate(string_2):
  
    # A lógica de preenchimento é semelhante à das linhas, mudando apenas 
    # a direção, que será vertical

    # Iteramos sobre o indice correspondente à posição do elemento na linha, indice 0 que corresponde
    # a primeira coluna 
    score[posicao_linha][0] = posicao_linha * score_space
  
    # Conforme mencionado acima, mesma lógica mas na vertical
    matriz_traceback[posicao_linha][0] = 0 if posicao_linha == 0 else 'C'


  # Iniciamos o primeiro ciclo for, que emparelha a segunda string com o a matriz score, correndo
  # linha a linha
  for posicao_linha, (elemento_string_2, linha) in enumerate(zip(string_2, score)):

    # No segundo ciclo for começamos a fazer a comparação dos elementos das strings, coluna a coluna

    for posicao_coluna, (elemento_string_1, valor_score) in enumerate(zip(string_1, linha)):

      
      if posicao_linha > 0 and posicao_coluna > 0: # Parte do 0 pois ignora a posição 0 são gaps

        # Compara os elementos ao longo de toda a matriz atribuindo os scores.

        # Compara diagonal
        diag = score[posicao_linha - 1][posicao_coluna - 1] + score_subst(elemento_string_1, elemento_string_2, score_space)
        
        # Compara à esquerda
        esq  = score[posicao_linha    ][posicao_coluna - 1] + score_space

        # Compara acima
        cima = score[posicao_linha - 1][posicao_coluna    ] + score_space

        # Agrupa os resultados, determina o maior score e atribui uma das direções.
        # usa-se uma string de referência para facilitar a atribuição / ser mais eficiente

        escolhas = [diag, esq, cima]
        direcoes = "DEC"

        # Encontramos o valor maior que corresponderá ao melhor score
        # que levará ao alinhamento ótimo

        valor = max(*escolhas)
        
        # Populamos a matriz score
        score[posicao_linha][posicao_coluna] = valor

        # Convertemos em direção e populamos a matriz traceback
        matriz_traceback[posicao_linha][posicao_coluna] = direcoes[escolhas.index(valor)]

        

  # Recorremos à função print_matrix() para imprimir as nossas matrizes score e traceback

  print_matrix(string_1, string_2, score)
  print_matrix(string_1, string_2, matriz_traceback)

  '''
  Devolvemos o último valor da matriz score (o ponto de partida para fazer o traceback)
  acrescentamos também as sequências reconstruídas partindo da matriz de traceback e usando
  a função reconstroi
  '''

  return score[-1][-1], reconstroi(string_1, string_2, score, matriz_traceback, 'nw')



'''

Algoritmo de Smith-Waterman

'''

def smith_waterman(string_1 : str, string_2 : str, score_subst : int, score_space : int = -4) -> tuple: 
  '''
  Parameters
  ----------
  string_1 : str
    primeira string

  string_2 : str 
    segunda string
  
  score_space : int
    valor penalidade atribuido a espaços vazios
  
  score_subst : int
    função que recebe dois caracteres e devolve o score da substituição de um pelo outro

  Returns
  -------

  tuple
    devolve um tuplo com o score do melhor alinhamento possível e o respetivo alinhamento
    
  '''
  # Garantimos que recebemos uma sequência. Este algoritmo não é só para DNA / aminoácidos por isso não usamos o validar_dna

  assert type(string_1) and type(string_2) == str

  # Acrescentamos os gaps para iniciar a matriz corretamente
  string_1 = '-' + string_1
  string_2 = '-' + string_2

  # Definimos o número de linhas e colunas da nossa matriz, posicionando as nossas strings
  # corretamente
  ncols = len(string_1)
  nlins = len(string_2)

  # Inicializar toda a matriz a zeros
  score = [[0 for gap in range(ncols)] for gap in range(nlins)]
  max_score = max([val for linha in score for val in linha])

  matriz_traceback = [[0 for gap in range(ncols)] for gap in range(nlins)]



  # Iniciamos o primeiro ciclo for, que emparelha a segunda string com o a matriz score, correndo
  # linha a linha
  for posicao_linha, (elemento_string_2, linha) in enumerate(zip(string_2, score)):
    #print('#####linha',posicao_linha,'#####') 
    # No segundo ciclo for começamos a fazer a comparação dos elementos das strings, coluna a coluna

    for posicao_coluna, (elemento_string_1, valor_score) in enumerate(zip(string_1, linha)):
      #print('####coluna',posicao_coluna,'####')
      
      if posicao_linha > 0 and posicao_coluna > 0: # Parte do 0 pois ignora a posição 0 são gaps

        # Compara os elementos ao longo de toda a matriz atribuindo os scores.
        
        # Compara diagonal
        diag = score[posicao_linha - 1][posicao_coluna - 1] + score_subst(elemento_string_1, elemento_string_2)
        #print('diag',diag)
        #print('e1,e2',(elemento_string_1,elemento_string_2))
        
        # Compara à esquerda
        esq  = score[posicao_linha    ][posicao_coluna - 1] + score_space
        #print('esq',esq,'score-space',score_space)

        

        # Compara acima
        cima = score[posicao_linha - 1][posicao_coluna    ] + score_space
        #print('cima',cima)
        

        # Agrupa os resultados, determina o maior score e atribui uma das direções.
        # usa-se uma string de referência para facilitar a atribuição / ser mais eficiente

        escolhas = [diag, esq, cima, 0]
        direcoes = "DEC"

        # Encontramos o valor maior que corresponderá ao melhor score
        # que levará ao alinhamento ótimo

        valor = max(*escolhas)
        #print('valor=',valor)
        
        # Populamos a matriz score
        score[posicao_linha][posicao_coluna] = valor


        # Convertemos em direção e populamos a matriz traceback
        if valor != 0: matriz_traceback[posicao_linha][posicao_coluna] = direcoes[escolhas.index(valor)] 
      
        # else: matriz_traceback[posicao_linha][posicao_coluna] = 0

     

  # Recorremos à função print_matrix() para imprimir as nossas matrizes score e traceback

  print_matrix(string_1, string_2, score)
  print_matrix(string_1, string_2, matriz_traceback)

  '''
  Devolvemos o último valor da matriz score (o ponto de partida para fazer o traceback)
  acrescentamos também as sequências reconstruídas partindo da matriz de traceback e usando
  a função reconstroi
  '''
  # Smith Waterman parte do valor mais alto para a reconstrução, por isso o valor de partida tem de ser o maior da matriz
  # Para isso é preciso "espalmar" a matriz para encontrar o valor mais alto

  max_score = max([val for linha in score for val in linha])
  # print('pontuacao-maxima=',max_score)
  return max_score, reconstroi(string_1, string_2, score, matriz_traceback, 'sw')
