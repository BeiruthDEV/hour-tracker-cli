# HourTracker CLI ⏱️

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQLite](https://img.shields.io/badge/SQLite-Persistence-green)
![Type](https://img.shields.io/badge/Type-CLI%20Tool-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📋 Project Overview
O **HourTracker** é uma ferramenta de interface de linha de comando (CLI) projetada para desenvolvedores e freelancers que necessitam de um método rápido e sem fricção para registrar horas trabalhadas.

Diferente de ferramentas web pesadas, este projeto foca na velocidade e na persistência local, utilizando **Python** para a lógica de aplicação e **SQLite** para armazenamento confiável de dados, permitindo a geração de relatórios precisos de produtividade.

## 🚀 Key Features
* **Zero Latency Logging:** Inicie e pare contadores de tempo instantaneamente via terminal.
* **Data Persistence:** Todos os registros são salvos em um banco de dados relacional local (SQLite), garantindo integridade mesmo se o computador reiniciar.
* **Detailed Reporting:** Cálculo automático de duração de sessões com agregação por tarefas.
* **Modular Architecture:** Separação clara entre camada de apresentação (CLI), lógica de negócio e persistência de dados.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** SQLite3 (Embedded)
* **Libraries:** `argparse` (CLI parsing), `datetime`

## ⚙️ Architecture
O projeto segue uma arquitetura modular para facilitar manutenção e testes:

* `cli.py`: Ponto de entrada, gerencia argumentos e comandos do usuário.
* `models.py`: Camada de abstração de dados e regras de negócio.
* `db.py`: Gerenciamento de conexões e inicialização de schemas do SQLite.
* `schema.sql`: Definição DDL da estrutura do banco de dados.

## 📦 Installation

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/BeiruthDEV/hour-tracker-cli.git](https://github.com/BeiruthDEV/hour-tracker-cli.git)
    cd hour-tracker-cli
    ```

2.  **Prepare o ambiente:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## 💻 Usage

A ferramenta expõe comandos intuitivos para o fluxo de trabalho diário:

### 1. Iniciar uma Sessão
Começa a contagem de tempo para uma tarefa específica.
```bash
python -m tracker.cli start --task "Refatoração API"
# Output: ✅ Sessão iniciada para tarefa: Refatoração API
```

### 2. Finalizar Sessão
Encerra a tarefa atual e salva o timestamp final.

```bash

python -m tracker.cli stop
# Output: 🛑 Sessão encerrada com sucesso.
```

### 3. Gerar Relatório
Exibe o histórico de trabalho e duração calculada.

```bash

python -m tracker.cli report
Exemplo de Saída:

Plaintext
```

### 📊 Relatório de Sessões

ID: 1 | Tarefa: Refatoração API | Início: 2023-10-27 10:00:00 | Fim: 2023-10-27 12:30:00 | Horas: 2.50
ID: 2 | Tarefa: Deploy AWS      | Início: 2023-10-27 14:00:00 | Fim: 2023-10-27 15:00:00 | Horas: 1.00
🔮 Future Improvements
[ ] Exportação de relatórios para CSV/JSON.

[ ] Suporte a múltiplas sessões simultâneas.

[ ] Visualização gráfica de produtividade no terminal (ASCII charts).

Desenvolvido por Matheus Beiruth.
