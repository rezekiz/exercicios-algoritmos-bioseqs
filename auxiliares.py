def validar_dna(seq):
    
    """
    Devolve a validade de uma sequência de ADN

    
    Parameters
    -------------
    seq : str
        Uma string que representa a sequência de ADN

    
    Returns
    -------------
    bool : True se for uma sequência válida ou False se for uma sequência inválida
    
    """
    if not bool(seq): return False
    
    seq = seq.upper()        
    seq = seq.replace(" ","")   

    valido_dna = True
    
    for base in seq:                  
        if base not in "ATCG":         
            valido_dna = False
    
    if valido_dna == False:
        return False
    else:
        return True

def aprimorar_seq(seq):
    """
    Devolve uma sequência de ADN só com letras maiúsculas e sem espaços em branco

    Parameters
    -------------
    seq : str
        Uma string que representa a sequência de ADN

    Returns
    -------------
    str
        sequência de ADN com as bases em maiúsculas e sem espaços em branco
    
    """
    return seq.upper().replace(" ","")
     

''' Função usada para formatar o conteúdo, que irá ajudar na formatação da matriz '''

def formatar(conteudo):

    if not isinstance(conteudo, (int,float,str)): 
        print('Inválido, tem de ser um número ou string.')
        return None

    if type(conteudo) is int:

        '''Se x for um int converte-o em str e alinha-o à direita (por causa do indicador de formatação '>')
  
        Se pretendessemos alinhar à esquerda o indicador de formatação seria '<'
    
        A parte 3d significa o número mínimo de dígitos de largura que queremos no alinhamento.''' 
    

        return f"{conteudo:>3d}"

    else:

        '''
        Caso não seja um int alinha na mesma à direita mas aqui o fator d já não se aplica uma vez que o format
        code d não se aplica a strs por exemplo.
        '''

        return f"{conteudo:>3}"
    
''' Função usada para imprimir a matriz corretamente formatada '''

def print_matrix(primeira_string : str, segunda_string : str, matriz_scores : list):
  '''
  S1 -> primeira string
  S2 -> segunda string
  M  -> matriz

  '''

  '''
  Começamos por construir e formatadar a nossa linha de colunas.

  Para isso convertemos a string 1, correspondente às colunas, em lista e iteramos elemento a elemento.

  Usamos operador * para fazer unpack da lista, carater a carater. Desta forma não imprime a lista como um todo. 
  Neste caso usamos definimos o parâmetro sep da função print, indicando 2 espaços em branco para espaçar melhor a nossa linha de colunas.
  
  '''
  
  print(*list(" " + primeira_string), sep = '   ')

  '''
  Formatamos o conteúdo da nossa coluna de linhas e respetivo conteúdo das linhas.

  Para isto usamos um ciclo for que irá iterar por cada elemento do emparelhamento da nossa segunda string e a matriz de scores obtida.

  '''

  for linha, conteudo_linha in zip(segunda_string, matriz_scores):
    #print('linha', linha)
    conteudo_formatado = [formatar(conteudo) for conteudo in conteudo_linha]
    print(linha, *conteudo_formatado)

  print()       # Adicionamos um alinha em branco para separar do conteúdo seguinte.

'''
Função auxiliar que reconstroi as sequências devidamente alinhadas.

'''

'''
Função que encontra as coordenadas do valor mais alto da matrix score.

'''
def max_score_loc(scr):
    ms = scr[0][0]
    mi,mj = 0,0
    for linha in range(len(scr)): # itera por cada linha
    
        for coluna in range(len(scr[linha])): # itera por cada item de cada linha 
            if scr[linha][coluna] > ms:
                ms = scr[linha][coluna] # regista o maior
                mi,mj = linha,coluna # regista as coordenadas
    
    return mi,mj

'''

Função que reconstroi a sequência alinhada em função do algoritmo selecionado (NW ou SW)

'''

def reconstroi(string_1, string_2, score, matriz_traceback, algoritmo):
  '''
  Parameteres
  -----------

  string_1 : str
    primeira string para alinhamento

  string_1 : str
    segunda string para alinhamento

  matriz_traceback : list
    lista de listas correspondente a uma matriz com direções para percorrer as strings
    e reconstruir os alinhamentos

  Returns
  -------

  tuple
    devolve um tuple com as matrizes alinhadas
  
  '''
  
  # Iniciamos as variáveis-resultado
  string_1_alinhada = ''
  string_2_alinhada = ''
  
  if algoritmo == 'nw':
    # Criamos os contador para iterar, que nos devolverá o último elemento de cada string
    colunas = len(string_1) - 1
    linhas  = len(string_2) - 1
    

    # Itera pela matriz traceback e em função da direção calculada determina a posição e o elemento a atribuir.
    
    while matriz_traceback[linhas][colunas] != 0:
      # print(linhas, colunas, string_2[linhas], string_1[colunas], matriz_traceback[linhas][colunas])

      # Se na matriz andarmos na diagonal significa que os elementos são iguais, então saltam para o alinhamento
      if matriz_traceback[linhas][colunas] == 'D':
        string_1_alinhada = string_1[colunas] + string_1_alinhada  # De notar que adicionamos sempre a string alinhada no fim 
        string_2_alinhada = string_2[linhas]  + string_2_alinhada  # pois estamos a construí-la de trás para a frente

        linhas  -= 1                                               # Subtraímos 1 a linhas e colunas para avançar para percorrer
        colunas -= 1                                               # mais um nível na nossa matriz traceback

      # Se na matriz andarmos para cima, significa que não são iguais e conservamos o elemento da segunda string
      elif matriz_traceback[linhas][colunas] == 'C':
        string_1_alinhada = '-'              + string_1_alinhada
        string_2_alinhada = string_2[linhas] + string_2_alinhada

        linhas  -= 1                                              # Como andamos para cima só avançamos nas linhas

      # Se na matriz andarmos para a esquerda, significa que não são iguais e conservamos o elemento da primeira string
      elif matriz_traceback[linhas][colunas] == 'E':
        string_1_alinhada = string_1[colunas] + string_1_alinhada
        string_2_alinhada = '-'               + string_2_alinhada

        colunas -= 1                                               # Como andamos para a esquerda só avançamos nas colunas

  elif algoritmo == 'sw':
    coord_string_1, coord_string_2 = max_score_loc(score)

    # i = linha (s2)
    # j = coluna (s1)

