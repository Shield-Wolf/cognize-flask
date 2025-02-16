import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
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
       return render_template('hello.html', question = question)
   else:
       print('Request for hello page received with no question or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
