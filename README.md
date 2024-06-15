# API Básica em Flask com MySQL

Esta é uma API básica desenvolvida em Flask que utiliza MySQL como banco de dados para operações CRUD (Create, Read, Update, Delete) de usuários.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.7 ou superior
- MySQL Server
- Postman (ou ferramenta similar) para testar as APIs

## Configuração

### 1. Clone o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone git@github.com:abrahao/Flask_basic_Api.git
cd API_basica_mysql
```

### 2. Crie e Ative um Ambiente Virtual (Opcional, mas recomendado)

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
```

### 3. Instale as Dependências

Instale as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados

1. Crie um banco de dados MySQL e um usuário com permissões para acessá-lo.

2. Configure as variáveis de conexão com o banco de dados no arquivo `app/db.py`.

### 5. Execute o Aplicativo

Execute o script `run.py` para iniciar o servidor Flask:

```bash
python3 run.py
```

O servidor estará disponível em `http://localhost:5000`.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
API_basica_mysql/
│── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── routes.py
├── run.py
└── requirements.txt
```

- **`app/`**: Contém o código principal da aplicação Flask, incluindo inicialização, definição de rotas, modelos de dados e operações de banco de dados.
- **`run.py`**: Script de inicialização do servidor Flask.
- **`requirements.txt`**: Lista de dependências Python necessárias para o projeto.

## Uso da API

A API oferece endpoints básicos para gerenciar usuários:

- `POST /api/v1/usuarios`: Cria um novo usuário.
- `GET /api/v1/usuarios`: Lista todos os usuários.
- `GET /api/v1/usuarios/<user_id>`: Obtém detalhes de um usuário específico.
- `PUT /api/v1/usuarios/<user_id>`: Atualiza os detalhes de um usuário existente.
- `DELETE /api/v1/usuarios/<user_id>`: Deleta um usuário existente.

### Exemplos de Requisições

Você pode usar o Postman ou qualquer outra ferramenta para enviar requisições HTTP para testar a API.

- **POST `/api/v1/usuarios`**
  ```json
  {
    "nome": "Novo Usuário",
    "email": "novo_usuario@teste.com",
    "idade": 25
  }
  ```

- **GET `/api/v1/usuarios`**

- **GET `/api/v1/usuarios/<user_id>`**

- **PUT `/api/v1/usuarios/<user_id>`**
  ```json
  {
    "nome": "Usuário Atualizado",
    "email": "atualizado@teste.com",
    "idade": 30
  }
  ```

- **DELETE `/api/v1/usuarios/<user_id>`**

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para reportar problemas ou enviar pull requests com melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---
