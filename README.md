# 💰 AI Financial Planner

An AI-powered Multi-Agent Financial Advisory System built using **CrewAI**, **Streamlit**, **Pandas**, and **Ollama**.

The application analyzes a user's financial transactions, evaluates spending habits, assesses financial health, generates personalized financial recommendations using multiple AI agents, and provides an interactive chatbot for follow-up financial queries.

---

## Features

- 📊 Expense Analysis from CSV
- 🤖 Multi-Agent Financial Advisory System
- 💹 Financial Health Dashboard
- 📈 Expense Visualization
- 💰 Savings & Budget Analysis
- 🏦 Loan & EMI Recommendations
- 📉 Financial Risk Assessment
- 📈 Investment Suggestions
- 💬 AI Financial Chatbot
- 📄 Downloadable Financial Report
- 🔒 Offline AI using Ollama

---

## Technologies Used

### Programming Language

- Python

### AI Framework

- CrewAI

### Local LLM

- Ollama
- Llama 3.2 (1B)

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Streamlit

### Environment

- Python Virtual Environment
- dotenv

---

## Project Structure

```
FinancialPlanner/
│
├── agents.py
├── tasks.py
├── crew.py
├── chatbot.py
├── main.py
├── utils.py
├── app.py
│
├── data/
    ├── expenses.csv
├── requirements.txt
└── README.md
```

---

## Multi-Agent Architecture

The application consists of six specialized AI agents.

### Budget Planning Agent

- Analyzes spending habits
- Identifies unnecessary expenses
- Suggests budgeting improvements

### Investment Advisor

- Provides investment guidance
- Suggests diversification strategies
- Recommends long-term planning

### Loan & EMI Advisor

- Evaluates borrowing capacity
- Suggests responsible EMI planning

### Financial Risk Analyzer

- Detects financial vulnerabilities
- Evaluates emergency fund coverage
- Identifies overspending risks

### Savings Planner

- Recommends savings strategies
- Helps achieve financial goals

### Report Manager

- Combines all specialist reports
- Removes duplicate recommendations
- Produces the final financial report

---

## Workflow

```
Expense CSV
      │
      ▼
Data Cleaning
      │
      ▼
Financial Statistics
      │
      ▼
Financial Summary
      │
      ▼
CrewAI Multi-Agent Analysis
      │
      ▼
Professional AI Report
      │
      ▼
Dashboard + Charts
      │
      ▼
Financial Chatbot
```

---

## Dashboard

The Streamlit dashboard provides:

- Monthly Income
- Total Expenses
- Remaining Savings
- Savings Rate
- Financial Health Score
- Category-wise Expense Chart
- Expense Distribution Pie Chart
- Needs vs Wants Analysis

---

## AI Chatbot

After the report is generated, users can ask follow-up questions such as:

- Can I afford to buy a house?
- How long until I can buy a car?
- How can I reduce unnecessary expenses?
- Should I invest more or save more?
- How can I improve my financial score?

The chatbot answers based on:

- User profile
- Financial summary
- AI-generated report
- Previous conversation history

---

## Offline AI

The application supports completely offline execution using **Ollama**.

Model used:

```
llama3.2:1b
```

Download the model:

```bash
ollama pull llama3.2:1b
```

Run Ollama:

```bash
ollama serve
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd FinancialPlanner
```

Create virtual environment

```bash
python -m venv myenv
```

Activate environment

Windows

```bash
myenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## Sample Input

Upload a CSV file containing financial transactions.

Example:

| Date | Category | Amount |
|------|----------|---------|
| 01-01-2026 | Groceries | 3500 |
| 02-01-2026 | Fuel | 1800 |
| 03-01-2026 | Entertainment | 2200 |

---

## Future Enhancements

- PDF Financial Report Export
- Bank Statement Upload
- Insurance Document Analysis
- Loan Eligibility Prediction
- Investment Portfolio Tracking
- RAG-based Financial Knowledge Base
- Voice-enabled Financial Assistant

---

## Author

**Reddy Velangani Ridhima**

B.Tech Computer Science & Engineering

---

## License

This project is developed for educational purposes.
