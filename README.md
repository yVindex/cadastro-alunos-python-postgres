<h1 align="center">🎓 Sistema de Cadastro de Alunos</h1>

<p align="center">
  CRUD completo no terminal, feito em <b>Python</b> com banco de dados <b>PostgreSQL</b>.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-database-4169E1?logo=postgresql&logoColor=white">
  <img alt="psycopg2" src="https://img.shields.io/badge/psycopg2-driver-2E7D32">
  <img alt="Interface" src="https://img.shields.io/badge/interface-terminal-black">
  <img alt="Status" src="https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen">
</p>

---

## 📑 Sumário

- [Sobre o projeto](#sobre)
- [Aluno](#aluno)
- [Funcionalidades](#funcionalidades)
- [Exemplo de uso](#exemplo-de-uso)
- [Validações e segurança](#validacoes-e-seguranca)
- [Tecnologias](#tecnologias)
- [Estrutura do projeto](#estrutura)
- [Como executar](#como-executar)
- [Banco de dados](#banco-de-dados)

---

## <a id="sobre"></a>📌 Sobre o projeto

Sistema interativo de cadastro e gerenciamento de alunos via terminal (CLI) desenvolvido em Python e integrado com PostgreSQL. O projeto faz a persistência de dados no banco de dados e conta com um CRUD completo, validação de entradas, consultas parametrizadas e cálculo de média de notas direto no banco.

---

## <a id="aluno"></a>👤 Aluno

- **Nome:** Guilherme Barbosa da Silva França
- **Matrícula:** 01879072

---

## <a id="funcionalidades"></a>✨ Funcionalidades

| Opção | Funcionalidade | Comando SQL |
|:-----:|----------------|-------------|
| **1** | ➕ Cadastrar aluno (nome, idade e nota) | `INSERT` |
| **2** | 📋 Listar todos os alunos (ID, nome, idade e nota) | `SELECT` |
| **3** | 🔍 Buscar aluno pelo nome (aceita parte do nome, sem diferenciar maiúsculas) | `SELECT ... WHERE ... ILIKE` |
| **4** | ✏️ Atualizar dados de um aluno, pelo ID | `UPDATE` |
| **5** | 🗑️ Remover aluno, pelo ID | `DELETE` |
| **6** | 📊 Mostrar a média geral das notas | `AVG()` |
| **7** | 🚪 Sair | - |

---

## <a id="exemplo-de-uso"></a>💻 Exemplo de uso

```text
-----------SISTEMA DE CADASTRO DE ALUNOS-----------
1. Cadastrar aluno
2. Listar todos os alunos
3. Buscar aluno pelo nome
4. Atualizar dados de um aluno
5. Remover aluno
6. Mostrar média geral das notas
7. Sair
---------------------------------------------------
Digite uma opção: 1
---------------------------------------------------
Digite o nome do aluno: Maria Silva
Digite a idade do aluno: 20
Digite a nota do aluno: 8,5
Aluno cadastrado com sucesso!
```

Listagem de alunos (opção 2):

```text
------------------Lista de Alunos------------------
ID: 1
Nome: Maria Silva
Idade: 20 anos
Nota: 8.5
---------------------------------------------------
```

---

## <a id="validacoes-e-seguranca"></a>🛡️ Validações e segurança

- O **nome** não pode ficar vazio (espaços nas pontas são ignorados).
- A **idade** deve ser um número inteiro entre 1 e 150.
- A **nota** deve ser um número entre 0 e 10 (aceita vírgula ou ponto: `8,5` ou `8.5`).
- O **ID** deve ser um número inteiro, e o sistema confere se o aluno existe antes de atualizar ou remover.
- Todas as consultas são **parametrizadas** (`%s`), sem concatenar valores digitados dentro do SQL, o que evita *SQL injection*.
- As credenciais do banco ficam em um arquivo **`.env`**, que não é enviado ao GitHub.

---

## <a id="tecnologias"></a>🛠️ Tecnologias

- **Python 3**
- **PostgreSQL**
- **psycopg2**: comunicação entre o Python e o PostgreSQL
- **python-dotenv**: leitura das configurações do arquivo `.env`

---

## <a id="estrutura"></a>📁 Estrutura do projeto

```text
cadastro-alunos-python-postgres/
├── connect.py                     # conexão, criação do banco e da tabela
├── sistema_cadastro_alunos_db.py  # menu, validações e funcionalidades
├── requirements.txt               # bibliotecas necessárias
├── .env.example                   # modelo das configurações do banco
├── .gitignore
└── README.md
```

---

## <a id="como-executar"></a>🚀 Como executar

### 1. Pré-requisitos

- [Python 3](https://www.python.org/downloads/) instalado
- [PostgreSQL](https://www.postgresql.org/download/) instalado e com o serviço em execução

### 2. Clonar o repositório

```bash
git clone https://github.com/yVindex/cadastro-alunos-python-postgres.git
cd cadastro-alunos-python-postgres
```

### 3. Instalar as bibliotecas

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco

Copie o arquivo `.env.example` para `.env` e troque `SUA_SENHA` pela senha do seu usuário do PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=SUA_SENHA
DB_NAME=escola
```

### 5. Executar

```bash
python sistema_cadastro_alunos_db.py
```

> 💡 No Windows, se o comando `python` não for reconhecido, use `py sistema_cadastro_alunos_db.py`.

---

## <a id="banco-de-dados"></a>🗄️ Banco de dados

O banco `escola` e a tabela `alunos` são criados automaticamente, caso ainda não existam:

```sql
CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    nota REAL NOT NULL
);
```

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | `SERIAL` (chave primária) | Identificador único, gerado automaticamente |
| `nome` | `TEXT` | Nome do aluno |
| `idade` | `INTEGER` | Idade do aluno |
| `nota` | `REAL` | Nota do aluno (0 a 10) |

---
