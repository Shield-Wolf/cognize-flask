import os
import prompter
import json_decoder
import json


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

    #Strip out the new line characters, quotes and other characters
    decoded_jason_sources = json_decoder.decode(sources)
   
    #quote to strip out " '{    "resource1": {        "title": "Government of Canada - About Ottawa"        "url": "https://www.canada.ca/en/government/system/crown/about-ottawa.html""    }    "resource2": {        "title": "City of Ottawa Official Website"        "url": "https://ottawa.ca/en""    }    "resource3": {        "title": "Encyclopedia Britannica - Ottawa"        "url": "https://www.britannica.com/place/Ottawa""    }    "resource4": {        "title": "National Geographic - Ottawa"        "url": "https://www.nationalgeographic.com/travel/destinations/north-america/canada/ottawa/""    }    "resource5": {        "title": "Canada.ca - Welcome to Ottawa"        "url": "https://www.canada.ca/en/canadian-heritage/services/visit-ottawa.html""    }}'

    #sources2 = '{  "resources": [    {      "title": "Official Website of the Government of Canada",      "url": "https://www.canada.ca/en/government.html"    }    {      "title": "CIA World Factbook - Canada",      "url": "https://www.cia.gov/the-world-factbook/countries/canada/"    }    {      "title": "Encyclopedia Britannica - Ottawa",      "url": "https://www.britannica.com/place/Ottawa"    }    {      "title": "History.com - Ottawa",      "url": "https://www.history.com/topics/canada/ottawa"    }    {      "title": "National Geographic - Ottawa",      "url": "https://www.nationalgeographic.com/travel/canada/ottawa"    }  ]}'

    print ("decoded_jason_sources=%s" % decoded_jason_sources)
    #print ("Sources2=%s" % sources2)
    #json_result = json.loads(sources2)

    json_result = json.loads(decoded_jason_sources)

    ###print("json result first url=%s" % json_result.sources[0].url)
    #print(python_obj["name"]) 

    #sources = second_response.choices[0].message.content

    #first_source_text = sources[0]['title']
    #first_source_url = sources[0]['url']

    #print('First source=%s' % first_source_text)
    #print('First url=%s' % first_source_url)

    # NEED TO ADD CODE TO EXTRACT THE SOURCES FROM THE RESPONSE

    
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
