# db_connection.py

from langchain_community.utilities.sql_database import SQLDatabase

# Reusable variables
db_user = "postgres"
db_password = "varsha"
db_host = "localhost"
db_name = "postgres"

# Create LangChain SQLDatabase instance
db = SQLDatabase.from_uri(
    f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
)
print("✅ Database connection object created successfully!")

