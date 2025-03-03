import os
# import prompter
import prompter


from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

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
    #response = prompter.chatgpt(question)
    #response = "This is a canned response"
    if question:
        print('Request for home page received with question=%s' % question)
         # Call Azure OpenAI
         # Call Azure OpenAI with values
        print('Request key=%s' % os.environ.get("APP_PERMISSION_KEY" ))
        if key != os.environ.get("APP_PERMISSION_KEY"):
               print('Request for home page received with key redirecting=%s' % key)
               return redirect(url_for('index'))


    # Call Azure OpenAI
    # Call Azure OpenAI with values
    response = prompter.chatgpt(question)
    print('Response from Azure OpenAI=%s' % response)
    answer = response[0]
    sources = response[1]
    
    return render_template('question.html', question = question, key = key, answer = answer, sources = sources)
# @app.route('/question', methods=['POST'])
# def question():
#     question = request.form.get('question')
#     key = request.form.get('key')

#     if question:
#         print('Request for home page received with question=%s' % question)
#          # Call Azure OpenAI
#          # Call Azure OpenAI with values
#         print('Request key=%s' % os.environ.get("APP_PERMISSION_KEY" ))
#         if key != os.environ.get("APP_PERMISSION_KEY"):
#                print('Request for home page received with key redirecting=%s' % key)
#                return redirect(url_for('index'))

#         # Call Azure OpenAI
#         # Call Azure OpenAI with values
#         response = prompter.chatgpt(question)
#         print('Response from Azure OpenAI=%s' % response)
#         return render_template('question.html', question = question, key = key, response = response)
#     else:
#         print('Request for hello page received with no question or blank name -- redirecting')
#         return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
