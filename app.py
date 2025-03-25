import os
import prompter
import json_decoder
import json


from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
   print("iN iNDEX")
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cognize-logo-favicon.ico', mimetype='images/cognize-logo-favicon.ico')

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

    #Strip out the new line characters, quotes and other characters from the JSON in the response
    decoded_jason_sources = json_decoder.decode(sources)
   
    print ("decoded_jason_sources= %s" % decoded_jason_sources)
    #print ("Sources2=%s" % sources2)
    #json_result = json.loads(sources2)

    json_result = json.loads(decoded_jason_sources)


    # Get all the titles and urls from resources
    titles = []
    urls = []
    for resource in json_result['resources']:
        title = resource.get('title')
        url = resource.get('url')
        if title and url:
            titles.append(title)
            urls.append(url)

    print("Extracted titles: %s" % titles)
    print("Extracted urls: %s" % urls)


    ### Return the response to the template 
    return render_template('question.html', question = question, key = key, answer = answer, sources = sources, title1 = titles[0], url1 = urls[0], title2 = titles[1], url2 = urls[1], title3 = titles[2], url3 = urls[2], title4 = titles[3], utl4 = urls[3], title5 = titles[4], url5 = urls[4])

if __name__ == '__main__':
   app.run()
