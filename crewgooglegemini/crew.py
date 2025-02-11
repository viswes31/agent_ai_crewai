from crewai import Crew, Process
from agents import news_writer, news_researcher
from tasks import writer_task, researcher_task

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[researcher_task, writer_task],
    process=Process.sequential,
)

result = crew.kickoff(inputs={'topic':'AI in automotive'})
print(result)