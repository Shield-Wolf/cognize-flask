import os
import prompter
import prompter_basic


from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from azure.identity import DefaultAzureCredential

from azure.keyvault.secrets import SecretClient

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cognize-logo-favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/question', methods=['POST'])
def question():
    question = request.form.get('question')
    key = request.form.get('key')                               
    response ="canned response"
    
    return render_template('question.html', question = question, key = key, response = response)
#@app.route('/question', methods=['POST'])
# def question():
#    question = request.form.get('question')
#    key = request.form.get('key')

#    if question:
#        print('Request for home page received with question=%s' % question)
#         # Call Azure OpenAI
#         # Call Azure OpenAI with values
#        print('Request key=%s' % os.environ.get("APP_PERMISSION_KEY" ))
#        if key != os.environ.get("APP_PERMISSION_KEY"):
#               print('Request for home page received with key redirecting=%s' % key)
#               return redirect(url_for('index'))

#        # Call Azure OpenAI
#        # Call Azure OpenAI with values
#        response = prompter_basic.chatgpt(question)
#        print('Response from Azure OpenAI=%s' % response)
#        return render_template('question.html', question = question, key = key, response = response)
#    else:
#        print('Request for hello page received with no question or blank name -- redirecting')
#        return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
