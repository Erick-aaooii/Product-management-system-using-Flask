<img src="img/Flask.png" alt="Flask img" width="100">

# API Flask para Gerenciamento de Usuários e Produtos

Esta é uma API desenvolvida em Python usando o Flask, que permite o gerenciamento de usuários e produtos. A API fornece funcionalidades para registro, login, adição, atualização, exclusão e recuperação de produtos, além de um sistema de autenticação por token.

## Funcionalidades

### Usuários
- **Registro de Usuários**: Permite que novos usuários se registrem.
- **Login de Usuários**: Usuários podem fazer login e receber um token para autenticação em futuras requisições.

### Produtos
- **Adicionar Produtos**: Permite que usuários autenticados adicionem novos produtos.
- **Obter Produtos**: Usuários autenticados podem recuperar informações sobre produtos específicos.
- **Atualizar Produtos**: Usuários autenticados podem atualizar detalhes dos produtos.
- **Deletar Produtos**: Usuários autenticados podem remover produtos do sistema.

## Tecnologias Utilizadas

- Python 3
- Flask
- JSON para armazenamento de dados
- Token JWT para autenticação

## Estrutura do Projeto

```
project/
│
├── app.py                # Arquivo principal da API
├── users.py              # Módulo para gerenciamento de usuários
├── products.py           # Módulo para gerenciamento de produtos
├── db_manager.py         # Módulo para manipulação de arquivos JSON
└── data/
    ├── users.json        # Arquivo JSON para armazenamento de usuários
    └── products.json     # Arquivo JSON para armazenamento de produtos
```

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Erick-aaooii/Product-management-system-using-Flask.git
   cd Product-management-system-using-Flask
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**
   ```bash
   pip install Flask, json
   ```

## Execução

Para iniciar a API, execute o seguinte comando:

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`.

## Como Usar

### Requisições de Usuário

#### Registrar Usuário
```http
POST /user/new
```
**Corpo:**
```json
{
    "name": "Usuário Teste"
    "email": "user@example.com",
    "password": "12345",
}
```

#### Login de Usuário
### Essa função retorna um token que deve ser colocado no cabeçalho e em todas as ações a seguir
```http
POST /user/register
```
**Corpo:**
```json
{
    "email": "user@example.com",
    "senha": "12345"
}
```

### Requisições de Produto

#### Adicionar Produto
```http
POST /products/set
```
**Corpo:**
```json
{
    "name": "Produto Teste",
    "price": 99.99,
    "quantity": 1
}
```

#### Obter Produto
```http
GET /products/get/<id>
```

#### Atualizar Produto
```http
PUT /products/update/<id>
```
**Corpo:**
```json
{
    "name": "Produto Atualizado",
    "price": 89.99
}
```

#### Deletar Produto
```http
DELETE /products/delete/<id>
```

## Autenticação

As requisições que modificam produtos requerem um token JWT que pode ser obtido após o login. O token deve ser enviado no cabeçalho `x-access-token`.

### Exemplo de Cabeçalho
```http
x-access-token: seu_token_aqui
```

## Contribuições

Qualquer pessoa pode ajudar! Este programa foi criado com fins educacionais, então, se você puder contribuir explicando o porquê das suas sugestões, isso será de grande ajuda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
