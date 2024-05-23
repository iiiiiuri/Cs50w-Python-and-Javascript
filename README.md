# 🏗️ Project 2 : Models and Migrations - Site de Leilões
<img src="markdown/commerce.png" width="100%">

## 📝 Descrição
Este projeto é um site de leilões online desenvolvido com Django, onde os usuários podem criar, visualizar, fazer lances, comentar e acompanhar listagens de leilões. Os usuários também podem adicionar itens à sua lista de observação e fechar leilões. O projeto inclui uma interface de administração para gerenciamento de listagens, lances e comentários.

## 🎯 Funcionalidades
### 📚 Modelos
O projeto possui os seguintes modelos além do modelo User:
- AuctionListing: Representa uma listagem de leilão com campos para título, descrição, lance inicial, URL da imagem, categoria e status ativo/inativo.
- Bid: Representa um lance feito por um usuário em uma listagem de leilão.
- Comment: Representa um comentário feito por um usuário em uma listagem de leilão.

### 📝 Criar Listagem
- URL: /create_auction
- Descrição: Permite ao usuário criar uma nova listagem de leilão especificando um título, descrição, lance inicial, URL da imagem e categoria opcional.

### 📋 Página de Listagens Ativas
- URL: /
- Descrição: Exibe todas as listagens de leilões atualmente ativas com título, descrição, preço atual e foto (se disponível).

### 📖 Página da Listagem
- URL: /show/<int:id>
- Descrição: Exibe todos os detalhes de uma listagem específica de leilão.
    - Usuários autenticados podem adicionar ou remover a listagem da sua lista de observação.
    - Usuários autenticados podem fazer lances na listagem.
    - O criador da listagem pode fechar o leilão.
    - Se o leilão estiver fechado, exibe uma mensagem indicando o vencedor.
    - Usuários autenticados podem adicionar comentários à listagem, que são exibidos na página.

### 👀 Lista de Observação
- URL: /watchlist
- Descrição: Exibe todas as listagens que o usuário adicionou à sua lista de observação. Cada listagem é clicável e leva à página da listagem.

### 🏷️ Categorias
- URL: /categories
- Descrição: Exibe uma lista de todas as categorias de leilões. Clicar em uma categoria leva a uma página que exibe todas as listagens ativas nessa categoria.

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
- 🧭 Navegue e Interaja:
    - 📝 Registre uma nova conta ou faça login com uma conta existente.
    - 🛍️ Crie, visualize, edite e faça lances em listagens de leilões.
    - 👀 Adicione e remova itens da sua lista de observação.
    - 💬 Comente nas listagens de leilões.
    - 🔧 Use a interface de administração para gerenciar dados do site.

## 📂 Estrutura do Projeto
- `commerce/`: Diretório principal do projeto Django.
    - `auctions/`: Aplicativo Django contendo:
        - `templates/auctions/`: Templates HTML para as páginas do site.
        - `static/auctions/`: Arquivos CSS e JS.
        - `urls.py`: Configuração de URLs.
        - `views.py`: Lógica das views.
        - `models.py`: Definição dos modelos de dados.
- `settings.py`: Configurações do Django.
- `urls.py`: Configuração de URLs do projeto.

## 📋 Requisitos
- Python 3.x
- Django 3.x

# Licença 📜

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more information.

Copyright 2024 Iuri de Lima Ferreira


<img src="markdown/logoIuri.svg" width="200">
