# API de Web Scraping e Download de Arquivos

Esta API foi desenvolvida utilizando FastAPI para realizar operações de web scraping em páginas web especificadas e permitir o download de arquivos XLSX.

## Instalação

1. **Clonar o repositório:**

   git clone https://github.com/fiap-alunos-prof-rodrigo-viannini/MLET-module-1.git

2. **Instalar dependências:**

   Recomenda-se criar um ambiente virtual antes de instalar as dependências.

   pip install -r requirements.txt

3. **Configurar ambiente:**

   Certifique-se de ter o ChromeDriver instalado e configurado corretamente, conforme necessário para o Selenium.

## Uso

1. **Iniciar a API:**

   Execute o seguinte comando para iniciar o servidor da API:

   uvicorn main --reload

   Isso iniciará o servidor localmente em `http://localhost:8000`.

2. **Endpoints Disponíveis:**

   - **Obter links do primeiro nível de um website:**
     ```
     GET /links/
     ```
     Retorna uma lista de links do primeiro nível de um website especificado.

   - **Obter links do segundo nível de um website:**
     ```
     GET /links2/?link={URL}
     ```
     Retorna uma lista de links do segundo nível de um website, onde `{URL}` é a URL do link para acessar.

   - **Baixar arquivo XLSX de uma URL:**
     ```
     GET /download/?link={URL}
     ```
     Baixa um arquivo XLSX da URL especificada.

3. **Exemplos de Uso:**

   - Para obter links do primeiro nível de um site:
     ```
     curl -X GET "http://localhost:8000/links/"
     ```

   - Para obter links do segundo nível de um site específico:
     ```
     curl -X GET "http://localhost:8000/links2/?link=https://example.com"
     ```

   - Para baixar um arquivo XLSX de uma URL:
     ```
     curl -X GET "http://localhost:8000/download/?link=https://example.com/file.xlsx"
     ```

## Documentação da API

Para uma documentação interativa da API, você pode acessar `http://localhost:8000/docs` após iniciar a API. Isso abrirá automaticamente o Swagger UI, onde você pode explorar os endpoints disponíveis, enviar solicitações e ver as respostas.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
