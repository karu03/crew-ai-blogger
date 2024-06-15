from crewai import Task
from tools import *
from agents import researcher, writer
#reserach task
from dotenv import load_dotenv
load_dotenv()
import os
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
from crewai_tools import SerperDevTool
search_tool = SerperDevTool() 

research_task = Task(
    description="""
        Identifying the next big thing in {topic}.
        Analyzes and predicts the future of the {topic}.
        Generates insights on future use cases and innovative ideas 
        and things, ways to make that that happen in the real world.
        Underlines all the pros and cons and the overall narrative.
        Your final report should clearly articulate the key points,
        its market opportunities, and potential risks.
        """,
    expected_output = 'A comprehensive long report on {topic}. with images and reffernce and generated human like ideas',
    tools = [search_tool],
    agent = researcher,
    
)

#writing task
writing_task = Task(
    description=(
        "compose an insightfull article on {topic}."
        "analyzes and predict the future of the {topic}."
        "genrate insights on future use case and innovative ideas and things, ways to make that that happen in real world"
        "Focus on the latest trends on how it is impacting the industry."
        "the article should be clear, easy to understand and enganging."

    ),
    expected_output = 'A comprehensive 4-6 paragraphs long report on {topic}. with images and reffernce and generated human like ideas'
    'advancements formatted as markdown'
    'main words which carries the main theme and important should be highlighted'
    'use {topic} related images for making the article more interesting'
    'write it in the tone on of the humours, intelligent, a genius like tony stark tone and words',
    tools=[search_tool],
    agent = writer,
    async_execution = False,
    output_file = '{topic}.txt'
)


#if  __name__ == '__main__':

