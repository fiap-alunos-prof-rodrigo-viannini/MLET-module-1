from utils.find_links import find_links_at_level_one, find_links_at_level_two

def test_find_links_at_level_one():
    # Define o conteúdo HTML que será usado para testar a função find_links_at_level_one
    html_content = '<html><body><a href="http://iseb3.com.br/respostas-participantes/teste">Link 1</a></body></html>'

    # Chama a função find_links_at_level_one para encontrar os links no conteúdo HTML
    links = find_links_at_level_one(html_content)

    # Verifica se a lista de links retornada não está vazia
    assert len(links) > 0

    # Verifica se o link específico está presente na lista de links encontrados
    assert "http://iseb3.com.br/respostas-participantes/teste" in links



