from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
groq_api_key=os.environ['GROQ_API_KEY']
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

app=FastAPI(
     title="Langchain Server",
     version="1.0",
     description="A simple API Server"

)

add_routes(
    app,
    GoogleGenerativeAI(model="gemma-3-12b-it"),
    path="/genai"
)


model=ChatGroq(model_name="gemma2-9b-it",groq_api_key=groq_api_key)

## O llama2

llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")


add_routes(
    app,
    prompt1|model,
    path="/essay"


)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8000)
