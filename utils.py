# Calculations

import pandas as pd
from config import CATEGORY_TYPE

file_path = "expenses.csv"

# Load CSV
def load_expenses(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe


# Calculate total expenses
def calculate_total_expense(df):
    total = df["Amount"].sum()
    return total


# Categorize expenses
def expense_by_category(df):
    category_totals = df.groupby("Category")["Amount"].sum()
    return category_totals


# Balance
def remaining_balance(income, total_expense):
    return income - total_expense


# No of transactions
def transaction_count(df):
    return len(df)


# Avg transaction
def avg_transaction(df):
    return df["Amount"].mean()


# Largest expense
def largest_expense(df):
    return df["Amount"].max()


# Smallest expense
def smallest_expense(df):
    return df["Amount"].min()


# Largest spending category
def largest_category(df):
    categories = expense_by_category(df)
    return categories.idxmax() # label of largest value


# Savings rate
def savings_rate(income, balance):
    return (balance / income) * 100


# How much of the total spending is an expense
def largest_category_percentage(catgories, total_expense):
    largest_amount = catgories.max()
    return (largest_amount / total_expense) * 100


# Current Emergency Coverage - How many months can this person survive once their income stops at constant expense rate
def emergency_fund_coverage(current_savings, total_expense):
    return current_savings / total_expense


# Expense ratio - how much of income is spent
def expense_ratio(income, total_expense):
    return (total_expense / income) * 100


def classify_expenses(df):
    df["Type"] = df["Category"].map(CATEGORY_TYPE)
    return df


def spending_by_type(df):
    return df.groupby("Type")["Amount"].sum()


def spending_percentages(type_totals):
    total = type_totals.sum()
    percentages = (type_totals / total) * 100
    return percentages # pandas divides each value (Need or Want) individually & returns multiple values


# Summary of CSV
def generate_financial_summary(stats):
    summary = f"""
MONTHLY FINANCIAL SUMMARY

Monthly Income: ₹{stats["income"]}

Total Expenses: ₹{stats["total_expense"]}

Remaining Balance: ₹{stats["remaining_balance"]}

Number of Transactions: {stats["transaction_count"]}

Average Transaction: ₹{stats["average_transaction"]:.2f}

Largest Single Expense: ₹{stats["largest_expense"]}

Smallest Expense: ₹{stats["smallest_expense"]}

Highest Spending Category: {stats["largest_category"]}

Expenses by Category:

"""

    for category, amount in stats["category_totals"].items():
        summary += f"{category}: ₹{amount}\n"

    summary += f"""==================================

FINANCIAL HEALTH METRICS

==================================

Savings Rate : {stats["savings_rate"]}%

Expense Ratio : {stats["expense_ratio"]}%

Largest Category Share : {stats["largest_category_percentage"]}%

Current Savings : ₹{stats["current_savings"]}

Emergency Coverage : {stats["emergency_coverage"]} months

"""
    summary += "\nNeeds vs Wants Spending:\n"

    for expense_type in stats["type_totals"]:
        amount = stats["type_totals"][expense_type]
        percentage = stats["type_percentages"][expense_type]

        summary += (
            f"{expense_type}: ₹{amount} "
            f"({percentage:.2f}%)\n"
        )


    return summary


def calculate_financial_statistics(income, current_savings, df):
    total = calculate_total_expense(df)
    balance = remaining_balance(income, total)
    categories = expense_by_category(df)

    type_totals = spending_by_type(df)
    type_percentages = spending_percentages(type_totals)

    count = transaction_count(df)
    average = avg_transaction(df)
    largest = largest_expense(df)
    smallest = smallest_expense(df)
    top_category = largest_category(df)

    savings = savings_rate(income, balance)
    expense = expense_ratio(income, total)
    largest_share = largest_category_percentage(categories, total)
    coverage = emergency_fund_coverage(
        current_savings,
        total
    )


    statistics = {
        "income": income,
        "total_expense": total,
        "remaining_balance": balance,
        "transaction_count": count,
        "average_transaction": average,
        "largest_expense": largest,
        "smallest_expense": smallest,
        "largest_category": top_category,
        "category_totals": categories.to_dict(),
        "current_savings": current_savings,
        "savings_rate": savings,
        "expense_ratio": expense,
        "largest_category_percentage": largest_share,
        "emergency_coverage": coverage,
        "type_totals": type_totals.to_dict(),
        "type_percentages": type_percentages.to_dict()
    }

    return statistics