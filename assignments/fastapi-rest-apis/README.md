# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para consultar e cadastrar livros, praticando rotas HTTP, parâmetros de caminho, validação de dados e códigos de status.

## 📝 Tarefas

### 🛠️ Implementar endpoints de leitura

#### Descrição
Complete as rotas `GET` no arquivo inicial para listar livros e consultar um livro pelo identificador. Os dados devem ficar em uma lista em memória. Instale as dependências com `python -m pip install fastapi uvicorn` e execute a API com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI e disponibilizar `GET /books` para retornar todos os livros como JSON
- Disponibilizar `GET /books/{book_id}` usando um parâmetro de caminho inteiro para retornar um único livro
- Retornar o status HTTP `404` quando o identificador solicitado não existir

### 🛠️ Cadastrar livros com validação

#### Descrição
Adicione uma rota para cadastrar livros recebendo os dados no corpo da requisição. Use o modelo Pydantic fornecido no arquivo inicial e verifique as rotas e respostas pela interface interativa em `/docs`.

Exemplo de corpo da requisição:

```json
{
  "title": "Dune",
  "author": "Frank Herbert"
}
```

#### Requisitos
O programa concluído deve:

- Disponibilizar `POST /books` com campos `title` e `author` obrigatórios e não vazios
- Criar um identificador inteiro único, armazenar o novo livro e retorná-lo como JSON
- Responder com status HTTP `201` ao criar um livro
- Deixar o FastAPI retornar um erro de validação para dados inválidos e confirmar o comportamento em `/docs`
