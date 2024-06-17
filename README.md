# 0. Description
LangChain and Elastic Collaborate to Enhance RAG with Vector Database and Semantic Reranking https://lnkd.in/eVXPUiDY

Given the expertise and prominence of both LangChain and Elastic in their respective domains, their collaboration promises significant advancements. Let's delve into the specifics of what makes this integration so powerful.

Elasticsearch Capabilities:
- Advanced Search Functionalities: Elasticsearch is renowned for its powerful and popular open-source search engine capabilities. It surpasses traditional BM25 keyword search by enabling complex search functionalities such as filtering, sorting, and advanced querying using "must" and "should" conditions. This enhances the accuracy of search results, ensuring that the materials sent to the LLM are of higher quality, thereby improving the overall quality of answers.
- Versatility in Search: By offering both keyword and vector search capabilities, Elasticsearch caters to various scenarios, compensating for the limitations of each method. This dual approach ensures comprehensive coverage of search requirements.
- Robust Distributed System: Elasticsearch is a stable distributed system that supports multiple nodes, redundant shards, and includes built-in analysis and monitoring tools. This eliminates the need for creating a custom system, providing a reliable and scalable solution out of the box.

Practical Implementation:
The Elastic team has provided an article and accompanying code to demonstrate the integration. However, the complexity of the implementation requires a thorough understanding of the details to succeed. To facilitate this, I am writing a project to create a class that simplifies the use of these tools. This will help you leverage the combined power of LangChain and Elasticsearch more easily and effectively.
By combining Elasticsearch's robust search capabilities with LangChain's advanced language processing, this collaboration is set to significantly enhance the performance and applicability of RAG (Retrieval-Augmented Generation) systems, particularly in handling big data and complex scenarios.

I found that it is still a little bit difficult to use it. so I created this application to test it. you also can use ElasticLlm class to create your own LLM application.
# 1. GET OPENAI API_KEY
get a api_key from https://platform.openai.com/api-keys

# 2. config elastic cloud
## 2.1 register
https://www.elastic.co/cloud/cloud-trial-overview
register a 15 days trail elasticsearch, collect cloud id and create a es_api_key
## 2.2 (Alternative) Install a elasticsearch and Kibana on-premises
the configuration is a little bit complex, not prefer to beginners.
## 2.2 config ML node (TO-DO)
it is very important step! Need to config 1 node as ml node, otherwise, you can't deploy your mode, because there is no ml node by default. 
## 2.3 deploy model in elasticsearch
login Kibana,
"Machine Learning" ->"Model Management" ->"Trained Models"
find model ".elser_model_2", download it and then deploy it.
![image](https://github.com/pointearth/elastic_llm/assets/1859919/7baf5d19-ad82-4052-944d-ef24b2567f41)

# 3. Config the Application
## 3.1 install process
-- install python3 and dependencies
```
brew install python
python3 -m venv .venv # only for the first running
source .venv/bin/activate
which python # show the env (option)
pip3 install -r requirements.txt # only for the first running
```
## 3.2 config
in src/config file, input all the information:
- ELASTIC_CLOUD_ID
- ES_API_KEY
- GPT_API_KEY
  
# 4 Run the Application
## 4.1. save data into elasticsearch
```
python src/save_doc.py
```
![image](https://github.com/pointearth/elastic_llm/assets/1859919/cb0e03b5-5d60-4902-86ce-385944f4fcb4)

you can change the documents in the code.
## 4.2 ask question
```
python src/question.py
```
<img width="844" alt="image" src="https://github.com/pointearth/elastic_llm/assets/1859919/db02be15-ac88-4411-adce-7fd11a5e9e09">

you can change questions in the code
# 5. exist venv
```
deactivate
```

