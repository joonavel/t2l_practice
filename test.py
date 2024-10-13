from dotenv import load_dotenv
import os
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "test"


db = SQLDatabase.from_uri(os.environ["db_uri"])
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "employees 테이블에서 가장 나이든 사람이 누구야?"})
print(f"response: {response}")
print(f"result: {db.run(response)}")

