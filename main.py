
from flask import Flask

app = Flask(__name__)

# changes all routes to utilize multi-line HTML
@app.after_request
def treat_as_html(response):
    response.headers["content-type"] = "text/html"
    return response

@app.route('/')
def index():
    return """<h1>Home page!</h1>'
<p>Here is p tag!</p>
<p>Here is another p tag!</p>
"""
@app.route('/about')
def about():
    return """<h2>About page!</h2>'
<p>Here is p tag!</p>
<p>Here is another p tag!</p>
"""

app.run(host='0.0.0.0', port=81)
