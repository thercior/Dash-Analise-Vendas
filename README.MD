# ANÁLISE DE VENDAS 
<!-- Emoji e Language Tools -->
<div style="display: inline_block"><br>
<img align="center" alt="Thercio-Python" height="50" width="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

## Sobre
Dashboard construído em Python para apresentar dados de vendas de equipes de uma empresa, de forma intuitiva e dinâmica, verificando vendas por mês, por equipe, médias e outros gastos.

Este Dash é um projeto de **Análise de Vendas** desenvolvido durante o curso de Dashsboards da plataforma [Asimov Academy](https://asimov.academy/).


## Funcionalidades

- Temas dark e light
- Gráficos dinâmicos e iterativos
- Seletores de ano e equipe para alterar parâmetros
- Apresentação de resultados em gráficos e valores destacados


## Pré-requisitos

As dependências desse projetos encontram-se no arquivo requirements.txt.

Mas pode-se destacar as seguintes bibliotecas:
 - **dash==2.12.1**: criação da aplicação em dashboard
 - **dash-bootstrap-components==1.42.2** e **dash-bootstrap-templates==1.42.2**: criação dos layouts e componentes do dashboard
 - **ipykernel==6.25.1** (para habilitar o terminal iterativo)
 - **numpy==1.25.2** e **pandas=2.0.3**: para manipulação dos dados
 - **plotly=5.16.1**: para criação dos gráficos dinâmicos e iterativos




## Instalação

Clone o projeto para uma pasta de sua preferência.

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências utilizando o pacote pip do python. Pode ser:
- Digitando para cada biblioteca - onde tem nome-da-biblioteca:

    ```bash
    pip install nome-da-biblioteca
    ex: pip install dash==2.12.1
    ```
- Tendo um arquivo requirements.txt na pasta do projeto, basta apenas:

    ```bash
    pip install -r requirements.txt
    ```

Após isso, basta iniciar o servidor rodando o arquivo ```main.py``` no terminal na pasta do seu projeto:

```bash
python main.py
```

Após executar, no terminal irá aparecer a tela:

```bash
Dash is running on http://0.0.0.0:9000/

* Serving Flask app 'main'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:9000
* Running on http://172.31.8.131:9000
Press CTRL+C to quit
```
Pronto, agora o dash está rodando na porta 9000.
    
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thercio-rodrigues/)


## Demonstração

Insira um gif ou um link de alguma demonstração


## Screenshots

Imagem mostrando o layout do Dashboard.
<img src="assets/img/Captura de tela 2023-09-25 202307.png" alt="Layout Dash">


