import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()
def set_environment():
    print(os.environ["OPENAI_API_BASE"]) 
    print(os.environ["OPENAI_MODEL_NAME"])
    print(os.environ["OPENAI_API_KEY"]) 

def create_agent():
    return Agent(
        role="Summarizer",
        goal="summarizing large texts in understandable language",
        backstory="""Answer with nothing but the structured flow. Do not mention the process in your answer. Do not mention the Article in your summary. Act like you write a completely new Article. Always Answer in the whole answer in English! Use Markdown for formating.
                    Structured process:
                    # Title:
                    create a suitable title for the content and include the link of the article in the title as hyperlink in markdown format
                    ## Keypoints:
                    summarise the content in 5-10 really short key points in bullet points
                    ## Summary:
                    Create a summary of the entire content as continuous text
                    ## Why you should care:
                    create a short list of points why the content could be important for future events""",
        verbose=True,
        allow_delegation=False,
    )

def create_task(content, url):
    return Task(
        description = f"Summarize the following News Article:\n{content}\nArticle URL:\n{url}",
        agent=create_agent(),
        expected_output="Well summarised content. With all instructions followed as described",
        allow_delegation=False,
    )

def initialize_crew(content, url):
    summarizer = create_agent()
    summarize_task = create_task(content, url)
    return Crew(
        agents=[summarizer],
        tasks=[summarize_task],
        verbose=2,
        process=Process.sequential,
    )

def summarize(content, url):
    set_environment()
    crew = initialize_crew(content, url)
    output = crew.kickoff()
    return output
