# Crew

from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

def create_financial_crew(financial_summary):
    agents = create_agents()
    tasks = create_tasks(financial_summary, agents)

    crew = Crew(
        agents = list(agents.values()), 
        tasks = tasks,
        process=Process.sequential,
        verbose = True
    )

    return crew
