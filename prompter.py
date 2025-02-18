import openai
import os
from openai import AzureOpenAI 

system_message = """
You are a chat bot. Your name is Cognize and
you have one goal: figure out what people need.
You communicate effectively and succinctly.
"""

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
    
    endpoint = AZURE_OPEN_AI_ENDPOINT
    deployment = AZURE_OPEN_AI_DEPLOYMENT
    subscription_key = AZURE_OPEN_AI_KEY

    # Initialize Azure OpenAI Service client with key-based authentication    
    client = AzureOpenAI(  
        azure_endpoint=endpoint,  
        api_key=subscription_key,  
        api_version="2024-05-01-preview",
    )
    

    #Prepare the chat prompt 
    chat_prompt = [
        {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
        },
        {
            "role": "user",
            "content": prompt
        }
    ] 
    
    # Include speech result if speech is enabled  
    messages = chat_prompt  
    
    # Generate the completion  
    completion = client.chat.completions.create(  
        model=deployment,
        messages=messages,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        stop=None,  
        stream=False
    )

    completion_json = completion.to_json()
    print("The complete json is:" + completion_json) 

    response = completion.choices[0].message.content
    print("the message is: " + response) 
    
    return response
