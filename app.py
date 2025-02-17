import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from azure.identity import DefaultAzureCredential

from azure.keyvault.secrets import SecretClient

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   AZURE_KEY_VAULT_URL = os.environ.get("AZURE_KEY_VAULT_URL")
   print('AZURE_KEY_VAULT_URL=%s' % AZURE_KEY_VAULT_URL)
   AZURE_OPEN_AI_ENDPOINT = os.environ.get("AZURE_OPEN_AI_ENDPOINT")
   print('AZURE_OPEN_AI_ENDPOINT=%s' % AZURE_OPEN_AI_ENDPOINT)
   AZURE_OPEN_AI_KEY = os.environ.get("AZURE_OPEN_AI_KEY")
   print('AZURE_OPEN_AI_KEY=%s' % AZURE_OPEN_AI_KEY)
   AZURE_OPEN_AI_REGION = os.environ.get("AZURE_OPEN_AI_REGION")
   print('AZURE_OPEN_AI_REGION=%s' % AZURE_OPEN_AI_REGION)
   AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID")
   print('AZURE_TENANT_ID=%s' % AZURE_TENANT_ID)
   
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   question = request.form.get('question')

   if question:
       print('Request for home page received with question=%s' % question)
        # Call Azure OpenAI
        # Call Azure OpenAI with values
        
       return render_template('hello.html', question = question)
   else:
       print('Request for hello page received with no question or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
