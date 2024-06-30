from utils.scraping import scrap_website


def test_scrap_website(mocker):
    # Mocka a criação de um objeto Chrome WebDriver da biblioteca Selenium
    mocker.patch("utils.scraping.webdriver.Chrome")

    # Conteúdo HTML fictício que será retornado pelo WebDriver mockado
    html_content = "<html><body><p>Test Content</p></body></html>"

    # Cria um objeto Mock para simular o comportamento do WebDriver
    mock_driver = mocker.Mock()
    mock_driver.page_source = html_content  # Define o conteúdo da página simulada
    mock_driver.get.return_value = None  # Simula o retorno da função get (abrir URL)
    mock_driver.quit.return_value = None  # Simula o retorno da função quit (fechar navegador)

    # Substitui a chamada original para criar um objeto Chrome WebDriver pela instância mockada
    mocker.patch("utils.scraping.webdriver.Chrome", return_value=mock_driver)

    # Chama a função a ser testada, passando uma URL fictícia
    content = scrap_website("http://iseb3.com.br/respostas-participantes-processo-20222023")

    # Verifica se o conteúdo retornado pela função é igual ao conteúdo HTML fictício
    assert content == html_content
