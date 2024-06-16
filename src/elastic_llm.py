import os
import config
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import OpenAIEmbeddings
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

class ElasticLlm:
    def __init__(self, config):
        self.es_store = ElasticsearchStore(
            **config.ES_CONNECTION_DETAILS,
            strategy=ElasticsearchStore.SparseVectorRetrievalStrategy(model_id=config.ELASTIC_MODEL_ID)
        )
        llm = ChatOpenAI(api_key=config.GPT_API_KEY)
        prompt = hub.pull("rlm/rag-prompt")  # standard prompt from LangChain hub
        retriever = self.es_store.as_retriever()
        self.rag_chain = (
            {"context": retriever | ElasticLlm._format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    def save_docs(self, docs):
        self.es_store.add_texts(docs)
        
    def ask_question(self, question:str):
        answer = self.rag_chain.invoke(question)
        return answer
    
    @classmethod
    def _format_docs(cls, docs):
        return "\n\n".join(doc.page_content for doc in docs)