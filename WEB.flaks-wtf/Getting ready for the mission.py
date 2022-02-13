from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def ind(title):
    return render_template('base.html', title=title)


app.run(port=8080, debug=True)
