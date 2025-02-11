from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

researcher_task=Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opprtunities and potential risks."
        ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends',
    tools=[tool],
    agent=news_researcher
)

writer_task=Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This articule should be easy to understand, engaging, and positive."
        "Provide compelling examples and statics to keep the reader interested."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)