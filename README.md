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

# 2. config elastic
## 2.1 register cloud
https://www.elastic.co/cloud/cloud-trial-overview
register a 15 day trail elasticsearch, collect cloud id and create a es_api_key
## 2.2 (Alternative) Install an elasticsearch and Kibana on-premises
the configuration is a little bit complex, and not preferred for beginners. I registered the model and wrote documents into elasticsearch, but I can't retrieve them. there is the report https://github.com/elastic/elasticsearch/issues/109778 
## 2.2 Config ML node
it is a very important step! Need to configure 1 node as an ML node, otherwise, you can't deploy your mode, because there is no ML node by default. 
go to "cloud" -> "deployments" -><your deployment"(My deployment)
<img width="998" alt="image" src="https://github.com/pointearth/elastic_llm/assets/1859919/b835fef4-b8a9-499b-843f-ad1223ecd703">
you need to add an ML node or edit an instance, and change it as an ML node. 
![image](https://github.com/pointearth/elastic_llm/assets/1859919/76093dd6-3848-43df-95a9-03aad419905e)

"Machine Learning instances" -> "Minimum size per zone" as follows:
![image](https://github.com/pointearth/elastic_llm/assets/1859919/c0a772d3-7c61-4d5b-a2c2-1926632ea99f)
I also close whatever functions you don't need, save them, and then you get:
<img width="380" alt="image" src="https://github.com/pointearth/elastic_llm/assets/1859919/e5eb59fe-3a3c-4ba1-94d0-bf4533923693">
then, go to "Machine Learning"-> "overview", you can see the node:
<img width="1409" alt="image" src="https://github.com/pointearth/elastic_llm/assets/1859919/8626fd06-abaf-49eb-9237-2989aea1934b">
and you you go to next step to deploy a model into this node.
## 2.3 Deploy model in elasticsearch
login Kibana,
"Machine Learning" ->"Model Management" ->"Trained Models"
find model ".elser_model_2", download it and then deploy it.
![image](https://github.com/pointearth/elastic_llm/assets/1859919/7baf5d19-ad82-4052-944d-ef24b2567f41)

you can check that your model are running on your ML node at "Machine Learning"-> "overview":
![image](https://github.com/pointearth/elastic_llm/assets/1859919/b94172d6-4ae3-48d5-b007-352e891b3f11)

All settings on Elastic Cloud are done!

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

