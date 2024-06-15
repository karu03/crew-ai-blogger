from crewai import Crew, process
from tasks import research_task, writing_task
from agents import researcher, writer


#frommating the tech focused crew with some enhancements
crew = Crew(
    agents=[researcher,writer],
    tasks=[research_task, writing_task],
)


results=crew.kickoff()
print(crew.usage_metrics)
print(results)