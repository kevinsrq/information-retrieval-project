import pandas as pd
import numpy as np

# Função que calcula o log na base 2 da frequência das palavras em um documento
def log_freq(doc):
    """
    Calcula o log na base 2 da frequência das palavras em um documento.

    Args:
        doc (str): O documento para o qual o log de frequência será calculado.

    Returns:
        pandas.Series: A série de palavras e seus logs de frequência.

    """
    words = doc.split(' ') # Separar o documento em palavras
    freq = pd.Series(words).value_counts() # Contar a frequência de cada palavra
    log_freq = 1 + np.log2(freq) # Calcular o log na base 2 da frequência
    return log_freq

# Função que aplica a função log_freq a cada documento do dataframe
def ri_tf(dataframe: pd.DataFrame, column: str):
    """Calcula o term frequency relativo para cada documento em uma coluna do dataframe.
    Args:
    dataframe (pandas.DataFrame): O dataframe com a coluna desejada.
    column (str): O nome da coluna que contém os documentos.

    Returns:
        pandas.DataFrame: O dataframe com os logs de frequência para cada palavra em cada documento.

    """
    return dataframe[column].apply(log_freq).T

# Função que calcula o IDF (inverse document frequency) de cada termo do corpus
def ri_idf(dataframe: pd.DataFrame, column: str): 
    """Calcula o inverse document frequency relativo para cada palavra em uma coluna do dataframe.
    Args:
    dataframe (pandas.DataFrame): O dataframe com a coluna desejada.
    column (str): O nome da coluna que contém os documentos.

    Returns:
        dict: Um dicionário com as palavras e seus respectivos IDF relativos.

    """
    words = [phrase.split(' ') for phrase in dataframe[column]] # Separar cada frase em palavras

    df_t = pd.Series([i for j in words for i in j]).value_counts() # Contar a frequência de cada termo

    n_i = {} # Dicionário que armazenará a quantidade de documentos que contém cada termo
    idf = {} # Dicionário que armazenará o IDF de cada termo

    # Calcular n_i e IDF para cada termo do corpus
    for term in df_t.index: 
        n_i[term] = dataframe[column].map(lambda x: term in x).sum() # Quantidade de documentos que contém o termo
        idf[term] = np.log2(dataframe.shape[0]/n_i[term]) # IDF do termo

    return idf

# Função que calcula o TF-IDF de cada termo em cada documento do corpus
def tfidf(dataframe, column): 
    """Calcula o TF-IDF relativo para cada palavra em cada documento de uma coluna do dataframe.
    Args:
    dataframe (pandas.DataFrame): O dataframe com a coluna desejada.
    column (str): O nome da coluna que contém os documentos.

    Ret'urns:
        pandas.DataFrame: O dataframe com os TF-IDFs relativos para cada palavra em cada documento.

    """
    tf = ri_tf(dataframe=dataframe, column=column) # Calcular o TF de cada termo em cada documento
    idf = ri_idf(dataframe=dataframe, column=column) # Calcular o IDF de cada termo

    df = {}
    for word in tf.index: # Iterar por cada termo do corpus
        df[word] = tf.loc[word]*idf[word] # Calcular o TF-IDF do termo em cada documento

    return pd.DataFrame.from_dict(df, orient='index').fillna(0) # Retornar os resultados em um DataFrame
