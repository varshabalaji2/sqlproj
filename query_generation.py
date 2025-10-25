# query_generation.py
from query_cleaner import clean_sql_quer
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

def execute_query(query: str):
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# LLM that will generate SQL queries
generate_query = ChatOpenAI(model="gpt-4o", temperature=0)
