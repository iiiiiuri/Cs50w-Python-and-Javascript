# 🏗️ Final Project - Flexy PDV
<img src="markdown/banner.png" width="100%">

# Introdução 📝

Flexy PDV é uma aplicação web abrangente de Ponto de Venda (POS), projetada para otimizar e simplificar a gestão de negócios de varejo. A aplicação permite um registro eficiente de vendas, análise detalhada de vendas diárias, controle de inventário em tempo real e gerenciamento de produtos intuitivo. Construído com Django no back-end e JavaScript no front-end, utilizando TailwindCSS para design responsivo e Jazzmin para a interface de administração, Flexy PDV garante uma experiência de usuário robusta e responsiva, tanto em dispositivos móveis quanto em desktops.

# Estrutura de Arquivos 📂

<img src="markdown/estrutura.png" width="200">

- `.env`: Arquivo para ambiente virtual Python (venv)
- `Flexy`: Projeto Django
    - `PDV`: App do projeto Django Flexy
        - `static`: Pasta com arquivos estáticos
            - `Css`: Pasta com arquivos CSS
            - `Js`: Pasta com scripts JavaScript
            - `Img`: Pasta com imagens
        - `Views`: Pasta com views Django
- `Markdown`: Pasta com todas as imagens para arquivo markdown
- `db.sqlite`: Banco de dados SQLite
- `manage.py`: Script para gerenciar o projeto Django

# 🌟 Distinção e Complexidade

Flexy vai além de ser apenas mais uma aplicação POV ou gerenciador de inventário. Sua singularidade e complexidade residem em sua abordagem abrangente para a gestão de negócios. Aqui está o porquê Flexy se destaca:

- `Funcionalidade Abrangente`: Enquanto muitas aplicações se concentram em áreas específicas como vendas ou inventário, Flexy oferece uma solução completa. Permite o gerenciamento de produtos, registro de vendas e análise detalhada, tudo em um só lugar. Os usuários podem lidar com todos os aspectos de seus negócios de forma contínua.

- `Controle de Estoque`: Monitorar o inventário em tempo real é crucial para qualquer negócio. Flexy fornece este recurso, garantindo que os usuários sempre saibam quais produtos estão disponíveis e quais precisam ser reabastecidos. Isso não só simplifica as operações diárias, mas também ajuda a prevenir a falta de estoque durante períodos críticos.

- `Análise Detalhada`: Tomar decisões estratégicas requer informações precisas e acionáveis. Com Flexy, os usuários podem acessar relatórios detalhados sobre vendas diárias, permitindo uma análise aprofundada do desempenho do negócio ao longo do tempo. Isso facilita a identificação de padrões, tendências e áreas para melhoria facilmente.

- `Interface Amigável`: Apesar de sua complexidade, a interface do Flexy permanece amigável ao usuário. Projetada para ser intuitiva e fácil de navegar, até mesmo usuários sem conhecimento técnico podem começar a usar o Flexy sem esforço. Isso reduz a curva de aprendizado e aumenta as taxas de adoção.

# Como Executar a Aplicação 🔛

### 1. Instale o Ambiente Virtual Python
```sh
python -m venv venv
```

### 2. Ative o Ambiente Virtual Python

**No Windows:**
```sh
venv\Scripts\activate
```

**No macOS/Linux:**
```sh
source venv/bin/activate
```

### 3. Instale as Dependências
```sh
pip install -r requirements.txt
```

### 4. Execute a Aplicação
```sh
python manage.py runserver
```


# Rotas e Endpoints 🌐

## Autenticação 🔐

    GET /: Página de login.
    POST /register: Página de registro de novo usuário.
    POST /logout: Logout do usuário atual.

## Pagamento 💳

    GET /pagamento: Página de pagamento.
    GET /resumoCompra/<int:cod>: Exibe o resumo da compra com o código fornecido.
    POST /removeCompra/<int:cod>: Remove a compra com o código fornecido.

## Gerenciamento de Produtos 📦

    POST /cadastrar: Registra um novo produto.
    POST /excluir: Exclui um produto.
    POST /excluir/<int:id>: Exclui um produto específico por ID.
    POST /editar: Edita um produto.
    POST /editar/<int:id>: Edita um produto específico por ID.
    GET /itemSelecionado/<int:id>: Exibe os detalhes de um produto específico por ID.

## Vendas 🛒

    POST /registrar_venda: Registra uma nova venda.
    GET /vendas: Renderiza a página de vendas.

## CSV 📄

    POST /upload_csv: Carrega produtos via CSV.
    GET /dadosVenda/<int:id>: Exibe os dados de uma venda específica por ID.

## Trocas 🔄

    POST /troca/<int:id>: Faz uma troca de um item por ID.
    GET /codVerify/<int:cod>: Verifica um código de troca.
    GET /dadosEmpresa/<str:user>: Exibe os dados da empresa do usuário.

## Análise 📊

    GET /analise/: Página de análise.
    GET /analise/getMetodoPagamento: Obtém os métodos de pagamento utilizados.
    GET /analise/getTopProdutosPerHour: Obtém os produtos mais vendidos por hora.
    GET /analise/getVendasPerHour: Obtém as vendas por hora.
    GET /analise/getVendasPerVendedor: Obtém as vendas por vendedor.


# Licença 📜

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more information.

Copyright 2024 Iuri de Lima Ferreira


<img src="markdown/logoIuri.svg" width="200">