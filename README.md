# 🕒 HourTracker - Controlador de Horas com Python + SQLite

O **HourTracker** é um controlador de horas simples e eficiente, feito em Python, que permite registrar o tempo gasto em diferentes projetos.  
Com ele, você pode **iniciar, parar e consultar relatórios de horas** trabalhadas, tudo salvo em um banco de dados SQLite local.

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
git clone https://github.com/seu-usuario/hourtracker.git
cd hourtracker
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
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

📜 Licença

Este é um projeto pessoal, feito apenas para estudos e prática em Python.
Não possui vínculo comercial nem garantia de suporte.

✍️ Autor

Feito com dedicação por Matheus Beiruth Miranda dos Santos  🖊️