# 🕒 HourTracker - Controlador de Horas com Python + SQLite

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)  
[![SQLite](https://img.shields.io/badge/sqlite-database-green.svg)](https://www.sqlite.org/index.html)  
[![Tests](https://img.shields.io/badge/tests-pytest-success.svg)](https://docs.pytest.org/)  
[![License](https://img.shields.io/badge/license-Pessoal-lightgrey.svg)](#-licença)

---

## 🎯 O que é?
O **HourTracker** é um controlador de horas simples e eficiente, feito em Python, que permite registrar o tempo gasto em diferentes projetos.  
Com ele, você pode **iniciar, parar e consultar relatórios de horas** trabalhadas, tudo salvo em um banco de dados SQLite local.


## 🚀 Funcionalidades
✅ Registrar horas trabalhadas em tarefas/projetos  
✅ Listar registros existentes  
✅ Atualizar ou excluir registros  
✅ Armazenamento em **SQLite**, totalmente local e leve  
✅ Estrutura modular, organizada e testável  

---

## 🗂 Estrutura do Projeto

```bash
Projeto-Pessoal-Hour-Tracker-Python-SQLite/
│
├── tracker/                # Código-fonte principal
│   ├── __init__.py
│   ├── core.py
│   ├── storage.py
│   ├── cli.py
│   ├── db.py
│   ├── models.py
│   └── schema.sql
│
├── tests/                  # Testes automatizados
│   └── test_tracker.py
│
├── README.md               # Documentação principal
├── pyproject.toml          # Configuração do projeto
├── .gitignore              # Ignorar DB, cache, etc.
```


---

## 🚀 Na prática, para que ele serve?

- Acompanhar **quanto tempo você gastou em cada projeto** ou tarefa.  
- Manter um **histórico confiável** de sessões, salvo em banco de dados.  
- Melhorar sua **produtividade pessoal** e ter clareza sobre onde seu tempo está sendo usado.  
- Ser usado por **freelancers** para medir horas de trabalho e facilitar **cobranças a clientes**.  
- Auxiliar em **estudos ou projetos pessoais**, ajudando a gerenciar o tempo investido.

---

## 📦 Instalação

Clone o repositório e crie um ambiente virtual:

```bash
git clone https://github.com/seu-usuario/Projeto-Pessoal-Hour-Tracker-Python-SQLite.git

cd Projeto-Pessoal-Hour-Tracker-Python-SQLite
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate      # Windows/VS Code
pip install -e .
python -m tracker.cli add --task "Projeto X" --hours 5
python -m tracker.cli list


```

⚡ Uso
1. Iniciar um projeto

```bash

python cli.py start "Projeto X"

```

📌 Marca a hora de início no banco de dados.

2. Parar um projeto
```bash
python cli.py stop "Projeto X"
```

📌 Registra a hora de fim e calcula quanto tempo foi gasto.

3. Gerar relatório
```bash
python cli.py report
```

Saída esperada:
```bash
Horas acumuladas por projeto:
 - Projeto X: 2.00h
 - Projeto Y: 3.50h
```

📊 Exemplo prático

Você começa a estudar Python:
```bash
python cli.py start "Estudos Python"
```

Depois de 1h30, você para:
```bash
python cli.py stop "Estudos Python"
```

E gera o relatório:
```bash
Horas acumuladas por projeto:
 - Estudos Python: 1.50h
```

👉 Assim, você acompanha na prática quanto tempo foi investido.

📦 Banco de Dados

O banco de dados é criado automaticamente em SQLite.

O arquivo schema.sql contém a estrutura das tabelas.

O banco (hourtracker.db) é local e ignorado pelo Git (não versionado).



📜 Licença

Este é um projeto pessoal, feito apenas para estudos e prática em Python.
Não possui vínculo comercial nem garantia de suporte.

✍️ Autor

Feito com dedicação por Matheus Beiruth Miranda dos Santos  🖊️