import os

def read_files(doc_dir) -> dict:
    # Use a list comprehension to get a list of file paths
    database = [{'filepath': doc_dir,
                 'filename': filename,
                 'text': open(os.path.join(doc_dir, filename), 'r').read().strip()}
                 for filename in os.listdir(doc_dir)]

    return database

def process_files(doc_dir: str) -> dict:
    """
    Processa os arquivos em um diretório e seus subdiretórios.

    Args:
        doc_dir (str): Caminho para o diretório que contém os arquivos.

    Returns:
        list: Uma lista de dicionários contendo os dados processados de cada arquivo.

    """
    database = []  # Lista para armazenar os dados processados

    for filepath in os.listdir(doc_dir):  # Percorre os arquivos no diretório
        for filename in os.listdir(f'{doc_dir}{filepath}'):  # Percorre os arquivos nos subdiretórios

            # Abre o arquivo e lê seu conteúdo
            with open(os.path.join(doc_dir, filepath, filename), 'r') as f:
                text_data = f.read().strip()

            try:
                # Divide o conteúdo do arquivo em header e body
                header, body = text_data.split('\n\n', maxsplit=1)

                # Adiciona os dados processados à lista database
                database.append({
                    'filepath': filepath,
                    'filename': filename,
                    'body': body,
                })
            except ValueError:
                # Se ocorrer uma exceção ao dividir o conteúdo, continua para o próximo arquivo
                continue

    return database

