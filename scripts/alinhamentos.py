def score_subst(ele_string_1, ele_string_2, equal = 2, subst = -1, g = -4):
  '''Função que compara um elemento das sequências e calcula a pontuação

  Se a comparação for feita com um gap, devolve o valor correspondente a um gap
  
  Se o elemento for igual devolve o valor equal, caso contrário o valor de substituição
  '''

  if '-' in ele_string_1 + ele_string_2: 
     return g
  
  elif ele_string_1 == ele_string_2:
      return equal
  
  else: 
      return subst
  
  