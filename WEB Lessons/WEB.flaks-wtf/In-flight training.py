from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def train(prof):
    return render_template('ship.html', p=prof)


app.run(port=8080, debug=True)
