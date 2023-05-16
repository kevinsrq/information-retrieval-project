import pandas as pd
import numpy as np

def lemmatize_word(word):
    '''
    Uma palavra lematizada é a forma básica ou canônica de uma palavra, sem os sufixos que indicam flexão de número, gênero, tempo, modo ou aspecto. Por exemplo, as palavras 'cantando', 'cantou' e 'cantaria' são lematizadas como 'cantar'.

    Esta função aplica algumas regras simples para remover os sufixos mais comuns em português, como 's', 'ns', 'ing', 'ly' e 'ed'. Ela não usa um dicionário ou um algoritmo sofisticado de análise morfológica, portanto pode não funcionar para todas as palavras ou casos especiais.

    Parâmetros
    ----------
    word : str
    A palavra a ser lematizada.

    Retorna
    -------
    str: A palavra lematizada.
    '''

    vowels = ['a', 'e', 'i', 'o', 'u']
    # Se a palavra termina com 'ns', remove os dois últimos caracteres
    if word.endswith('ns'):
        return word[:-2]

    # Se a palavra termina com 's', remove o último caractere
    if word.endswith('s'):
        return word[:-1]

    # Se a palavra termina com 'ing' e tem mais de cinco caracteres, aplica algumas regras para remover o sufixo
    if word.endswith('ing') and len(word) > 5:
        # Se os dois últimos caracteres antes de 'ing' são iguais e não são vogais, remove os quatro últimos caracteres e adiciona o terceiro último caractere
        if word[-4] == word[-5] and word[-5] not in vowels:
            return word[:-4] + word[-3:]
        # Se o terceiro último caractere é uma vogal, remove os três últimos caracteres
        elif word[-3] in vowels:
            return word[:-3]
        # Caso contrário, remove os dois últimos caracteres
        else:
            return word[:-2]

    # Se a palavra termina com 'ly' e tem mais de quatro caracteres, remove os dois últimos caracteres
    if word.endswith('ly') and len(word) > 4:
        return word[:-2]

    # Se a palavra termina com 'ed' e tem mais de três caracteres, aplica algumas regras para remover o sufixo
    if word.endswith('ed') and len(word) > 3:
        # Se os dois últimos caracteres antes de 'ed' são iguais e não são vogais, remove os três últimos caracteres e adiciona o segundo último caractere
        if word[-3] == word[-4] and word[-4] not in vowels:
            return word[:-3] + word[-2:]
        # Caso contrário, remove os dois últimos caracteres
        else:
            return word[:-2]

    # Se nenhuma das regras anteriores se aplica, retorna a palavra sem alteração
    return word
