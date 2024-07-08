from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 使用較便宜的模型名稱
MODEL_NAME = "gpt-3.5-turbo"

# 2. Create model
model = ChatOpenAI(api_key=OPENAI_API_KEY, model=MODEL_NAME)

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser
