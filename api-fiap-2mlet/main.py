from fastapi import FastAPI, HTTPException, Query  # Importa classes e funções necessárias do FastAPI
import os, json  # Importa módulos do sistema operacional e para manipulação de JSON
import requests  # Importa a biblioteca requests para fazer solicitações HTTP
import shutil  # Importa a biblioteca shutil para operações de arquivos
import logging  # Importa a biblioteca de logging para registrar informações e erros
from datetime import datetime  # Importa datetime para manipular datas e horas

from utils.find_links import find_links_at_level_one, find_links_at_level_two  # Importa funções de extração de links
from utils.scraping import scrap_website  # Importa função de scraping de sites

# Inicializa uma instância do FastAPI
app = FastAPI()

# Configura o logging para registrar informações e erros
logging.basicConfig(level=logging.INFO)

# Define uma rota GET para obter links do website
@app.get("/links/")
async def get_website_links():
    """
    Rota GET para obter links do primeiro nível de um website.

    Returns:
        dict: Um dicionário contendo uma lista de links encontrados.

    Raises:
        HTTPException: Se nenhum conteúdo ou link for encontrado.
    """
    # Faz o scraping do site especificado
    website_content = scrap_website("https://iseb3.com.br/respostas-em-planilhas")

    # Verifica se há conteúdo no site
    if not website_content:
        # Lança uma exceção HTTP 404 se nenhum conteúdo for encontrado
        raise HTTPException(status_code=404, detail="Nenhum conteúdo encontrado")

    # Extrai os links do conteúdo da página no primeiro nível
    links = find_links_at_level_one(website_content)

    # Verifica se há links extraídos
    if not links:
        # Lança uma exceção HTTP 404 se nenhum link for encontrado
        raise HTTPException(status_code=404, detail="Nenhum link encontrado")

    # Retorna os links extraídos como resposta
    return {"links": links}

# Define uma rota GET para obter links do segundo nível do website
@app.get("/links2/")
async def get_website_links2(link: str = Query(..., description="URL do link para acessar")):
    """
    Rota GET para obter links do segundo nível de um website.

    Args:
        link (str): A URL do link para acessar.

    Returns:
        dict: Um dicionário contendo uma lista de links encontrados.

    Raises:
        HTTPException: Se o parâmetro 'link' estiver ausente, ou se nenhum conteúdo ou link for encontrado.
    """
    # Registra o link recebido
    logging.info(f"Recebendo link: {link}")

    # Verifica se o link foi recebido corretamente
    if not link:
        # Lança uma exceção HTTP 400 se o parâmetro 'link' estiver ausente
        raise HTTPException(status_code=400, detail="Parâmetro 'link' é obrigatório")

    # Faz o scraping do site especificado pelo link
    website_content = scrap_website(link)

    # Verifica se há conteúdo no site
    if not website_content:
        # Lança uma exceção HTTP 404 se nenhum conteúdo for encontrado
        raise HTTPException(status_code=404, detail="Nenhum conteúdo encontrado")

    # Extrai os links do conteúdo da página no segundo nível
    links = find_links_at_level_two(website_content)

    # Verifica se há links extraídos
    if not links:
        # Lança uma exceção HTTP 404 se nenhum link for encontrado
        raise HTTPException(status_code=404, detail="Nenhum link encontrado")

    # Retorna os links extraídos como resposta
    return {"links": links}

# Define uma rota GET para fazer o download de um arquivo
@app.get("/download/")
async def download_file(link: str = Query(..., description="URL do link para o arquivo XLSX")):
    """
    Rota GET para fazer o download de um arquivo XLSX.

    Args:
        link (str): A URL do link para o arquivo XLSX.

    Returns:
        dict: Uma mensagem de sucesso e o caminho do arquivo salvo.

    Raises:
        HTTPException: Se o parâmetro 'link' estiver ausente, ou se ocorrer um erro durante o download ou processamento do arquivo.
    """
    # Registra o link de download recebido
    logging.info(f"Recebendo link de download: {link}")

    # Verifica se o link foi recebido corretamente
    if not link:
        # Lança uma exceção HTTP 400 se o parâmetro 'link' estiver ausente
        raise HTTPException(status_code=400, detail="Parâmetro 'link' é obrigatório")

    try:
        # Faz o download do arquivo a partir do link fornecido
        response = requests.get(link, stream=True)
        # Verifica se a solicitação foi bem-sucedida
        response.raise_for_status()

        # Verifica se o link aponta para um arquivo XLSX
        if not link.lower().endswith('.xlsx'):
            # Lança uma exceção HTTP 400 se o link não apontar para um arquivo XLSX
            raise HTTPException(status_code=400, detail="O link não aponta para um arquivo XLSX")

        # Extrai o nome do arquivo da URL
        filename = link.split('/')[-1]
        # Adiciona a data e hora atual ao nome do arquivo
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename_with_timestamp = f"{timestamp}_{filename}"

        # Caminho onde o arquivo será salvo
        save_dir = "C://PROJECTS//api-fiap-2mlet//files"
        # Cria o diretório se ele não existir
        os.makedirs(save_dir, exist_ok=True)
        # Caminho completo do arquivo salvo
        file_path = os.path.join(save_dir, filename_with_timestamp)

        # Salva o conteúdo do arquivo no disco
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)

        # Registra que o arquivo foi baixado e salvo com sucesso
        logging.info("Arquivo XLSX baixado e salvo com sucesso")

        # Retorna uma mensagem de sucesso e o caminho do arquivo salvo
        return {"message": "Arquivo XLSX baixado e salvo com sucesso", "file_path": file_path}

    except requests.RequestException as e:
        # Registra e lança uma exceção HTTP 500 se ocorrer um erro durante o download
        logging.error(f"Erro durante o download do arquivo: {e}")
        raise HTTPException(status_code=500, detail="Erro durante o download do arquivo")

    except Exception as e:
        # Registra e lança uma exceção HTTP 500 se ocorrer um erro durante o processamento do arquivo
        logging.error(f"Erro durante o processamento do arquivo: {e}")
        raise HTTPException(status_code=500, detail="Erro durante o processamento do arquivo")