#    s1 = '-' + s1
#    s2 = '-' + s2
#    print(coord_string_2,coord_string_1,s1[coord_string_2],s2[coord_string_1])
    while coord_string_1 > 0 and coord_string_2 > 0:

        if matriz_traceback[coord_string_1][coord_string_2] == 'D':
            string_1_alinhada = string_1[coord_string_2] + string_1_alinhada
            string_2_alinhada = string_2[coord_string_1] + string_2_alinhada

            coord_string_1 -= 1
            coord_string_2 -= 1

        elif matriz_traceback[coord_string_1][coord_string_2] == 'C':
            string_1_alinhada = '-' + string_1_alinhada
            string_2_alinhada = string_2[coord_string_1] + string_2_alinhada

            coord_string_1 -= 1
            coord_string_2 -= 1

        elif matriz_traceback[coord_string_1][coord_string_2] == 'E':
            string_1_alinhada = string_1[coord_string_2] + string_1_alinhada
            string_2_alinhada = '-' + string_2_alinhada

            coord_string_1 -= 1
            coord_string_2 -= 1
        
        elif matriz_traceback[coord_string_1][coord_string_2] == 0:
            string_1_alinhada = '-' + string_1_alinhada
            string_2_alinhada = '-' + string_2_alinhada

            coord_string_1 -= 1
            coord_string_2 -= 1
  
  else: raise ValueError("Algoritmo inválido - escolher entre Needleman-Wunch (NW) ou Smith-Waterman (SW)")
     
  print()
  print(string_1_alinhada, string_2_alinhada, sep = "\n")        # Imprimimos as nossas strings alinhadas em linhas separadas

  return (string_1_alinhada, string_2_alinhada)                  # Obtemos as strings alinhadas reconstruídas para uso futuro

''' Função que substitui os elementos das strings e devolve o seu score comparativo '''

def score_subst(ele_string_1, ele_string_2, g = 0):
  '''Função que compara e substitui um elemento de cada uma das strings.

  Se a comparação for feita com um gap, devolve o valor correspondente a um gap'''

  if '-' in ele_string_1 + ele_string_2: return g
  
  ''' 
  É então comparado se os elementos são iguais. Se forem iguais, obtemos um score positivo
  
  Caso contrário obtemos uma penalidade/valor negativo
  '''
  if ele_string_1 == ele_string_2:
    return 2
  else:
    return -1


def tipo_seq(seq):
    """
    Função que a partir de uma sequência, classifica-a em DNA, RNA ou SEQUÊNCIA AMINÁCIDOS.

    Parâmetro
    ---------
    seq : str 
        A sequência a ser classificada.

    Retorna
    -------
    str
        A classificação da sequência.
        
    """

    if not bool(seq):
        raise ValueError("É uma sequência inválida")

    seq = aprimorar_seq(seq)
    
    if validar_dna(seq):
        return "DNA"
        
    if len([c for c in seq if c not in "ACGU"]) == 0:
        return "RNA"
        
    elif len([c for c in seq if c not in "ABCDEFGHIKLMNPQRSTVWYZ_"]) == 0:
        return "SEQUÊNCIA AMINOÁCIDOS"
    
    else:
        raise ValueError("É uma sequência inválida")
    




def complemento_inverso(sequencia : str) -> str:
    '''
    Função que itera sobre uma sequência de DNA e devolve
    o complemento reverso de cada nucleotido.

    Parametros 
    ----------

    sequencia : str
        sequência de DNA válida

    Retorna
    -------
    str
        sequência de nucléotidos complementar à cadeia fornecida

    Levanta
    -------

    ValueError
        caso não se trate de uma sequênica de DNA válida
        
    '''
    assert sequencia != '' or sequencia != ' '
    #assert validar_dna(sequencia)
    

    complementar = '' # inicializamos a cadeia complementar

    if tipo_seq(sequencia) == 'DNA':
        for base in sequencia.upper():
            if base == 'A':
                complementar += 'T'
            elif base == 'T':
                complementar += 'A'
            elif base == 'C':
                complementar += 'G'
            elif base == 'G':
                complementar += 'C'
    
    elif tipo_seq(sequencia) == 'RNA':
        for base in sequencia.upper():
            if base == 'A':
                complementar += 'U'
            elif base == 'U':
                complementar += 'A'
            elif base == 'C':
                complementar += 'G'
            elif base == 'G':
                complementar += 'C'
    
    else:
        raise ValueError('É uma sequência inválida')

    return complementar[::-1]





def get_orfs(seq):
    """
    Função que a partir de uma sequência de DNA ou RNA origina diferentes tipos de ORFS.

    Parâmetro
    --------
    seq : str
        Sequência de DNA ou RNA.

    Returns
    -------
    lista
        Lista das ORFs geradas a partir da sequência.
    
    """
    seq_comp_inv = complemento_inverso(seq)
    lista_orfs = [
            seq[0:], seq[1:], seq[2:],
            seq_comp_inv[0:], seq_comp_inv[1:], seq_comp_inv[2:]
        ]
    return lista_orfs
    

