import config
from elastic_llm import ElasticLlm

print("Welcome to elastic_llm")
print("Running version 1.0.0")
    
config.initialize()

texts = [
    "LangChain is a framework for developing applications powered by large language models (LLMs).",
    "Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases.",
]
elm = ElasticLlm(config)
elm.save_docs(texts)
