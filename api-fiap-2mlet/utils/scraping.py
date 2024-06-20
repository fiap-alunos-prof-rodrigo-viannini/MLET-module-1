from fastapi import HTTPException  # Importa a classe HTTPException da biblioteca FastAPI para tratar exceções HTTP
from selenium import webdriver  # Importa o webdriver do Selenium para controlar o navegador
from selenium.webdriver.chrome.options import \
    Options  # Importa a classe Options para definir opções específicas do navegador Chrome


def scrap_website(url: str):
    """
    Função que faz web scraping em uma página web especificada pela URL.

    Args:
        url (str): A URL da página web a ser raspada.

    Returns:
        str: O conteúdo da página web em formato HTML.

    Raises:
        HTTPException: Se ocorrer qualquer erro durante o processo de scraping.
    """
    try:
        options = Options()  # Cria uma instância de Options para configurar o navegador Chrome
        options.add_argument(
            "--headless")  # Adiciona argumento para executar o Chrome em modo headless (sem interface gráfica)
        options.add_argument("--no-sandbox")  # Adiciona argumento para desativar o sandboxing
        options.add_argument("--disable-dev-shm-usage")  # Adiciona argumento para desativar o uso de /dev/shm

        # Iniciar o chrome
        driver = webdriver.Chrome(options=options)  # Inicializa uma instância do Chrome com as opções definidas
        driver.get(url)  # Abre a URL fornecida no navegador
        page_content = driver.page_source  # Obtém o conteúdo HTML da página
        driver.quit()  # Fecha o navegador

        return page_content  # Retorna o conteúdo HTML da página

    except Exception as e:  # Captura qualquer exceção que ocorrer durante a execução
        raise HTTPException(status_code=500, detail=str(e))  # Lança uma exceção HTTP com status 500 e detalhes do erro
