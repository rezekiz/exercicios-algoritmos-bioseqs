def validar_dna(sequencia): 
    '''
    Valida se a string apresentada é uma sequência de DNA válida
    '''
    sequencia = sequencia.upper()
    valido = sequencia.count("A") + sequencia.count('T') + sequencia.count('C') + sequencia.count('G')
    if valido == len(sequencia): return True
    else: return False

  def complemento_inverso(sequencia): 
    '''
    Função que itera sobre uma sequência de DNA e devolve
    o complemento reverso de cada nucleotido.

    Lógica:
    A -> T
    T -> A
    C -> G
    G -> C
    '''
    assert validate_dna(sequencia)
    
    complementar = ''
    
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
