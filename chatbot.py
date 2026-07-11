from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

# api_key = os.getenv("OPENROUTER_API_KEY")


def ask_chatbot(question, financial_summary, ai_report, user_details, chat_history):
    # llm = LLM(model="openrouter/meta-llama/llama-3.1-8b-instruct", api_key=api_key)
    llm = LLM(
        model="ollama/llama3.2:1b",
        base_url="http://localhost:11434"
    )

    history = ""
    for message in chat_history:
        history += f'{message["role"].upper()}: {message["content"]}\n'


    prompt = f"""
You are a professional AI Financial Assistant.

Your job is to answer questions ONLY using
the information provided below.

Do not invent numbers.

If the user asks something unrelated to
personal finance, politely refuse.

==========================
USER PROFILE
==========================

Name: {user_details["name"]}
Age: {user_details["age"]}
Occupation: {user_details["occupation"]}
City: {user_details["city"]}

Financial Goal:
{user_details["goal"]}

Risk Appetite:
{user_details["risk"]}

==========================
FINANCIAL SUMMARY
==========================

{financial_summary}

==========================
AI FINANCIAL REPORT
==========================

{ai_report}

==========================
PREVIOUS CONVERSATION
==========================

{history}

==========================
CURRENT QUESTION
==========================

{question}
"""
    response = llm.call(prompt) 
    # response = llm.invoke(prompt)

    return response

