import config
from elastic_llm import ElasticLlm

config.initialize()

elm = ElasticLlm(config)
questions = ["What is your name?","Which frameworks can help me build LLM apps?"]
for question in questions:
    print("Question:")
    print(f"\t{question}")
    answer = elm.ask_question(question)
    print(f"Answer:")
    print(f"\t {answer}")
    print("**********************")