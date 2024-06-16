# config.py

AUTHOR = "Simon Chan"
ELASTIC_CLOUD_ID = "input your cloud id"
ES_API_KEY= "input your es_api_key"
ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "input your username for on-premises es"
ELASTIC_INDEX = "rag-example"
ELASTIC_MODEL_ID = ".elser_model_2"
ES_URL = "http://localhost:9200"
GPT_API_KEY="input your GPT API_KEY"
ES_CONNECTION_DETAILS= {
}

def initialize():
    print("Configuration initialized.")
    print(f"Author: {AUTHOR}")
    
    if ELASTIC_CLOUD_ID:
        print(f"ELASTIC_CLOUD_ID:  {ELASTIC_CLOUD_ID}")
        ES_CONNECTION_DETAILS["es_cloud_id"] = ELASTIC_CLOUD_ID
        ES_CONNECTION_DETAILS["es_api_key"] =ES_API_KEY
    else:
        print(f"ES_URL: {ES_URL}")
        print(f"ELASTIC_USERNAME: {ELASTIC_USERNAME}")
        ES_CONNECTION_DETAILS["es_url"] = ES_URL
        ES_CONNECTION_DETAILS["es_user"] = ELASTIC_USERNAME
        ES_CONNECTION_DETAILS["es_password"] = ELASTIC_PASSWORD
    
    ES_CONNECTION_DETAILS["index_name"] = ELASTIC_INDEX
    print(f"ELASTIC_MODEL_ID: {ELASTIC_MODEL_ID}")
    print(f"ELASTIC_INDEX: {ELASTIC_INDEX}")