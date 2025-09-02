from langchain_ollama import ChatOllama

def get_llm_model()-> ChatOllama:
   llm= ChatOllama(model="llama3:8b",temperature=0,verbose=True)
   return llm



def invoke_llm(prompt)->str:
    
    llm=get_llm_model()
    response=llm.invoke(prompt)
    return response.content