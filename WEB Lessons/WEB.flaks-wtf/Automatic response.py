from flask import Flask, render_template

app = Flask(__name__)

persons = {}


@app.route('/answer')
@app.route('/auto_answer/')
def answer():
    person = persons['']
    return render_template('base.html', title='', person=person)


app.run(port=8080, debug=True)
