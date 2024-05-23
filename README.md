# 📧 Project 3 : Django + Javascript - Cliente de Email
<img src="markdown/banner.png" width="100%">

## 📝 Descrição
Este projeto é um cliente de email desenvolvido com Django e JavaScript, onde os usuários podem enviar, receber, arquivar e visualizar emails. O sistema utiliza um banco de dados para armazenar as mensagens, em vez de enviá-las para servidores de email reais.

## 🛠️ Funcionalidades
### 📚 Modelos
O projeto utiliza um modelo de dados para representar emails, incluindo informações sobre o remetente, destinatários, assunto, corpo da mensagem, data e hora, e status (lido/não lido, arquivado/não arquivado).

### 📝 Compor Email
- URL: `/emails`
- Descrição: Permite ao usuário compor e enviar um novo email especificando os destinatários, assunto e corpo da mensagem. O email é salvo no banco de dados e exibido na caixa de saída do remetente.

### 📬 Visualizar Emails
- URL: `/emails/<int:email_id>`
- Descrição: Permite ao usuário visualizar um email específico, exibindo todos os detalhes do email, incluindo remetente, destinatários, assunto, corpo da mensagem e status.

### 📥 Caixa de Entrada
- URL: `/emails/inbox`
- Descrição: Exibe todos os emails recebidos pelo usuário, ordenados em ordem cronológica inversa. Emails arquivados são excluídos desta visualização.

### 📤 Caixa de Saída
- URL: `/emails/sent`
- Descrição: Exibe todos os emails enviados pelo usuário, ordenados em ordem cronológica inversa.

### 🗄️ Arquivar/Desarquivar Email
- URL: `/emails/<int:email_id>`
- Descrição: Permite ao usuário arquivar ou desarquivar um email específico, alterando o status do email.

### 1️⃣ Clone o Repositório
```sh
git clone <url_do_repositorio>
```
### 2️⃣ Instale Dependências
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure o Banco de Dados
```sh
python manage.py makemigrations mail
python manage.py migrate
```
### 4️⃣ Crie um Superusuário
```sh
python manage.py createsuperuser
```

### 5️⃣ Inicie o Servidor Django
```sh
python manage.py runserver
```

### 6️⃣ Navegue e Interaja
 - 🌐 Abra o navegador e acesse http://127.0.0.1:8000
 - 📝 Registre uma nova conta ou faça login com uma conta existente.
 - ✉️ Componha, visualize, arquive e desarquive emails.
 - 🔧 Use a interface de administração para gerenciar dados do site.

## 📂 Estrutura do Projeto
- `project3/`: Diretório principal do projeto Django.
    - `mail/`: Aplicativo Django contendo:
        - `templates/mail/`: Templates HTML para as páginas do site.
        - `static/mail/`: Arquivos CSS e JS.
        - `urls.py`: Configuração de URLs.
        - `views.py`: Lógica das views.
        - `models.py`: Definição dos modelos de dados.

## 🗺️ Rotas do Projeto
### Rotas Principais
- `index`: path("", views.index, name="index")
- `login`: path("login/", views.login_view, name="login")
- `logout`: path("logout/", views.logout_view, name="logout")
- `register`: path("register/", views.register, name="register")

### Rotas da API
- compose: path("emails", views.compose, name="compose")
    - Envia um email criado pelo usuário.

- email: path("emails/<int:email_id>", views.email, name="email")
    - Recupera os detalhes de um email específico.

- mailbox: path("emails/<str:mailbox>", views.mailbox, name="mailbox")
    - Recupera todos os emails em uma determinada caixa de correio (inbox, sent, archive).

## 📡 API
- `GET` /emails/str:mailbox
    - Descrição: Retorna uma lista de todos os emails em uma caixa de correio especificada (inbox, sent, archive) em formato JSON.
- `GET` /emails/int:email_id
    - Descrição: Retorna os detalhes de um email específico em formato JSON.
- `POST` /emails
    - Descrição: Envia um novo email com os destinatários, assunto e corpo especificados.
- `PUT` /emails/int:email_id
    - Descrição: Atualiza o status de um email (lido/não lido, arquivado/não arquivado).

## 📚 Considerações Finais
Este projeto fornece uma interface de usuário completa para gerenciar emails utilizando apenas Django e JavaScript. O foco principal é a integração entre o front-end dinâmico, gerenciado por JavaScript, e o back-end robusto provido por Django, permitindo uma experiência de usuário fluida e eficiente.

# Licença 📜

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for more information.

Copyright 2024 Iuri de Lima Ferreira


<img src="markdown/logoIuri.svg" width="200">