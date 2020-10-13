from flask import Flask, render_template


app = Flask(__name__)


# The index page. In this case, the only GET request
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', **locals())
