from dotenv import load_dotenv
import os
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "test"


db = SQLDatabase.from_uri(os.environ["db_uri"])
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
write_query = create_sql_query_chain(llm, db)
# 쿼리를 실행하는 tool 추가 = db.run(wirte_query)
execute_query = QuerySQLDataBaseTool(db=db)
chain = write_query | execute_query
result = chain.invoke({"question": "employees 테이블에서 알파벳 순으로 이름이 가장 느린 사람이 누구야?"})
print(result)