import re

def clean_sql_quer(text: str) -> str:
    """Clean the SQL query by removing any unnecessary code block syntax, SQL tags, and backticks."""
    block_pattern = r"```(?:sql|SQL|SQLQuery|mysql|postgresql)?\s*(.*?)\s*```"
    text = re.sub(block_pattern, r"\1", text, flags=re.DOTALL)

    prefix_pattern = r"^(?:SQL\s*Query|SQLQuery|MySQL|PostgreSQL|SQL)\s*:\s*"
    text = re.sub(prefix_pattern, "", text, flags=re.IGNORECASE)

    sql_statement_pattern = r"(SELECT.*?;)"
    sql_match = re.search(sql_statement_pattern, text, flags=re.IGNORECASE | re.DOTALL)
    if sql_match:
        text = sql_match.group(1)

    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\s+', ' ', text)

    keywords = ['SELECT', 'FROM', 'WHERE', 'GROUP BY']
    pattern = '|'.join(r'\b{}\b'.format(k) for k in keywords)
    text = re.sub(f'({pattern})', r'\n\1', text, flags=re.IGNORECASE)

    text = text.strip()
    text = re.sub(r'\n\s*\n', '\n', text)

    return text
