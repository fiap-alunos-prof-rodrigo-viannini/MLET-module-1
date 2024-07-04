# Publicação da Biblioteca Uber Simulator no PyPI e GitHub

Este documento descreve os passos necessários para publicar a biblioteca Uber Simulator no PyPI (Python Package Index) e GitHub.

## PyPI (Python Package Index)

1. **Preparação Inicial:**
   - Verifique se o código da sua biblioteca está completo e funcionando corretamente.
   - Certifique-se de que todas as dependências estejam especificadas no arquivo `setup.py` e que o arquivo `README.md` contenha informações detalhadas sobre a biblioteca, funcionalidades e exemplos de uso.

2. **Criação de Conta no PyPI:**
   - Acesse o site do PyPI em https://pypi.org/ e crie uma conta se ainda não tiver uma.

3. **Preparação do Pacote:**
   - Crie um arquivo `setup.py` na raiz do seu projeto com informações sobre a biblioteca, versão, autor, descrição e dependências. Exemplo de `setup.py`:

     ```python
     from setuptools import setup, find_packages

     setup(
         name='uber-simulator',
         version='1.0.0',
         packages=find_packages(),
         install_requires=[
             # lista de dependências necessárias
         ],
         author='Seu Nome',
         author_email='seu@email.com',
         description='Simulador de viagens Uber em Python',
         long_description=open('README.md').read(),
         long_description_content_type='text/markdown',
         url='https://github.com/seu_usuario/uber_simulator',
         classifiers=[
             'Programming Language :: Python :: 3',
             'License :: OSI Approved :: MIT License',
             'Operating System :: OS Independent',
         ],
     )
     ```

4. **Build e Distribuição:**
   - No terminal, navegue até a raiz do projeto e execute o seguinte comando para criar o pacote:

     ```
     python setup.py sdist
     ```

   - Isso criará um diretório `dist` com um arquivo `.tar.gz` do seu pacote.

5. **Upload para o PyPI:**
   - Execute o seguinte comando para enviar seu pacote para o PyPI (será solicitado seu nome de usuário e senha do PyPI):

     ```
     twine upload dist/*
     ```

   - Após a conclusão, sua biblioteca estará disponível para instalação via `pip`.

## GitHub

1. **Criação de Conta no GitHub:**
   - Se ainda não tiver uma conta, crie uma conta no GitHub em https://github.com/.

2. **Criação de Repositório:**
   - Crie um novo repositório no GitHub para hospedar seu projeto Uber Simulator.

3. **Iniciação do Repositório Local:**
   - No terminal, navegue até a raiz do seu projeto e execute os seguintes comandos para inicializar o repositório Git, adicionar os arquivos e fazer o primeiro commit:

     ```
     git init
     git add .
     git commit -m "Initial commit"
     ```

4. **Vinculação com Repositório Remoto:**
   - Vincule seu repositório local ao repositório remoto no GitHub:

     ```
     git remote add origin https://github.com/seu_usuario/uber_simulator.git
     git push -u origin master
     ```

5. **Atualização do Repositório:**
   - Ao fazer atualizações no código, adicione, faça commit e envie para o GitHub:

     ```
     git add .
     git commit -m "Descrição das mudanças"
     git push
     ```

6. **Release no GitHub:**
   - Para marcar versões específicas do seu projeto, vá para a página do seu repositório no GitHub, clique na aba "Releases", e crie uma nova release indicando a versão e um changelog das alterações.

7. **Documentação e README.md:**
   - Mantenha o arquivo `README.md` atualizado com informações sobre o projeto, instruções de instalação e uso, exemplos e referências.

Este documento fornece uma visão geral dos passos necessários para publicar sua biblioteca Uber Simulator no PyPI e GitHub. Certifique-se de seguir as melhores práticas de documentação e versionamento para facilitar o uso e contribuições futuras.
