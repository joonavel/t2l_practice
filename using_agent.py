import os
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "test"

db = SQLDatabase.from_uri(os.environ["db_uri"])
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
agent_executor.invoke(
    {
        "input": "손님들과 직원들의 이름을 나열하세요. 이름이 가장 긴 사람은 누구인가요??"
    }
)