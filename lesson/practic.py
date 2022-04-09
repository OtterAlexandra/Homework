from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('html.html')


app.run(port=8080, debug=True)
