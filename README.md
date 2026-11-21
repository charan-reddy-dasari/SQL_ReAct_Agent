# 🤖 SQL ReAct Agent

An AI-powered SQL Agent built using **LangChain, OpenAI, and Streamlit** that allows users to interact with relational databases using natural language instead of writing SQL queries manually.

The agent understands user questions, inspects database schemas, generates SQL queries, executes them against the database, and provides answers in natural language.

## 🚀 Features

- **Natural Language to SQL:** Ask questions in plain English without writing SQL queries.
- **Autonomous Tool Calling:** The LLM decides which SQL tools to use based on the user's question.
- **Database Schema Inspection:** Automatically inspects available tables and their schemas.
- **SQL Query Execution:** Generates and executes SQL queries dynamically.
- **Error Handling:** Handles API, database, and agent execution errors.
- **Interactive Chat Interface:** Streamlit-based chatbot for interacting with the database.
- **Modular Architecture:** Separates agent logic from the user interface for code reusability.

## 🏗️ Architecture

```text
                  User
                   |
                   v
            Streamlit UI (app.py)
                   |
                   v
             SQL ReAct Agent
                (agent.py)
                   |
                   v
             OpenAI LLM
                   |
                   v
           SQL Database Toolkit
                   |
          +--------+---------+
          |        |         |
          v        v         v
       List     Inspect    Execute
       Tables   Schema     SQL Query
          |        |         |
          +--------+---------+
                   |
                   v
             SQLite Database
                   |
                   v
            Query Results
                   |
                   v
             OpenAI LLM
                   |
                   v
            Final Response
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM application and agent framework |
| LangChain OpenAI | OpenAI model integration |
| LangChain Community | SQL database utilities and toolkit |
| OpenAI GPT-4.1-mini | Language model |
| SQLAlchemy | Database connectivity |
| SQLite | Relational database |
| Streamlit | Interactive web interface |
| Python-dotenv | Environment variable management |
| uv | Python dependency and environment management |

## 📂 Project Structure

```text
SQL_ReAct_Agent/
│
├── agent.py
│   └── SQL Agent initialization and execution logic
│
├── app.py
│   └── Streamlit user interface
│
├── main.py
│   └── Terminal-based interface
│
├── employees_db.py
│   └── Creates and populates the SQLite database
│
├── .env
│   └── Stores OpenAI API credentials
│
├── .gitignore
│   └── Excludes sensitive and unnecessary files
│
├── pyproject.toml
│   └── Project dependencies and configuration
│
├── uv.lock
│   └── Locked dependency versions
│
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SQL_ReAct_Agent.git
```

Navigate to the project directory:

```bash
cd SQL_ReAct_Agent
```

### 2. Install uv

If uv is not already installed:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

### 3. Install project dependencies

Run:

```bash
uv sync
```

This installs the dependencies defined in `pyproject.toml` using the versions specified in `uv.lock`.

### 4. Configure OpenAI API Key

Create a `.env` file in the project root directory.

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Important:** Never commit or upload your `.env` file to GitHub.

### 5. Populate the SQLite Database

**This step is mandatory before launching the Streamlit application.**

The project uses SQLite as its relational database. The database and employee table are created and populated through `employees_db.py`.

Execute:

```bash
uv run python employees_db.py
```

This script initializes the database and inserts sample employee records.

After successful execution, the SQLite database file will be available in your project directory.

### 6. Launch the Streamlit Application

Once the database has been populated, start the application:

```bash
uv run streamlit run app.py
```

Streamlit will launch the application in your default web browser.

Default local URL:

```text
http://localhost:8501
```

## 💬 Example Queries

Once the application is running, try asking the following questions:

**Basic Queries**
- How many employees are present in the database?
- Show all available departments.
- What is the highest salary?

**Analytical Queries**
- Which department has the highest average salary?
- Find employees earning more than 80000.
- Calculate the average experience of employees in each department.

**Advanced Queries**
- Find the second-highest salary.
- Rank employees based on their salaries.
- Which department has the highest total salary expenditure?

The agent generates the appropriate SQL queries, executes them, and returns the results in natural language.

## 🧠 How the Agent Works

1. The user submits a natural-language question through the Streamlit interface.
2. The question is passed to the SQL ReAct Agent.
3. The LLM analyzes the question and determines which database tools are required.
4. The agent inspects available tables and relevant schemas.
5. The LLM generates an SQL query.
6. The SQL toolkit executes the query against SQLite.
7. The query results are returned to the LLM.
8. The LLM generates a human-readable response.

## 🔐 Security Considerations

- Store API credentials in environment variables.
- Never expose API keys in source code or public repositories.
- Use read-only database permissions in production.
- Validate SQL queries before execution.
- Restrict database access to authorized tables and operations.

Note: Instructions in an LLM system prompt alone do not guarantee read-only database access. Enforce restrictions at the database and application levels.

## 🔮 Future Enhancements

- Implement conversational memory using LangGraph.
- Add SQL query validation and security guardrails.
- Implement automatic SQL error correction.
- Display generated SQL queries and execution results in the UI.
- Integrate PostgreSQL and MySQL.
- Add LangSmith tracing and agent evaluation.
- Containerize and deploy the application using Docker.

## 👨‍💻 Author

**Charan Reddy**

AI/ML | Generative AI | NLP | LLM Applications

---

⭐ If you find this project useful, consider giving the repository a star!