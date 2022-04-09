from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
def answer(title):
    return render_template('base.html', title=title)


@app.route('/auto_answer')
def auto(title):
    pass


app.run(port=8080, debug=True)
