from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool
##calling the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temprature = 0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

#creating a research agent
researcher = Agent(
    llm = llm,
    role = "Senior researcher",
    goal = 'uncover ground breaking technologies in {topic}',
    verbose = True,
    memory = True,
    backstory = (
        """Driven by curosit,
        you think like a genius and create hypothesis and theory, how can a AI be more advanced
        you are at the forefront of 
        innovation eager to explain and share knowledge that could change the world.
        """
    ),
    tool = [tool],
    allow_delegation =True,

)

##creating a writer agent


writer = Agent(
    llm = llm,
    role = "Senior content writer",
    goal = 'narrate the compelling tech stories about the {topic}',
    verbose = True,
    memory = True,
    backstory = (
        """ 
           with a power of simplyfying the complex terms, you craft enganging narratives that captivate and educate, bringing new 
            discoveries to light in an accessible and humours manner.
        """
    ),
    tool = [tool],
    allow_delegation =False,

)