from langchain.chains import create_sql_query_chain
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from operator import itemgetter
from query_cleaner import clean_sql_quer
from query_generation import execute_query, rephrase_answer
from langchain_core.prompts import ChatPromptTemplate

# final prompt (defined earlier)
final_prompt = ChatPromptTemplate.from_messages([...])

generate_query = create_sql_query_chain(llm, db, final_prompt)

chain = (
    RunnablePassthrough.assign(query=generate_query | RunnableLambda(clean_sql_quer))
    .assign(result=itemgetter("query") | execute_query)
    | rephrase_answer
)

a = chain.invoke({
    "question": inp_query,
    "to_day": "Thank you for using the LLM 2 SQL tool",
    "table_info": table_info,
    "table_metadata": str(table_metadata),
    "col_metadata": str(col_metadata)
})
print(a)
