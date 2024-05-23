# 📚 Project 1 : Backend Django - Enciclopédia Online

<img src="markdown/wikipedia.png" width="100%">

## 📝 Descrição

Este projeto é uma enciclopédia online que permite visualizar, criar, editar e buscar entradas utilizando a linguagem de marcação Markdown. Baseado na estrutura do Wikipedia, este projeto foi desenvolvido usando Django e permite a conversão de conteúdo Markdown para HTML para ser exibido aos usuários.

## 🌐 Navegação e Funcionalidades do Site

### 🏠 Página Inicial
- URL: `"/"`
- Lista todas as entradas da enciclopédia. (Função: `index`)

### 📖 Página de Entrada
- URL: `"/wiki/<str:title>/"`
- Exibe o conteúdo de uma entrada da enciclopédia especificada pelo título. Se a entrada não existir, uma página de erro é exibida. (Função: `entry`)

### 🔍 Busca
- URL: `"/search/"`
- Permite ao usuário buscar por entradas na enciclopédia. Se a consulta coincidir com o nome de uma entrada, o usuário é redirecionado para a página dessa entrada. Se não, uma página de resultados é exibida com todas as entradas que contêm a consulta. (Função: `search`)

### 📝 Nova Página
- URL: `"/new/"`
- Permite ao usuário criar uma nova entrada na enciclopédia. Se uma entrada com o título fornecido já existir, uma mensagem de erro é exibida. Caso contrário, a nova entrada é salva e o usuário é redirecionado para a página da nova entrada. (Função: `new`)

### ✏️ Editar Página
- URL: `"/edit/"`
- Permite ao usuário editar o conteúdo de uma entrada existente. O conteúdo atual é pré-preenchido na área de texto. (Função: `edit`)

### 💾 Alteração de Dados
- URL: `"/data_change/"`
- Salva as alterações feitas pelo usuário na entrada existente e redireciona o usuário para a página atualizada da entrada. (Função: `data_change`)

### 🎲 Página Aleatória
- URL: `"/rand/"`
- Redireciona o usuário para uma entrada aleatória da enciclopédia. (Função: `randomize`)

### 🔄 Conversão de Markdown para HTML
- O conteúdo em Markdown de cada entrada é convertido para HTML antes de ser exibido ao usuário.
- Utiliza o pacote markdown2 para a conversão, que pode ser instalado via `pip3 install markdown2`.

## 🚀 Como Utilizar

Siga os passos abaixo para configurar e executar o projeto:

1. **Clone o Repositório**

    Clone este repositório para sua máquina local.

    ```sh
    git clone <url_do_repositório>
    ```
2. **Instale as Dependências**

    Instale as dependências do projeto com o seguinte comando:

    ```sh
    pip install -r requirements.txt
    ```

2. **Inicie o Servidor Django**

    Execute o seguinte comando no terminal para iniciar o servidor Django:

    ```sh
    python manage.py runserver
    ```
    
## 🏗️ Estrutura do Projeto
- `wiki/`: Diretório principal do projeto Django.
    - `encyclopedia/`: Aplicativo Django contendo:
        - `templates/encyclopedia/`: Templates HTML para as páginas do site.
        - `static/encyclopedia/`: Arquivos CSS e JS.
        - `urls.py`: Configuração de URLs.
        - `views.py`: Lógica das views.
        - `util.py`: Funções utilitárias para interagir com as entradas da enciclopédia.
        - `entries/`: Diretório onde os arquivos Markdown das entradas são armazenados.
    - `settings.py`: Configurações do Django.
    - `urls.py`: Configuração de URLs do projeto.

## 📋 Requisitos
- Python 3.x
- Django 3.x
- markdown2

## 👨‍💻 Autor
Este projeto foi desenvolvido como parte de um exercício prático para o curso CS50W da Universidade de Harvard.

# Licença 📜

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more information.

Copyright 2024 Iuri de Lima Ferreira


<img src="markdown/logoIuri.svg" width="200">
