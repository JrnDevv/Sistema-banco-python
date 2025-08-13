# Sistema de Gerenciamento de Contatos

## Descrição
Este projeto é um sistema de gerenciamento de contatos desenvolvido em Python, utilizando MySQL como banco de dados. Ele permite adicionar, listar, buscar, atualizar e deletar contatos de forma prática via terminal.

---

## Funcionalidades
- Inserir novos contatos (nome, telefone, e-mail)
- Listar todos os contatos cadastrados
- Buscar contatos por nome
- Atualizar informações de um contato
- Deletar contatos existentes

---

## Tecnologias Utilizadas
- Python 3.x
- MySQL
- Biblioteca `mysql-connector-python`

---

## Como Configurar

1. **Clonar o repositório**
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
Instalar dependências

pip install mysql-connector-python
Configurar o banco de dados

Crie um banco de dados contatos_db no MySQL.

Crie a tabela contatos com os campos: id (INT, PK, AUTO_INCREMENT), nome (VARCHAR), telefone (VARCHAR), email (VARCHAR).

CREATE DATABASE contatos_db;
USE contatos_db;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL
);
Atualizar dados de conexão

Abra o arquivo db.py e configure os dados de conexão com seu MySQL:

host = "localhost"
user = "root"
password = "SUA_SENHA"
database = "contatos_db"
Executar o projeto

python db.py
