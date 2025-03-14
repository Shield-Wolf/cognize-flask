
import openai
import os
#import logging
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

    # The above code all works

    endpoint = AZURE_OPEN_AI_ENDPOINT
    deployment = AZURE_OPEN_AI_DEPLOYMENT
    subscription_key = AZURE_OPEN_AI_KEY
    api_version = AZURE_API_VERSION

    # Initialize Azure OpenAI Service client with key-based authentication
    client = AzureOpenAI(  
        azure_endpoint=endpoint,  
        api_key=subscription_key,  
        api_version=api_version,
    )
    # client = AzureOpenAI(  
    #      azure_endpoint=endpoint,  
    #     api_key=subscription_key,  
    #     api_version=api_version
    # )
    chat_prompt = [
        {
         "role": "system",
         "content": "You are an AI assistant that helps people find accurate information."
         },
         {
             "role": "user",
             "content": prompt
         }
    ] 

    # Include speech result if speech is enabled  
    messages = chat_prompt  

    print('chat_prompt=%s' % chat_prompt)

    first_response = client.chat.completions.create(  
          model=deployment,
          messages=chat_prompt,
          max_tokens=150,  
          temperature=0.7,  
          top_p=0.95,  
          frequency_penalty=0,  
          presence_penalty=0,
          stop=None,  
          stream=False
    )

    print('first_response=%s' % first_response) 

    answer = first_response.choices[0].message.content


    # Adding a follow-up question
    messages.append(
        {"role": "assistant", "content": first_response.choices[0].message.content}
    )
    messages.append(
        {"role": "user", "content": "Please provide 5 good resources supporting this asnwer in JSON format as an array or 'resources' objects each with a 'title' and a 'url'"}
    )
    second_response = client.chat.completions.create(  
          model=deployment,
          messages=chat_prompt,
          max_tokens=750,  
          temperature=0.7,  
          top_p=0.95,  
          frequency_penalty=0,  
          presence_penalty=0,
          stop=None,  
          stream=False
    )

    print('second_response=%s' % first_response) 

    # response = prompt

    sources = second_response.choices[0].message.content

    print('sources=%s' % sources)

    #return answer
    return [answer, sources]
