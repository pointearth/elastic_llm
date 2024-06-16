# 0. Description
LangChain and Elastic work together, both of them are the kings in their own areas, so I curious, how powerful it will be. Based on https://www.elastic.co/search-labs/blog/langchain-collaboration
I found that it is still a little bit difficult to use it. so i created this application to test it. 
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

