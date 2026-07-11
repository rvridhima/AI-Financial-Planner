from utils import (
    load_expenses,
    generate_financial_summary,
    classify_expenses,
    calculate_financial_statistics
)

from crew import create_financial_crew

def analyze_finances(csv_file, user_details):

    df = load_expenses(csv_file)

    df = classify_expenses(df)

    income = user_details["income"]
    current_savings = user_details["current_savings"]

    stats = calculate_financial_statistics(income,current_savings,df)

    financial_summary = generate_financial_summary(stats)

    crew = create_financial_crew(financial_summary)

    result = crew.kickoff()

    return {
        "stats": stats,
        "summary": financial_summary,
        "report": str(result)
    }


def main():
    print()




if __name__ == "__main__":
    main()