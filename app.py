# Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from main import analyze_finances
from chatbot import ask_chatbot

if "results" not in st.session_state:
    st.session_state.results = None

if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(
    page_title="AI Financial Planner",
    page_icon="💰",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("💰 AI Financial Planner")

st.caption(
    "Multi-Agent AI Financial Advisor built using CrewAI, Ollama, Pandas and Streamlit."
)

st.markdown(
    """
Welcome to the **AI Financial Planner**.

This application analyzes your financial transactions,
evaluates your spending habits,
assesses financial risks,
provides investment suggestions,
and generates a professional AI financial report using multiple AI agents.
"""
)


# Sidebar code

st.sidebar.header("Client Information")

name = st.sidebar.text_input("Name")

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

city = st.sidebar.text_input("City")

occupation = st.sidebar.text_input("Occupation")

goal = st.sidebar.selectbox(
    "Financial Goal",
    [
        "Debt Reduction",
        "Retirement",
        "Buying a Home",
        "Buying a Car",
        "Vacation",
        "Education",
        "Wealth building"
    ]
)

# Risk Appetite
risk = st.sidebar.selectbox(
    "Risk Appetite",
    [
        "Low",
        "Moderate",
        "High"
    ]
)

# Income and Savings
income = st.sidebar.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=75000,
    step=1000
)

current_savings = st.sidebar.number_input(
    "Current Savings (₹)",
    min_value=0,
    value=180000,
    step=5000
)


# File upload
uploaded_file = st.sidebar.file_uploader(
    "Upload Expense CSV",
    type=["csv"]
)

# analyze = st.button("Generate Financial Plan")
generate = st.sidebar.button(
    "🚀 Generate AI Report"
)

# Main area
if generate:
    if uploaded_file is None:
        st.error("Please upload a CSV file.")
        st.stop()

    user_details = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "city": city,
        "goal": goal,
        "risk": risk,
        "income": income,
        "current_savings": current_savings
    }

    with st.spinner("🤖 AI agents are analyzing your finances..."):
        st.session_state.results = analyze_finances(
        uploaded_file,
        user_details
    )
        
    # Save user details too
    st.session_state.user_details = user_details

if st.session_state.results is not None:

    results = st.session_state.results
    user_details = st.session_state.user_details

    stats = results["stats"]
    
    st.success("Analysis Complete!")


    # Metric Cards
    stats = results["stats"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Monthly Income",
            f"₹{stats['income']:,}"
        )

    with col2:
        st.metric(
            "Expenses",
            f"₹{stats['total_expense']:,}"
        )

    with col3:
        st.metric(
            "Savings",
            f"₹{stats['remaining_balance']:,}"
        )

    with col4:
        st.metric(
            "Savings Rate",
            f"{stats['savings_rate']:.1f}%"
        )


    # Financial Health Score
    score = (
        stats["savings_rate"] / 10
    )

    score = min(score,10)

    st.subheader("🏆 Financial Health Score")

    st.progress(score/10)

    st.write(f"Overall Score: **{score:.1f}/10**")

    # Expense Charts
    # Category Bar Chart
    st.subheader("📊 Spending by Category")

    fig, ax = plt.subplots(figsize=(8,4))

    category_series = pd.Series(stats["category_totals"])
    category_series.sort_values().plot(
    kind="barh"
)

    ax.set_xlabel("Amount (₹)")
    ax.set_ylabel("Category")
    ax.set_title("Category-wise Expenses")

    st.pyplot(fig)


    st.subheader("🥧 Expense Distribution")

    fig2, ax2 = plt.subplots(figsize=(6,6))

    category_series.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax2
    )

    ax2.set_ylabel("")

    st.pyplot(fig2)

    # Needs vs Wants
    st.subheader("Needs vs Wants")

    st.bar_chart(stats["type_totals"])


    # AI Report
    st.subheader("📄 AI Financial Report")

    st.markdown(results["report"])

    
    # Scorecard
    score = min(stats["savings_rate"]/10, 10)

    if score >= 9:
        grade = "Excellent"
        color = "🟢"

    elif score >= 7:
        grade = "Good"
        color = "🟡"

    elif score >= 5:
        grade = "Average"
        color = "🟠"

    else:
        grade = "Needs Improvement"
        color = "🔴"

    st.subheader("🏆 Financial Health Dashboard")

    st.metric(
        "Financial Score",
        f"{score:.1f}/10"
    )

    st.progress(score/10)

    st.success(f"{color} Overall Rating: {grade}")



    # Chatbot
    st.subheader("💬 Ask the AI Financial Assistant")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask anything about your finances, spending habits, or financial goals.")
    
    if question:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("🤖 AI is formulating a response..."):
                answer = ask_chatbot(
                    question,
                    results["summary"],
                    results["report"],
                    user_details,
                    st.session_state.messages
                )
            
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


    # Downlaod Button
    st.download_button(

        label="Download Report",

        data=results["report"],

        file_name="Financial_Report.md",

        mime="text/markdown"
    )
    
else:
    st.info("Please upload a CSV file and click Generate AI Report.")