
import openai
import os
from openai import AzureOpenAI 
#from openai import AzureOpenAI 

def chatgpt(prompt):
    print('Request for index page received')
    AZURE_KEY_VAULT_URL = os.environ.get("AZURE_KEY_VAULT_URL")
    print('PROMPT AZURE_KEY_VAULT_URL=%s' % AZURE_KEY_VAULT_URL)
    AZURE_OPEN_AI_ENDPOINT = os.environ.get("AZURE_OPEN_AI_ENDPOINT")
    print('PROMPT AZURE_OPEN_AI_ENDPOINT=%s' % AZURE_OPEN_AI_ENDPOINT)
    AZURE_OPEN_AI_KEY = os.environ.get("AZURE_OPEN_AI_KEY")
    print('PROMPT AZURE_OPEN_AI_KEY=%s' % AZURE_OPEN_AI_KEY)
    AZURE_OPEN_AI_REGION = os.environ.get("AZURE_OPEN_AI_REGION")
    print('PROMPT AZURE_OPEN_AI_REGION=%s' % AZURE_OPEN_AI_REGION)
    AZURE_OPEN_AI_DEPLOYMENT = os.environ.get("AZURE_OPEN_AI_DEPLOYMENT")
    print('PROMPT AZURE_OPEN_AI_DEPLOYMENT=%s' % AZURE_OPEN_AI_DEPLOYMENT)
    AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID")
    print('PROMPT AZURE_TENANT_ID=%s' % AZURE_TENANT_ID)
    APP_PERMISSION_KEY = os.environ.get("APP_PERMISSION_KEY")
    print('PROMPT APP_PERMISSION_KEY=%s' % APP_PERMISSION_KEY)
    AZURE_API_VERSION = os.environ.get("AZURE_API_VERSION")
    print('PROMPT AZURE_API_VERSIONY=%s' % AZURE_API_VERSION)

    endpoint = AZURE_OPEN_AI_ENDPOINT
    deployment = AZURE_OPEN_AI_DEPLOYMENT
    subscription_key = AZURE_OPEN_AI_KEY
    api_version = AZURE_API_VERSION
    return "This is a canned response from prompter"
