# Flask User API

Projeto acadêmico desenvolvido em **Python** utilizando **Flask**, com o objetivo de praticar a criação de uma API REST, operações CRUD, validação de dados, persistência em arquivo JSON e organização básica de um projeto backend.

## Tecnologias utilizadas

* Python
* Flask
* JSON
* Git e GitHub

## Funcionalidades

A API permite realizar operações de gerenciamento de usuários:

* **GET** — listar todos os usuários
* **GET por ID** — consultar um usuário específico
* **POST** — cadastrar um novo usuário
* **PUT** — editar um usuário existente
* **DELETE** — remover um usuário
* Validação dos campos obrigatórios
* Persistência dos dados em `users.json`
* Geração automática de IDs incrementais
* Respostas padronizadas em formato JSON

## Estrutura do projeto

```text
flask-user-api/
│
├── app.py
├── user.py
├── user_service.py
├── users.json
├── requirements.txt
├── .gitignore
└── venv/
```

### Descrição dos arquivos

**`app.py`**
Responsável pelas rotas da API, recebimento das requisições e retorno das respostas HTTP.

**`user.py`**
Arquivo destinado à representação/estrutura do usuário.

**`user_service.py`**
Responsável pela lógica de manipulação dos usuários, carregamento e gravação dos dados no arquivo JSON, além da geração dos IDs.

**`users.json`**
Arquivo utilizado como mecanismo de persistência dos usuários.

**`requirements.txt`**
Lista das dependências necessárias para executar o projeto.

**`.gitignore`**
Define arquivos e diretórios que não devem ser enviados ao GitHub, como o ambiente virtual.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/flask-user-api.git
```

### 2. Entrar na pasta

```bash
cd flask-user-api
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python app.py
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints

### Listar usuários

```http
GET /users
```

### Buscar usuário por ID

```http
GET /users/{id}
```

Exemplo:

```http
GET /users/1
```

### Cadastrar usuário

```http
POST /users
```

Exemplo de JSON:

```json
{
    "name": "Carlos",
    "email": "carlos@email.com"
}
```

### Atualizar usuário

```http
PUT /users/{id}
```

Exemplo:

```http
PUT /users/1
```

```json
{
    "name": "Carlos Silva",
    "email": "carlos.silva@email.com"
}
```

### Excluir usuário

```http
DELETE /users/{id}
```

Exemplo:

```http
DELETE /users/1
```

## Validação

A API verifica se:

* O corpo da requisição foi enviado;
* Os campos `name` e `email` foram informados;
* Os campos obrigatórios não estão vazios;
* O usuário informado existe nas operações de consulta, atualização e remoção.

As respostas seguem um padrão JSON para facilitar o consumo da API.

### Exemplo de resposta de sucesso

```json
{
    "success": true,
    "data": {
        "id": 3,
        "name": "Carlos",
        "email": "carlos@email.com"
    }
}
```

### Exemplo de resposta de erro

```json
{
    "success": false,
    "error": "Os campos name e email são obrigatórios"
}
```

## Persistência e geração de IDs

Os usuários são armazenados no arquivo `users.json`.

A aplicação carrega os dados do arquivo antes das operações e salva novamente o conteúdo após alterações.

Os IDs são gerados de forma incremental, utilizando como referência o maior ID atualmente armazenado:

```python
max([user["id"] for user in users], default=0) + 1
```

## Objetivo acadêmico

Este projeto foi desenvolvido como atividade prática de faculdade para consolidar conhecimentos em:

* Desenvolvimento de APIs REST;
* Python e Flask;
* Métodos HTTP;
* Manipulação de JSON;
* Validação de dados;
* Persistência de informações;
* Organização de aplicações backend;
* Controle de versão com Git e GitHub.

## Autor

**Estudante de Ciência da Computação**

Projeto desenvolvido para fins **acadêmicos e de aprendizado**.

## Licença

Este projeto foi desenvolvido para fins educacionais.
