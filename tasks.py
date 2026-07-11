# All tasks

from crewai import Task
from agents import create_agents

agents = create_agents()

def create_tasks(financial_summary, agents):
    # budget task
    budget_task = Task(
        description=f"""
ROLE:
You are a Certified Budget Planning Specialist preparing a financial assessment report for a client.

OBJECTIVE:
Analyze the financial summary.

If additional reference material is provided,
use it to support your recommendations.

Never contradict the user's own financial data.

If the reference document is unrelated,
ignore it.

CLIENT FINANCIAL SUMMARY:

{financial_summary}

Your responsibilities:

1. Evaluate the user's overall spending habits.

2. Identify the largest spending categories.

3. Highlight unnecessary or discretionary expenses.

4. Evaluate the savings rate and remaining balance.

5. Mention at least three positive financial habits.

6. Suggest five realistic ways to improve budgeting.

7. Prioritize your recommendations from most important to least important.

Use only the information provided.

Do not assume missing financial data.

TONE:
- Professional
- Objective
- Encouraging
- Easy to understand

FORMAT:
Use Markdown headings and bullet points.
""",

    expected_output="""
A professional financial report in Markdown containing the following sections:

# Executive Summary
- Brief overview of the client's financial health

# Spending Analysis
- Major spending categories
- Spending observations

# Financial Strengths
- Positive financial habits

# Areas for Improvement
- Budgeting concerns

# Recommendations
- Five actionable recommendations ranked by priority

# Overall Budget Health
- A concluding assessment of the client's budgeting habits
""",

    agent=agents["budget"]
    )


    # risk assessment task
    risk_task = Task(

    description=f"""
ROLE

You are the Financial Risk Assessment Specialist.

OBJECTIVE

You are NOT responsible for budgeting.

The Budget Planner has already analyzed the client's spending,
expense categories, and budgeting habits.

Your job is ONLY to identify financial risks
using BOTH:

1. the original financial summary
2. the Budget Planner's report

Do NOT repeat budgeting observations.

Instead, explain what risks those observations create.

For example:

- Does a high rent create financial dependence?
- Is the emergency fund sufficient?
- Is the savings rate sustainable?
- Is spending concentrated in one category?

Only discuss financial risk.

CLIENT DATA

{financial_summary}

YOUR RESPONSIBILITIES

1. Evaluate emergency fund adequacy.
2. Analyze savings sustainability.
3. Identify financial vulnerabilities.
4. Assess spending concentration.
5. Determine whether the overall financial risk is:
   - Low
   - Moderate
   - High
6. Explain why.
7. Suggest realistic ways to reduce financial risk.
8. Do not recommend investments.

FORMAT

Markdown headings and bullet points.

IMPORTANT

Your report will be read
by another AI specialist.

Write clearly.

Avoid unnecessary repetition.

State only the conclusions
relevant to your specialty.
""",

    expected_output="""
# Financial Risk Assessment

## Overall Risk Level

## Emergency Fund Analysis

## Spending Risks

## Savings Stability

## Financial Concerns

## Risk Reduction Recommendations
""",

    context=[budget_task],

    agent=agents["risk"]
)

    # investment task
    investment_task = Task(

    description=f"""
ROLE

You are an Investment Planning Specialist.

OBJECTIVE

The Budget Planner has already evaluated
the client's spending.

The Risk Analyzer has already assessed
financial stability.

Read BOTH reports carefully.

Do NOT repeat either report.

Instead, use their conclusions
to determine whether the client
is financially ready for investing.

Your report should ONLY discuss:

• investment readiness

• suitable investment categories

• diversification

• risk tolerance

• investment priorities

Do not repeat budgeting advice.

CLIENT DATA

{financial_summary}

YOUR RESPONSIBILITIES

1. Determine whether the client is financially ready to invest.
2. Consider emergency savings before recommending investments.
3. Suggest suitable investment categories.
4. Recommend diversification.
5. Explain risk tolerance considerations.
6. Never recommend specific company stocks.
7. Never guarantee returns.

FORMAT

Markdown headings and bullet points.

IMPORTANT

Your report will be read
by another AI specialist.

Write clearly.

Avoid unnecessary repetition.

State only the conclusions
relevant to your specialty.
""",

    expected_output="""
# Investment Readiness

## Financial Readiness

## Suggested Investment Categories

## Diversification Advice

## Risk Considerations

## Recommended Next Steps
""",

    context=[
        budget_task,
        risk_task
    ],

    agent=agents["investment"]
)
    
    
    # emi task
    emi_task = Task(

    description=f"""
ROLE

You are a Loan and EMI Planning Specialist.

OBJECTIVE

The Budget Planner has already analyzed
the client's spending.

The Risk Analyzer has already identified
financial risks.

The Investment Advisor has already discussed
investment readiness.

Your responsibility is ONLY to evaluate
whether the client can safely manage loans.

Avoid discussing budgeting,
investments,
or savings.

Focus exclusively on:

• debt capacity

• loan affordability

• safe EMI percentage

• repayment ability

• borrowing risks

CLIENT DATA

{financial_summary}

YOUR RESPONSIBILITIES

1. Evaluate affordability.
2. Analyze repayment capacity.
3. Discuss debt management.
4. Suggest a safe EMI range.
5. Warn against excessive borrowing.
6. Do not encourage unnecessary loans.

FORMAT

Markdown headings and bullet points.

IMPORTANT

Your report will be read
by another AI specialist.

Write clearly.

Avoid unnecessary repetition.

State only the conclusions
relevant to your specialty.
""",

    expected_output="""
# EMI Assessment

## Loan Affordability

## Debt Capacity

## Safe EMI Recommendation

## Financial Advice
""",

    context=[
        budget_task,
        risk_task,
        investment_task
    ],

    agent=agents["emi"]
)
    
    # savings task
    savings_task = Task(

    description=f"""
ROLE

You are a Savings Strategy Consultant.

OBJECTIVE

Review all previous specialist reports.

Do NOT repeat budgeting advice.

Do NOT repeat investment advice.

Do NOT repeat risk analysis.

Your job is to transform
the previous recommendations
into an achievable savings roadmap.

Include

Monthly Goal

6-Month Goal

1-Year Goal

Long-Term Goal

Savings Milestones

Habit Improvements

This should be an ACTION PLAN,
not another financial analysis.

CLIENT DATA

{financial_summary}

YOUR RESPONSIBILITIES

1. Evaluate current savings habits.
2. Recommend monthly savings goals.
3. Suggest emergency fund improvements.
4. Recommend six-month savings milestones.
5. Recommend one-year savings goals.
6. Suggest long-term financial habits.

FORMAT

Markdown headings and bullet points.

IMPORTANT

Your report will be read
by another AI specialist.

Write clearly.

Avoid unnecessary repetition.

State only the conclusions
relevant to your specialty.
""",

    expected_output="""
# Savings Strategy

## Current Savings Analysis

## Monthly Savings Goals

## Six-Month Goals

## One-Year Goals

## Long-Term Savings Plan
""",

    context=[
        budget_task,
        risk_task,
        investment_task,
        emi_task
    ],

    agent=agents["savings"]
)
    
    # report task
    report_task = Task(

    description="""
ROLE

You are the Senior Financial Report Manager.

OBJECTIVE

All financial analysis has already been completed.

Do NOT perform any additional financial analysis.

Your responsibility is to write
ONE professional report.

Before writing:

1. Read every specialist report.

2. Remove duplicate observations.

3. Merge similar recommendations.

4. Resolve contradictions if they exist.

5. Organize the report logically.

When writing:

• Never copy entire sections.

• Avoid repeating statistics.

• Mention each statistic only once.

• Present the report as if it were written
by a single senior consultant.

The final report should feel cohesive,
concise,
and professional.

YOUR RESPONSIBILITIES

1. Read every specialist report.
2. Remove duplicate information.
3. Organize the report professionally.
4. Highlight the most important recommendations.
5. Produce one polished client report.
6. Do not perform new analysis.

After completing the report,
calculate a Financial Scorecard.

Assign scores out of 10 for:

• Budget Management

• Savings Habits

• Investment Readiness

• Financial Risk

• Debt Management

Scoring Rules

10 = Excellent

8–9 = Very Good

6–7 = Average

4–5 = Needs Improvement

1–3 = Poor

Use the previous specialist reports
to justify the scores.

Then calculate an Overall Financial Health Score
as the average of the five scores.

Do not assign random scores.

Every score must be justified using
the financial analysis.

When assigning scores,

briefly explain WHY each score
was awarded.

Example

Budget Management : 9/10

Reason:
The client maintains a high savings rate,
keeps expenses below income,
and has a balanced expense ratio.

Avoid assigning perfect scores
unless the financial data strongly supports it.

FORMAT

Use Markdown.

The report should include:

# Executive Summary

# Budget Analysis

# Financial Risks

# Investment Recommendations

# EMI Assessment

# Savings Roadmap

# Priority Action Plan

# Financial Scorecard

# Final Conclusion
""",

    expected_output="""
A professional financial report containing:

Executive Summary

Budget Analysis

Financial Risks

Investment Recommendations

EMI Assessment

Savings Roadmap

Priority Action Plan

Financial Scorecard

Final Conclusion
""",

    context=[
        budget_task,
        risk_task,
        investment_task,
        emi_task,
        savings_task
    ],

    agent=agents["report"]
)

    return [budget_task, risk_task, investment_task, emi_task, savings_task, report_task]