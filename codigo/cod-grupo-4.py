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

def aprimorar_dna(seq):
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
     
def contar_bases(seq):

    """
    Devolve um dicionário com as frequências das bases de uma string de ADN (A, C, T e G)

    
    Parameters
    -------------
    seq : str
        Uma string que representa a sequência de ADN

    
    Returns
    -------------
    resultado : dict
        Dicionário com as frequências das bases da sequência introduzida
        As chaves são as bases "A", "T", "C" e "G" e os valores as frequências correspondentes

        
    Raises
    ----------
    ValueError
        No caso da string inserida não ser válida
    
    """

    if validar_dna(seq) is False:
        raise ValueError ("A sequência inserida é inválida")

    seq = aprimorar_dna(seq)
    
    contA = seq.count("A")
    contT = seq.count("T")
    contC = seq.count("C")
    contG = seq.count("G")
    
    resultado = {"A" : contA, "T" : contT, "C" : contC, "G" : contG}
    
    return resultado

def conteudo_gc(seq):
    
    """   
    Devolve a percentagem do conteúdo GC presente numa sequência de ADN

    
    Parameters
    -------------
    seq : str
        Uma string que representa a sequência de ADN

    
    Returns
    -------------
    resultado : float
        Percentagem do conteúdo GC na sequência de ADN

        
    Raises
    ----------
    ValueError
        No caso da string inserida não ser válida
    
    """

    if validar_dna(seq) is False:
        raise ValueError ("A sequência inserida é inválida")
    
    seq = aprimorar_dna(seq)
    
    conteudo_g = seq.count("G")
    conteudo_c = seq.count("C")
    conteudo_gc = round((conteudo_g + conteudo_c) / len(seq) * 100, 1)
    
        
    return conteudo_gc

conteudo_gc("gcta") 

def transc(seq):

    '''
        Função que itera sobre uma sequência de DNA e devolve
    a sequência transcrita.

    Lógica:
    A -> U
    T -> A
    C -> G
    G -> C

    Parameters:
    ------------
        seq : str Sequência de DNA
            Uma string que representa a sequência de DNA
    '''

    if not validar_dna(seq):
        print("Sequência inválida")
        return None

    '''
    Aqui é utilizada a função 'validar_dna' para garantir que a sequência não possui caracteres inválidos
    '''

    dna = aprimorar_dna(seq)
    mrna = ''

    '''
    A variável dna vai buscar a sequência aprimorada pela função definida anteriormente
    '''

    for base in dna:
        if base == 'A':
          mrna += 'U'
        elif base == 'T':
          mrna += 'A'
        elif base == 'C':
          mrna += 'G'
        elif base == 'G':
          mrna += 'C'
    '''
    Returns:
    --------
        str
          Sequência de mrna
    '''
    return mrna

'''
Chama a função 'transc' para fornecer uma varável, 'resultado'
'''

resultado = transc(seq)

'''
Se a sequência transcrita for válida, imprime o resultado
'''
if resultado is not None:
    print('A sequência de mRNA correspondente é:', resultado)

def complemento_inverso(sequencia : str) -> str:
    '''
    Função que itera sobre uma sequência de DNA e devolve
    o complemento reverso de cada nucleotido.

    Lógica:
    A -> T
    T -> A
    C -> G
    G -> C

    Parameters
    ----------

    sequencia : str
        sequência de DNA válida

    Returns
    -------
    str
        sequência de nucléotidos complementar à cadeia fornecida

    '''
    assert validar_dna(sequencia)

    complementar = '' # inicializamos a cadeia complementar

    for base in sequencia.upper():
        if base == 'A':
            complementar += 'T'
        elif base == 'T':
            complementar += 'A'
        elif base == 'C':
            complementar += 'G'
        elif base == 'G':
            complementar += 'C'

    return complementar



'''

SECÇÃO PARA FUNÇÃO GETORFS ASSIM QUE ESTIVER DEVIDAMENTE DOCUMENTADA

'''