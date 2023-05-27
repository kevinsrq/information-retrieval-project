Projeto prático da matéria de Recuperação da Informação do curso de Pós-graduação da Ciência da Computação da UNESP

# Recuperação da Informação

Neste texto, apresentamos uma introdução ao projeto prático da matéria de recuperação da informação na UNESP. O objetivo deste projeto é desenvolver um sistema de busca que permita aos usuários encontrar documentos relevantes em uma coleção de textos. Para isso, utilizaremos conceitos e técnicas de recuperação da informação, tais como: indexação, processamento de linguagem natural, modelos de recuperação, medidas de avaliação e feedback de relevância. O projeto será dividido em quatro etapas: 

1. pré-processamento dos documentos; 
2. construção do índice invertido;
3. implementação do modelo de recuperação; 
4. avaliação do sistema.   

Este trabalho não tem como objetivo fornecer uma ferramenta otimizada, mas sim uma ferramenta funcional com codificação manual, sem o uso de pacotes externos, para uma melhor compreensão das técnicas apresentadas.

## Pré-processamento dos documentos

O pré-processamento de texto é uma etapa fundamental para a recuperação da informação, pois visa transformar os documentos em uma representação adequada para a análise e a busca. O pré-processamento envolve técnicas como tokenização, normalização, remoção de stopwords, stemização e lematização, que têm como objetivo reduzir a complexidade e a variabilidade dos textos. Essas técnicas facilitam a identificação de termos relevantes e a comparação entre documentos, melhorando a eficiência e a eficácia dos sistemas de recuperação da informação.

## Construção do índice invertido

Um índice invertido de texto é uma estrutura de dados que armazena as ocorrências de cada palavra em um conjunto de documentos. Ele permite realizar buscas rápidas e eficientes por termos ou frases em uma grande coleção de textos. O processo de construção de um índice invertido envolve as seguintes etapas: 

- Pré-processamento: consiste em remover caracteres especiais, acentos, pontuação e espaços em branco dos documentos, além de aplicar técnicas de normalização, como conversão para letras minúsculas e remoção de palavras muito frequentes ou irrelevantes (stopwords).
- Tokenização: consiste em dividir os documentos em unidades mínimas de significado, chamadas tokens. Os tokens podem ser palavras, números, símbolos ou combinações desses elementos.
- Indexação: consiste em atribuir um identificador único a cada documento e a cada token, e criar uma tabela que associa cada token aos documentos em que ele ocorre. Essa tabela é chamada de lista invertida ou posting list. Cada entrada da lista invertida contém o token, a frequência com que ele aparece na coleção e os identificadores dos documentos que o contêm.

O índice invertido é uma ferramenta essencial para a recuperação da informação, pois permite realizar consultas complexas e obter resultados relevantes em um curto espaço de tempo. 

$$TF-IDF = TF(t, d) \cdot IDF(t)$$

Onde:  

$TF(t, d)$: representa a frequência do termo t no documento d.  
$IDF(t)$: representa o inverso da frequência do documento (IDF) do termo t.  

A fórmula completa do IDF é dada por:

$$IDF(t) = \log \left( \frac{N}{DF(t)} \right)$$

Onde:  

$N$ é o número total de documentos na coleção.  
$DF(t)$ é o número de documentos que contêm o termo t.  

## Implementação do modelo de recuperação

A recuperação da informação é o processo de encontrar e acessar informações relevantes em um grande conjunto de dados. Existem diferentes modelos computacionais que podem ser usados para representar e organizar as informações, bem como para definir e executar as consultas dos usuários. Neste texto, vamos introduzir alguns dos principais modelos de recuperação da informação, como o modelo booleano, o modelo vetorial e o modelo probabilístico. Também vamos discutir as vantagens e desvantagens de cada um deles, e como eles podem ser aplicados em diferentes contextos e domínios.

## Avaliação do Sistema

A recuperação da informação é uma área que visa encontrar e fornecer informações relevantes para os usuários, a partir de grandes coleções de documentos. Para isso, existem diversos modelos de recuperação da informação, que se baseiam em diferentes princípios e abordagens para representar e comparar os documentos e as consultas dos usuários. A avaliação dos modelos de recuperação da informação é fundamental para verificar a sua eficácia e eficiência, bem como para identificar os seus pontos fortes e fracos. Existem diferentes formas de avaliar os modelos de recuperação da informação, tais como: a avaliação experimental, que utiliza medidas quantitativas e conjuntos de teste padronizados; a avaliação centrada no usuário, que considera as necessidades, preferências e comportamentos dos usuários; e a avaliação comparativa, que analisa as vantagens e desvantagens de diferentes modelos em relação a um critério ou objetivo específico. A escolha do método de avaliação depende do contexto e do propósito da recuperação da informação, bem como dos recursos disponíveis. A avaliação dos modelos de recuperação da informação é essencial para o desenvolvimento e aprimoramento da área, pois permite identificar os problemas existentes e propor soluções inovadoras.

Ao final do projeto, é esperado que possamos gerar rankings de similaridade de acordo com cada e-mail utilizado como input. 
